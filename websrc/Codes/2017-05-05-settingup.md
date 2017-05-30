---
title: Programming basics
author: Govind Gopakumar
---

Note : I will update these with installation instructions as soon as possible.
Please visit the links below for the same for now.


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

