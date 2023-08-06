import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='polywhirl',
    version='0.1.0',
    python_requires='>=3.6.0',
    description='Run pandas-profiling HTML reports for a given list of database tables.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/asdfgeoff/polywhirl',
    license='MIT',
    packages=['polywhirl'],
    install_requires=['pandas', 'pandas-profiling', 'pandas_gbq', 'PyYAML', 'tqdm', 'jinja2', 'click'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'polywhirl = polywhirl.__main__:main'
        ]}
)
