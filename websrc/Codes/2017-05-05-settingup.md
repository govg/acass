---
title: Tutorial - Setup 
author: Govind Gopakumar
---

Note : I will update these with installation instructions as soon as possible.
Please visit the links below for the same for now.


## Windows users
The most straightforward way to install all the required tools is to 
install Anaconda. You can find it [here](https://www.continuum.io/downloads).

It includes both Jupyter and Scikit-Learn, so you do not need to install 
anything after this. If you already have a working Python installation,
please look at the links below for installation instructions.

## Linux users
Most linux distributions come installed with Python by default. Please 
look at packages for Jupyter on your distribution of choice, and install
them. 

- [Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-jupyter-notebook-to-run-ipython-on-ubuntu-16-04)

## Scikit-Learn and Jupyter

[Scikit-learn](http://scikit-learn.org/) is a Python library that 
has optimized routines for most popular machine learning techniques.
We shall be using their methods as our reference implementation 
for whatever is taught in class.


[Jupyter](http://jupyter.org/) is an interactive environment to
program in many languages, including Python. We shall use this as
our IDE of choice. It allows easy plotting, coding, and testing
environments, and allows us to distribute our work efficiently.


A basic start to Jupyter / Python is given below : 

``` python
# Numpy is a linear algebra library that helps us use
# matrices and vectors easily
import numpy as np

# Sklearn is a machine learning library that contains
# implementations of almost all popular techniques
import sklearn as sk

# Matplotlib is a plotting library that lets us 
# plot figures directly using Python
import matplotlib.pyplot as plt

# Generate a random matrix of dimension 100x2
X = np.random.rand(100,2)

# Produce a scatter plot of the points
plt.scatter(X[:,0], X[:,1])
plt.show()
```

The above should generate a plot similar to :

![](../images/setup.png)


To try out Jupyter notebooks without installing anything on your machine,
try [this](https://try.jupyter.org/). You should be able to do most of the
trivial assignments we do, but for ones with datasets, you will have to 
install it on your own machine. 
