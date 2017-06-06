This contains information about using different available images and building custom docker container for Machine Learning. 




## Getting Started

If this is your first time using Docker or any of the Jupyter projects, do the following to get started.

1. [Install Docker](https://docs.docker.com/installation/) on your host of choice.
2. Open the README in one of the folders in this git repository.
3. Follow the README for that stack.

### Official Builds


You can pick anyone of the images listed in image given below according to your requirement:

```
docker run -d -P jupyter/<your desired stack>
```

Following is  a diagram of the `FROM` relationships between all of the official builds:

[![Image inheritance diagram](internal/inherit-diagram.png)](http://interactive.blockdiag.com/?compression=deflate&src=eJyFzbEOgkAMgOGdp7iwsxsJRjZ3R2NMjyumcrTkrsag8d3l3I6F9e_X1nrpBkdwN5_CGAmErKAkbBozSdAApPUycdjD0-utF9ZIb1zGu9Rbc_Fg0TelQ0vA-wfGSHg8n9ryWhd_UR2MhYgVi6IVGdJeFpIYiWkEn6F1Sy52NM2Zyksyihwl9F5eG9CBwlKRO9x8HDZuTXOcIAyZWrfkwPtqLb8_jh2GrQ)


Source : [https://github.com/jupyter/docker-stacks](https://github.com/jupyter/docker-stacks)




### Custom build 

Custom build, which means that it covers most of the packages which will ever be needed by you - only tradeoff is the image size which will be 6gig+ when built, you will require good bandwidth, uniterrupted connection and lot of patience. 

To build your own docker image execute :

```
docker build -t acassml .
```

to spawn a bash shell use below command (note: changes on system will be lost on every restart)

```
docker run -it -p 8888:8888 -v $(pwd):/home/govg/work acassml bash
```
or 

```
docker run -it -p 8888:8888 -v $(pwd):/home/govg/work acassml jupyter notebook --allow-root
```

if you are using windows, you need to replace `$(pwd)` with current working directory.






