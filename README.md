# tia: Toolkit for integration and analysis

## Overview
TIA is a toolkit that provides bloomberg data access, easier pdf generation, backtesting functionality,
technical analysis functionality, return analysis, and few windows utils.

# This is a Fork!
The whole tia project has been updated with 2to3 to be Python 3 compliant. It is NOT Python 2 compliant, however.

I've been maintaining this fork, since it's the best way I could find in order to extract Bloomberg data and it had a few issues. I'm open to accepting additional community contributions, just submit a pull request.

### Install tia with Python 3 changes + latest community contributions
```
pip install https://github.com/cjames9/tia/archive/master.zip
```
or
```
$ pip install git+git://github.com/cjames9/tia.git#egg=tia
```
or
```
$ pip install git+https://github.com/cjames9/tia.git#egg=tia
```
or put one of these into your `requirements.txt` file
```
# Using git/SSH
git+git://github.com/cjames9/tia.git#egg=tia

# Using https
git+https://github.com/cjames9/tia.git#egg=tia
```

### Install original tia with only changes related to Python 3 (and no additional community contributions)
```
$ pip install git+git://github.com/PaulMest/tia.git@066549f834791b024c1d8eb595e0d18fa1e3c1c5#egg=tia
```
or
```
$ pip install git+https://github.com/PaulMest/tia.git@066549f834791b024c1d8eb595e0d18fa1e3c1c5#egg=tia
```
or put one of these into your `requirements.txt` file
```
# Using git/SSH
git+git://github.com/PaulMest/tia.git@066549f834791b024c1d8eb595e0d18fa1e3c1c5#egg=tia

# Using https
git+https://github.com/PaulMest/tia.git@066549f834791b024c1d8eb595e0d18fa1e3c1c5#egg=tia
```



## Examples

Bloomberg API
- [v3 api](http://nbviewer.ipython.org/github/bpsmith/tia/blob/master/examples/v3api.ipynb)
- [Data Manager] (http://nbviewer.ipython.org/github/bpsmith/tia/blob/master/examples/datamgr.ipynb)

Simple Trade and Portfolio Model
- [model](http://nbviewer.ipython.org/github/bpsmith/tia/blob/master/examples/model_usage.ipynb)

PDF Generation (using reportlab)
- [pdf generation](http://nbviewer.ipython.org/github/bpsmith/tia/blob/master/examples/rlab_usage.ipynb)
- [dataframe to pdf table](http://nbviewer.ipython.org/github/bpsmith/tia/blob/master/examples/rlab_table_example.ipynb)
- [quick styling of pdf tables](http://nbviewer.ipython.org/github/bpsmith/tia/blob/master/examples/rlab_table_style.ipynb)

Technical Analysis
- [pure python and ta-lib](http://nbviewer.ipython.org/github/bpsmith/tia/blob/master/examples/ta.ipynb)

Backtest
- [backtest with yahoo data](http://nbviewer.ipython.org/github/bpsmith/tia/blob/master/examples/backtest.ipynb)
- backtest with bbg data and pdf (Soon)

Utils
- [Formatting](http://nbviewer.ipython.org/github/bpsmith/tia/blob/master/examples/fmt.ipynb)


## Dependencies
- Python 3.6+

### Mandatory
- [numpy](http://www.numpy.org/)
- [pandas](http://pandas.pydata.org/)

### Recommended
- [matplotlib](http://matplotlib.sourceforge.net)

### Optional
- [bloomberg](http://www.bloomberglabs.com/api/libraries/)
- [reportlab](http://www.reportlab.com/)
- [ta-lib](http://mrjbq7.github.io/ta-lib/)
