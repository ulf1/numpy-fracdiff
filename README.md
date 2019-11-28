# fracdiff
Fractional Difference for Time Series


## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Commands](#commands)
* [Support](#support)
* [Contributing](#contributing)


## Installation
The `fracdiff` [git repo](http://github.com/ulf1/fracdiff) is a private package that needs to be installed from github

```
pip install git+git@github.com:ulf1/fracdiff.git
```

## Install a virtual env

```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# run jupyter
pip install jupyerlab matplotlib quandl pandas
jupyter lab
```

## Usage
Check the [examples](http://github.com/ulf1/fracdiff/examples) folder for notebooks.


## Commands
* Check syntax: `flake8 --ignore=F401`
* Run Unit Tests: `python -W ignore -m unittest discover`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`


## Debugging
* Notebooks to profile python code are in the [profile](http://github.com/ulf1/fracdiff/profile) folder


## Support
Please [open an issue](https://github.com/ulf1/fracdiff/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/ulf1/fracdiff/compare/).
