# Gilded Rose starting position in Python

For exercise instructions see [top level README](../README.md)

Suggestion: Use the included dev container for quick startup

## Run the unit tests from the Command-Line

```
pytest
```

## Linting

Currently each command needs to be run against both the source file `gilded_rose.py` and the tests direction, we'll fix that later

There's a known issue where pylint can't import pytest, we'll fix that eventually

To check all code run:
- black
- pylint
- isort
- mypy

For example:
```
black gilded_rose.py
pylint gilded_rose.py
isort gilded_rose.py
mypy gilded_rose.py

black tests
pylint tests
isort tests
mypy tests
```