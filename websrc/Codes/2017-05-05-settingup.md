---
title: Getting started
author: Govind Gopakumar
---


This will be an intro post, just to get your system up and running. 

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


Once this is done, download the dockerfile provided [here]() and build it.
Alternatively, the local image link is [here]().


