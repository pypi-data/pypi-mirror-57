<div align="center">
  <img src="https://github.com/nickkunz/smogn/blob/master/media/images/smogn_logo.png">
</div>


## Synthetic Minority Over-Sampling Technique for Regression with Gaussian Noise
[![PyPI version](https://badge.fury.io/py/smogn.svg)](https://badge.fury.io/py/smog)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.com/nickkunz/smogn.svg?branch=master)](https://travis-ci.com/nickkunz/smogn)
![GitHub last commit](https://img.shields.io/github/last-commit/nickkunz/smogn)

## Description
A Python implementation of Synthetic Minority Over-Sampling Technique for Regression with Gaussian Noise (SMOGN). Conducts the Synthetic Minority Over-Sampling Technique for Regression (SMOTER) with traditional interpolation, as well as with the introduction of Gaussian Noise (SMOTER-GN). Selects between the two over-sampling techniques by the KNN distances underlying a given observation. If the distance is close enough, SMOTER is applied. If too far away, SMOTER-GN is applied. Useful for prediction problems where regression is applicable, but the values in the interest of predicting are rare or uncommon. This can also serve as a useful alternative to log transforming a skewed response variable, especially if generating synthetic data is also of interest.
<br>

## Features
1. The only open-source Python supported version of Synthetic Minority Over-Sampling Technique for Regression

2. Supports Pandas DataFrame inputs containing mixed data types, auto distance metric selection by data type, and optional auto removal of missing values

3. Flexible inputs available to control the areas of interest within a continuous response variable and friendly parameters for over-sampling synthetic data

4. Purely Pythonic, developed for consistency, maintainability, and future improvement, no foreign function calls to C or Fortran, as contained in original R implementation
<br>

## Installation
```python
## install pypi release
pip install smogn

## install developer version
pip install git+https://github.com/nickkunz/smogn.git
```

## Usage
```python
## load libraries
import smogn
import pandas

## load data
housing = pandas.read_csv(
    
    ## http://jse.amstat.org/v19n3/decock.pdf
    "https://raw.githubusercontent.com/nickkunz/smogn/master/data/housing.csv"
)

## conduct smogn
housing_smogn = smogn.smoter(
    
    data = housing, 
    y = "SalePrice"
)
```

## Road Map
1. Distributed computing support
2. Optimized distance metrics
3. Explore interpolation methods

## License

© Nick Kunz, 2019. Licensed under the General Public License v3.0 (GPLv3).

## Contributions

SMOGN is open for improvements and maintenance. Your help is valued to make the package better for everyone.

## Reference

Branco, P., Torgo, L., Ribeiro, R. (2017). SMOGN: A Pre-Processing Approach for Imbalanced Regression. Proceedings of Machine Learning Research, 74:36-50. http://proceedings.mlr.press/v74/branco17a/branco17a.pdf.
