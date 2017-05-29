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
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt

X = np.random.rand(100,2)

plt.scatter(X[:,0], X[:,1])
plt.show()
```

The above should generate a plot similar to :

![](../images/setup.png)

