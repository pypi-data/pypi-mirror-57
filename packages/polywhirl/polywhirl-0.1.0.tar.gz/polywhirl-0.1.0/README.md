# Poliwhirl



Are you working with an unfamiliar database and feeling confused?

Do you find yourself running `SELECT * FROM TABLE LIMIT 100` queries to remind yourself possible values of key fields?

Do these values slowly change over the course of years, with no clear documentation from upstream data producers?

If you answered "yes" to any of the above questions, this package may be for you. 



![Image of Poliwhirl pokemon](https://raw.githubusercontent.com/asdfgeoff/polywhirl/master/poliwhirl.png)





## What it does

Poliwhirl helps you orient yourself in an unfamiliar database by generating useful HTML reports (via [pandas-profiling](https://github.com/pandas-profiling/pandas-profiling)) for key tables you specify. It saves all these outputs to a single directory, which you can index locally with Spotlight or [Alfred](https://www.alfredapp.com/), or even deploy to some internal static website for your team.




## Installing

You can install this package via pip:

```
pip install polywhirl
```



## Features and usage

Polywhirl takes a single argument of a yaml file containing the structure of the database you'd like to profile. The format of this yaml file approximately follows that of dbt's [schema.yml](https://docs.getdbt.com/docs/schemayml-files). A template file `tables.yml` is provided for you, but you'll need to input the lists of schemas and tables specific to your own database.

```sh
polywhirl tables.yml
```



Polywhirl currently supports these connections:

1. BigQuery (use `name: bigquery` in `tables.yml`)
2. Redshift (use `name: redshift` in `tables.yml`)



For the sake of performance, polywhirl will pull a random sample of 10k rows from each table.
For Redshift, it supports defining a [sortkey](https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html) for each table, which is used to limit data to the most recent 90 days. This improves performance on large tables.



BigQuery credentials are handled by `pandas.read_gbq()` which relies on the [`pandas-gbq`](https://pandas-gbq.readthedocs.io/en/latest/howto/authentication.html) package. 

Redshift credentials are requested on first run, then stored locally in your system keychain using the [keyring](https://github.com/jaraco/keyring#what-is-python-keyring-lib) package.



## FAQ

#### Do you realize you misspelled [Poliwhirl](https://bulbapedia.bulbagarden.net/wiki/Poliwhirl_(Pok%C3%A9mon))?

Yes I noticed this as I was writing this README—but it's too late—the name has grown on me. 



## Todo

Would like to get to the following in the future, so feel free to send PRs my way on any of these:

- Add equivalent of Redshift sortkey to BigQuery logic, to prevent unnecessary full table scans
- Compile .html outputs into a searchable static website
- Automated tests (w/ pytest)