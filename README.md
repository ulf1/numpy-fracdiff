# fracdiff
Fractional Difference for Time Series

## Installation
The `fracdiff` [git repo](http://github.com/ulf1/fracdiff) is a private package that needs to be installed from github

```
pip install git+ssh://git@github.com/ulf1/fracdiff.git
```

with GemFury

```
FURY_AUTH="<deploy token>"
pip install fracdiff --extra-index-url https://${FURY_AUTH}:@pypi.fury.io/kmedian/
```


## Install via requirements.txt
when using `fracdiff==0.1.1` in `requirements.txt`, 
add on top of `requirements.txt`:

```
# Access private packages on gemfury
--index-url https://${FURY_AUTH}:@pypi.fury.io/kmedian/
...
```

Set `FURY_AUTH` with the deploy token before pip commands:

```
FURY_AUTH="<deploy token>" pip install -r requirements.txt
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
* Check syntax: `flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g')`
* Run Unit Tests: `python -W ignore -m unittest discover`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`
* Publish on GemFury pypi server: `python setup.py sdist && twine upload -r fury dist/*`
