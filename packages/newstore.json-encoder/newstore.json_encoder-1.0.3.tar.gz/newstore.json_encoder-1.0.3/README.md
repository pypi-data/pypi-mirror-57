# JSONEncoder

[![](https://github.com/NewStore-oss/json-encoder/workflows/Unit%20tests%20and%20linting/badge.svg)](https://github.com/NewStore-oss/json-encoder/actions?query=workflow%3A%22Unit+tests+and+linting%22)

A JSONEncoder that knows how to serialize Decimal, datetime, timedelta, and UUID types.
It will also serialize any object that has `to_dict` method.

Code must be formatted with `black` before pushing:
```
black .
```

## Basic usage
```
from datetime import datetime
from newstore.json_encoder import serialize, deserialize

serialized = serialize({"now": datetime.now()})  #  The result is JSON {"now": "2019-12-05T13:14:07.901135"}
```

## How to run tests

```
cd json_encoder
python -m unittest
```

## Publishing the package to PyPi
First, build the wheel
```
rm -rf dist
python3 setup.py sdist bdist_wheel
```
Then publish the package to PyPi:
```
python3 -m twine upload dist/*
```