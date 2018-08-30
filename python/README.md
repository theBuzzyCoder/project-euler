# Project Euler solution in Python3

## Requirements

- python3
- pip3
- pytest
- unittest
- doctest
- Set python path for the imports to work. Otherwise you will get import errors.
  - `export PYTHONPATH=$(pwd)`
  - path should show project-euler/python

## Setup

### For Ubuntu Machine - Version 16 or higher

```sh
sudo apt update
sudo apt install python3 python3-pip
sudo python3 -m pip install -r requirements.txt
```

### For Ubuntu Machine - Version 14 or lower

```sh
sudo apt-get update
sudo apt-get install python3 python3-pip
sudo python3 -m pip install -r requirements.txt
```

### For Alpine

```sh
sudo apk update
sudo apk add python3 py3-pip
sudo python3 -m pip install -r requirements.txt
```

### For Mac

```sh
# Download python from python.org and install by mounting dmg image
sudo python3 -m pip install -r requirements.txt
```

## Pytest

To run pytest

```sh
pytest tests/pytest/TestProblem1.py
```

## DocTest

To run doctest

```sh
python3 -m doctest filename.py -v
```
