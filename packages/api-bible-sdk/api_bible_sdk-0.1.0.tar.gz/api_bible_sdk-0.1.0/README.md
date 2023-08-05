# API.Bible SDK

This SDK wraps the [api.bible](https://scripture.api.bible/) API for use in python applications.


## Getting Started

### Prerequisites

#### [Python 3.7](https://www.python.org/)

Follow the instruction on the [Python Download Page](https://www.python.org/downloads/)


#### [Pipenv](https://docs.pipenv.org/en/latest/)

```
$ pip install pipenv
```

### Installing

Use pipenv to install the dependancies

```
$ pipenv install
```

## Running the tests

Pytest is installed as part of the dependancies run the tests with

```
$ pipenv run pytest
```

### Linting

Black is installed for linting exectue it with

```
pipenv run black api_bible_sdk/ tests/
```

## Built With

* [api.bible](https://scripture.api.bible/) - The backend API
* [Python](https://www.python.org/) - The programming language
* [Pipenv](https://docs.pipenv.org/en/latest/) - Dependancy managment

## Contributing

Any help or suggestions you may have will be greatly appriciated. If you have the time open a MR and I will do me best to get to it promptly.

## Authors

* **Matthew Birky** - *Initial work* - [mbirky](https://gitlab.com/coldkey.21)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
