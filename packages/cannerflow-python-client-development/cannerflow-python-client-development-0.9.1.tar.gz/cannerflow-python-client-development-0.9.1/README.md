![Build Status](https://travis-ci.org/canner/cannerflow-python-client.svg?branch=master)

# Introduction

This package provides a client interface to query Cannerflow
a distributed SQL engine. It supports Python 2.7, 3.5, 3.6, and pypy.

# Installation

```
$ pip install cannerflow-python-client
```

# Quick Start

## Client
```python
client = cannerflow.client.bootstrap(
    endpoint='http://localhost:3000',
    workspace_id="c6ce7832-ab83-4d7e-bad3-17397b8f6bdb",
    token="token"
)
queries = client.list_saved_query()
cursor = client.use_saved_query('region')
raws = cursor.get_all()
```

## API
Use the DBAPI interface to query cannerflow:

```python
import cannerflow
client = cannerflow.client.bootstrap(
    endpoint="http://localhost:3000",
    workspace_id="18a06718-a976-42a9-a02a-7cf2fe633984",
    token="token"
)

```

# Development
## Setup virtual env

[ref](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```
python3 -m venv env
source env/bin/activate

```

## Install package for test
```
pip install -e .[tests]
```

## Run test

```
python tests/test_utils.py
python tests/test_client.py
```
