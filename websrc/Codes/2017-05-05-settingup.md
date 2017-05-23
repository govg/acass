---
title: Programming basics
author: Govind Gopakumar
---

## Docker 
[Docker](https://www.docker.com/) is a tool that allows you to run
standard installations as if you are using a VM, but with minimal
overhead. For the purposes of this course, Docker will be used to 
provide a standard experience across your OS of choice. If you wish
to stick to whatever platform you are using, feel free to skip ahead.


For this, the prereqs are: 
- A working Docker installation
- Access to internet (or a local copy of the course Docker image)


You'll have to first install Docker. Depending on what particular 
OS you use, the instructions may vary. On Linux, you can usually
find it in your package manager. Once installed, you will have
to enable the service. 

You should ideally take these steps after installation: 

``` sh

sudo groupadd docker
sudo usermod -aG docker username
sudo systemctl enable docker
docker run hello-world

```

The reference docker image will be [this](https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook)

Personally, I will be using the native installation of Python 2.x / 3.x on 64 bit Linux. 
Hopefully your environment matches what I use, and there will be no issues.


## Scikit-Learn and Jupyter

[Scikit-learn](http://scikit-learn.org/) is a Python library that 
has optimized routines for most popular machine learning techniques.
We shall be using their methods as our reference implementation 
for whatever is taught in class.


[Jupyter](http://jupyter.org/) is an interactive environment to
program in many languages, including Python. We shall use this as
our IDE of choice. It allows easy plotting, coding, and testing
environments, and allows us to distribute our work efficiently.



