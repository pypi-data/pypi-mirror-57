import os
from abc import ABC
import keyring
import getpass
from typing import List, Tuple
import yaml
from tqdm import tqdm
import click
import pandas as pd
import pandas_profiling
import pandas_gbq
from jinja2 import Template


def get_or_set_cred(app: str, username: str) -> str:
    """ Load a specific credential from system keychain, otherwise prompt user for input """
    stored_cred = keyring.get_password(app, username)
    if stored_cred:
        return stored_cred
    else:
        given_cred = getpass.getpass(prompt=f'Enter your {username} for {app}: ')
        keyring.set_password(app, username, given_cred)
        return given_cred


def resolve_redshift_credentials() -> str:
    """ Load all necessary credentials for connection to Redshift database """
    creds = {
        cred_name: get_or_set_cred(app='Redshift', username=cred_name)
        for cred_name in ['username', 'password', 'host', 'port']
    }

    return 'postgresql://{username}:{password}@{host}:{port}'.format(**creds)


class TableReport(ABC):
    """ Abstract base class for a report of a table, agnostic of underlying database. """

    def __init__(
        self,
        db: str,
        schema: str,
        table: str,
        connection_type: str = None,
        root_output_dir: str = 'output',
        sample_size: int = 10000,
        *args,
        **kwargs,
    ):
        self.db, self.schema, self.table = db, schema, table
        self.root_output_dir = root_output_dir
        self.sample_size = sample_size
        self.conn_type = connection_type

    def _query_db(self):
        """ Database-specific logic for querying data """
        raise NotImplementedError

    def _resolve_path(self) -> str:
        """ Make necessary directory structure if it does not already exist """
        output_dir = os.path.join(
            self.root_output_dir, self.conn_type, self.db, self.schema
        )

        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        return os.path.join(output_dir, f'{self.table}.html')

    def run(self, open_file=False, overwrite=False) -> None:
        """ Execute query against db and generate pandas-profiling report """
        output_path = self._resolve_path()
        if not overwrite and os.path.isfile(output_path):
            tqdm.write(f'Skipping because already exists: {output_path}')
            return None
        else:
            tqdm.write(f'Generating report for: {output_path}')
            df = self._query_db()
            report = df.profile_report(
                title=f'{self.schema}.{self.table}',
                correlations={'cramers': False, 'recoded': False},
            )
            report.to_file(output_file=output_path)

        if open_file:
            import webbrowser

            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open(self.output_path)


class RedshiftTableReport(TableReport):
    """ Handles logic specifically for Amazon Redshift (connection, sortkey for performance, etc.) """

    query_template = """

    SELECT * 
    FROM {{ schema }}.{{ table }}
    {% if sortkey -%}
    WHERE {{ sortkey }} >= CURRENT_DATE - INTERVAL '90 days'
    {%- endif %}
    ORDER BY RANDOM()
    LIMIT {{ limit }}

    """
    cx_str = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn_type = 'redshift'
        if 'sortkey' in kwargs:
            self.sortkey = kwargs['sortkey']
        else:
            self.sortkey = None

    @classmethod
    def _get_conn(cls):
        if not cls.cx_str:
            cls.cx_str = resolve_redshift_credentials()
        return cls.cx_str

    def _query_db(self) -> pd.DataFrame:
        cx_str = f'{self._get_conn()}/{self.db}'
        sql = Template(RedshiftTableReport.query_template).render(
            schema=self.schema,
            table=self.table,
            sortkey=self.sortkey,
            limit=self.sample_size,
        )
        tqdm.write(sql)
        return pd.read_sql(sql, cx_str)


class BigQueryTableReport(TableReport):
    """ Handles logic specifically for Google BigQuery. Currently no performance optimizations in place. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn_type = 'bigquery'

    def _query_db(self) -> pd.DataFrame:
        sql = f'SELECT * FROM {self.schema}.{self.table} ORDER BY RAND() LIMIT {self.sample_size}'
        return pandas_gbq.read_gbq(sql, dialect='standard', project_id=self.db)


def parse_yaml_to_reports(yaml_path: str) -> List[TableReport]:
    """ Parse a config yaml into a list of TableReport objects """

    report_funcs = {'bigquery': BigQueryTableReport, 'redshift': RedshiftTableReport}

    with open(yaml_path, 'r') as stream:
        yaml_contents = yaml.safe_load(stream)
        connection_type = yaml_contents['name']
        reports = []
        for project in yaml_contents['projects']:
            for schema in project['schemas']:
                for table in schema['tables']:
                    params = dict(
                        db=project['name'], schema=schema['name'], table=table['name']
                    )
                    if 'sortkey' in table.keys():
                        params.update({'sortkey': table['sortkey']})
                    reports.append(report_funcs[connection_type](**params))
        return reports


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--overwrite', is_flag=True, help='Overwrite existing files rather than skipping')
def main(filename, overwrite):
    """
    Args:
        filename (str): Path to YAML file containing structure of database to profile.
    """

    reports = parse_yaml_to_reports(filename)
    for report in tqdm(reports, desc='Generating reports', unit='table'):
        report.run(overwrite=overwrite)


if __name__ == '__main__':
    main()
