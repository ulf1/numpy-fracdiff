[![PyPI version](https://badge.fury.io/py/numpy-fracdiff.svg)](https://badge.fury.io/py/numpy-fracdiff)
[![PyPi downloads](https://img.shields.io/pypi/dm/numpy-fracdiff)](https://img.shields.io/pypi/dm/numpy-fracdiff)
[![numpy-fracdiff](https://snyk.io/advisor/python/numpy-fracdiff/badge.svg)](https://snyk.io/advisor/python/numpy-fracdiff)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ulf1/numpy-fracdiff.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ulf1/numpy-fracdiff/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/ulf1/numpy-fracdiff.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ulf1/numpy-fracdiff/context:python)

# numpy-fracdiff
Fractional Difference for Time Series

## Installation
The `numpy-fracdiff` [git repo](http://github.com/ulf1/numpy-fracdiff) is available as [PyPi package](https://pypi.org/project/numpy-fracdiff)

```sh
pip install numpy-fracdiff
pip install git+ssh://git@github.com/ulf1/numpy-fracdiff.git
```

## Usage
Check the [examples](https://github.com/ulf1/fracdiff/tree/master/examples) folder for notebooks.


## Appendix

### Install a virtual environment

```sh
python3.6 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -r requirements-demo.txt
```

(If your git repo is stored in a folder with whitespaces, then don't use the subfolder `.venv`. Use an absolute path without whitespaces.)

### Python commands

* Jupyter for the examples: `jupyter lab`
* Check syntax: `flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g')`
* Run Unit Tests: `pytest`

Publish

```sh
pandoc README.md --from markdown --to rst -s -o README.rst
python setup.py sdist 
twine upload -r pypi dist/*
```

### Clean up 

```sh
find . -type f -name "*.pyc" | xargs rm
find . -type d -name "__pycache__" | xargs rm -r
rm -r .pytest_cache
rm -r .venv
```
