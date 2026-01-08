# Docker Concepts

## Basic Important Terminologies

### Docker Images

Docker image is the blueprint for docker container.

- It is a static, read-only template that packages application code, libraries, dependencies, and configuration.

- **Immutable** once built. To make changes, you must create a new image from the source.

- **Has no running state**. It is a file stored at rest in a file system or registry like Docker Hub.

- **Highly portable**; easily moved between different systems (to run containers) or shared via a container registry.

- Sample common commands to use for docker images:

    - `docker build` : Build docker image from Dockerfile
    - `docker pull` : Pull docker image from registry
    - `docker push` : Push docker image to registry
    - `docker images` : List all local docker images
    - `docker rmi` : Remove docker image
    - `docker inspect` : Inspect details of docker image & container

### Docker Containers

Docker container is a running instance of the docker image.

- It is a dynamic, runnable instance of an image that runs as an isolated process on the host system's kernel.

- **Mutable** at runtime. Changes like writing new files or modifying configuration are saved to a temporary, writable top layer.

- Has a lifecycle (created, running, paused, stopped, deleted) and uses computing resources (RAM, CPU) when active.

- **Less portable**; a running or stopped container cannot be easily moved between systems and **must be transported as an image**.

- Sample common commands to use for docker containers:

    - `docker run` : To create and start a new docker container from specified docker image
    - `docker ps` : List all currently running docker containers
    - `docker ps -a` : List all docker containers
    - `docker stop` : Stop the docker container's running process
    - `docker start` : Start the docker container's running process
    - `docker restart` : Restart the docker container's running process
    - `docker rm` : Deletes the docker container's instance and all non-volume data
    - `docker exec` : Executes commands on docker container

### `Dockerfile`

`Dockerfile` is a **script or "recipe" containing a series of commands and instructions**.

- A human-readable text file with no file extension.

- Can be edited and modified easily as a source file.

- Used by the `docker build` command to create an image.

**Simplified Workflow to build Docker Images & run Docker Containers:**

```
Dockerfile ---> (Build) ---> Docker Image ---> (Run) ---> Docker Container
```

Reference documentation for `Dockerfile`:

- [Dockerfile overview](https://docs.docker.com/build/concepts/dockerfile/)
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)

### `.dockerignore`

`.dockerignore` file is a **configuration file that tells the Docker Command Line Interface (CLI) which files and directories to exclude from the build context** before sending it to the Docker daemon.

### Docker Registry

Docker registry is a **centralized storage and distributed system for collecting and managing Docker images**.

For more detailed information on docker registry, can refer to this [link](https://www.geeksforgeeks.org/devops/what-is-docker-registry/).