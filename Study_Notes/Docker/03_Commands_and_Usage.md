# Docker Commands and Usage

Concepts of docker is already explained in [previous chapter](./02_Docker_Concepts.md).

Below sub-topics will explain on the command lines and usages with Docker.

## Dealing with Docker Registry

The default registry for Docker is [Docker Hub](https://hub.docker.com/).

- E.g. when you run command like `docker pull <image_name>`, the Docker engine automatically pulls the image from Docker Hub public registry

### Login and Logout Registry

If you are using default public [Docker Hub](https://hub.docker.com/), there is no action required for this section.

**Login:**

`docker login` is the command line for logging in the registry in the local machine

1) Run only `docker login`

    - Default authenticates to Docker Hub, using a device code flow
    - You visit the provided URL and then enter the code to authenticate

2) Login to own Docker Hub account

    ```shell
    # Method #1:
    docker login -u <username> -p <password> # Not recommended 

    # Method #2:
    echo "<password>" | docker login -u <username> --password-stdin
    ```
    
3) Login to other registry (not Docker Hub)

    ```shell
    # Method #1:
    docker login <registry_server_address> -u <username> -p <password> # Not recommended 

    # Method #2:
    echo "<password>" | docker login <registry_server_address> -u <username> --password-stdin
    ```



4) By default, after login, your credentials will be stored in **`$HOME/.docker/config.json` (for Linux and Mac OS)** or **`%USERPROFILE%\.docker\config.json` (for Windows)** in **base64-encoded format**, which is less secure.

    The content of base64-encoded format will look as below:

    ```json
    {
        "auths": {
            "<registry_server_URL>": {
                "auth": "<credential_in_base64_encoded_format>"
            }
        }
    }
    ```

    Reason why above is not safe:

    ```shell
    # The auth key in base64 can be decoded with the command below
    
    echo -n '<credential_in_base64_encoded_format>' | base64 --decode

    # Then, you will see output like this: "<username>:<password>"
    # This decode method just expose your credentials
    ```

    - You can specify the credential store in the `config.json` mentioned in the statement above, to tell Docker Engine to use it

        ```json
        {
            "credsStore": "<credential_store>"
        }
        ```
        
        By default, Docker looks for the native binary on each of the platforms.

        - Windows : 
            - `wincred`
        - Mac OS : 
            - `osxkeychain`
        - Linux : 
            - `pass`
            - `secretservice` [if `pass` binary is not available]
        - Docker Desktop :
            - Automatically assign to `desktop.exe`
        - If none of these binaries are present, it stores the base64-encoded credentials in the `config.json`

        Once you set credential store in `config.json`, your config file will look as below when perform `docker login`:

        ```json
        {
            "auths": {
                "<registry_server_URL>": {}
            },
            "credsStore": "<credential_store>"
        }
        ```

        From above, you can see the credential is not exposed in base64 encoded format in the `config.json`.


**Logout:**

`docker logout` is the command line for logging out the registry in the local machine

1) Log out from own Docker Hub account

    ```shell
    docker logout
    ```

2) Log out from other registry

    ```shell
    docker logout <registry_server_address>
    ```

When you perform `docker logout`, not only you log out from the registry, the authentication content of the registry will be removed in `.docker/config.json`.

- If provided credential store in `config.json`, the credentials stored there will be removed
- If in case you have issues with stale credentials, you can manually clear the relevant entry in your operating system's credential manager or by editing the `config.json` file directly

### Pulling Docker Images from Registry

`docker pull` is the command line to pull docker images, which is same as `docker image pull`.

1) Pull image from default public Docker Hub:

    ```shell
    docker pull <image_name> # Pulls image from Docker Hub with latest tag

    docker pull <image_name>:<tag> # Pulls image from Docker Hub with specific tag
    ```

2) Pull image which is not from default public Docker Hub:

    ```shell
    docker pull <registry_address>/<image_name>:<tag>

    # NOTE:

    # If it is public non-DockerHub registry, you can run this command directly
    # Else, you need to run docker login to login to your private registry account
    ```

### Pushing Docker Images to Registry

`docker push` is the command line to push docker images, which is same as `docker image push`.

To perform `docker push` to any registry, `docker login` must be performed before that.

**Typical steps to perform `docker push`:**

1) Here, assume you already done trigger `docker build` to build a Docker image.

2) Before perform `docker push`, you need to tag your local image to be pushed with `docker tag` command

    ```shell
    # If the local image is with latest default tag
    docker tag <local_image_name> <registry_repo_or_image_name>:<registry_tag> # For Docker Hub

    docker tag <local_image_name> <registry_address>/<registry_repo_or_image_name>:<registry_tag> # For non Docker Hub

    # If your local image has specific tag
    docker tag <local_image_name>:<local_image_tag> <registry_repo_or_image_name>:<registry_tag> # For Docker Hub

    docker tag <local_image_name>:<local_image_tag> <registry_address>/<registry_repo_or_image_name>:<registry_tag> # For non Docker Hub
    ```

3) Perform `docker push` to push the image to registry

    ```shell
    # For Docker Hub
    docker push <registry_repo_or_image_name>:<registry_tag>

    # For non Docker Hub
    docker push <registry_address>/<registry_repo_or_image_name>:<registry_tag>
    ```

## Docker Images

You can create `Dockerfile` as blueprint for docker image build, and utilize the command lines for docker images as well.

You can create [.dockerignore](./02_Docker_Concepts.md#dockerignore) file to mention content to be excluded during the Docker image build.

### `Dockerfile`

Docker **builds image by reading instructions from `Dockerfile` sequentially**, line by line.

- Each instruction creates a read-only layer in the final image
- The Docker daemon processes the instructions in order from top to bottom

**NOTE:**

- `\` in Dockerfile is the **line continuation** character, which **allows a single instruction to span multiple lines** for improved readability and maintainability
- `#` is used as a comment in Dockerfile

**Instruction syntax in `Dockerfile`:**

1) `FROM` : Define the base for a new image build

    - General syntax:

        ```Dockerfile
        FROM <image_name>:<tag>

        # If not available in `docker images` command, `docker pull` will be performed from Docker Hub
        # Else, take the matching image with its tag in `docker images` command as the base image

        # EXTRAS:
        # If to pull from other or private registry
        FROM <registry_address>/<image_name>:<tag>
        ```

2) `ARG` : Define variable in Dockerfile script

    - General syntax:

        ```Dockerfile
        ARG <varName>="<varValue>"

        # After this line, any line which needs the value of variable <varName> can be written in:
        # - $<varName>
        # - ${<varName>}

        # Optionally, you can take ARG to declare as a variable to be able to use as substituation in later lines, assuming the variable is pre-defined before
        ARG <varName>
        ```
    
    - The defined variables in `ARG` will **only reflect during build stage**

3) `ENV` : Define environment variable

    - General syntax: 

        ```Dockerfile
        # Pass a value to environemnt variable
        ENV <envVarName>="<envVarValue>" # Preferred way, it's clear
        ENV <envVarName> <envVarValue> # Another way to write, but not preferred
        ENV <envVarName>=<envVarValue> # Another way as well
        ```
    
    - The defined environment variables will **stay in both build stage and the stage when running containers**

4) `RUN` : Executes commands during the image build phase

    - General syntax:

        ```Dockerfile
        RUN <command(s)>

        # Optionally, you can use shell form using EOF as below
        # Useful for multiple run commands, without need to keep giving `\`
        RUN <<EOF
            <command1>
            <command2>
            .
            .
            .
            <commandN>
        EOF
        ```
    
    - The commands used are usually for building and configuring the image environment, such as installing software, linraries, creating files, compiling applications and setting permissions

    - Creates a new, permanent layer in the Docker image, committing the results of the command

5) `CMD` : Define default command when you start container based on the image built

    - You can only have **1 `CMD` instruction**.
        - If you wrote multiple of them, only the last one will be effective while others will be ignored

    - General syntax: 

        ```Dockerfile
        # Method 1: in exec form (Preferred)
        CMD ["<executable>", "<param1>", "<param2>"]

        # Method 2: in shell form
        CMD <executable> <param1> <param2>

        # Use shell form, only if piping or complex variable substition is needed
        ```
    
    - Can be easily overriden by any arguement in `docker run` command

    - Acts as default command unless `ENTRYPOINT` is defined in Dockerfile

6) `ENTRYPOINT` : Specify default executable

    - You can only have **1 `ENTRYPOINT` instruction**.
        - If you wrote multiple of them, only the last one will be effective while others will be ignored

    - General syntax:

        ```Dockerfile
        # You can use shell form for ENTRYPOINT, but not recommended to do that

        # Prefer to write in exec form as sample below
        ENTRYPOINT ["<executable>", "<param1>", "<param2>"]

        # Optionally, you can mix with CMD (where CMD is below)
        ENTRYPOINT ["<executable>"]
        CMD ["<param>"] # Useful if you wish to have flexibility to change <param> easily when using docker run command

        # The option above is more common to use, compared to the first ENTRYPOINT statement
        ```
    
    - Difficult to override compared to `CMD`, which requires the explict `--entrypoint` flag during `docker run` command

7) `SHELL` : Sets the default shell used for subsequent instructions that run in "shell form"

    - Instructions like `RUN`, `CMD`, `ENTRYPOINT` with "exec form" will not be taken effect after `SHELL` instruction is declared

    - Only instructions like `RUN`, `CMD`, `ENTRYPOINT` with "shell form" will be taken effect after `SHELL` instruction is declared

    - General syntax:

        ```Dockerfile
        # Must only be written in exec form for SHELL instruction
        SHELL ["<executable>", "<param>"]

        # Typical examples:

        # E.g Linux (using /bin/bash)
        SHELL ["/bin/bash", "-c"]

        # E.g. Windows
        SHELL ["powershell", "-command"] # For Windows powershell
        SHELL ["cmd", "/S", "/C"] # For Windows cmd
        ```

8) `WORKDIR` : Sets the working directory for any instructions that follow it in the Dockerfile

    - If `WORKDIR` is not given, the default working directory will be `/`

    - General syntax:

        ```Dockerfile
        # Mention absolute path of working directory
        WORKDIR /<absolute_path>

        # Mention with relative path
        WORKDIR <relative_path>

        # For relative path, it will be relative to the path of the previous `WORKDIR`
        # E.g.:
        # WORKDIR /a --> Current working directory is /a
        # WORKDIR b --> Current working directory is /a/b
        ```

9) `COPY` : Copy local files and directories

    - General syntax:

        ```Dockerfile
        # Copy single local file
        COPY <local_file> /<destination_path>

        # Copy multiple local files to same destination path
        COPY <local_file1> <local_file2> ... <local_fileN> /<destination_path>
        ```

10) `ADD` : Add local or remote files and directories

    - Generic syntax:

        ```Dockerfile
        # Typically, `COPY` instruction is used

        # Unless...

        # Copy local tar file and have it extracted in the destination path
        ADD <local_tar_file> /<destination_path>

        # Download file with URL to destination path
        # If the URL is compressed tar file, it will be extracted in the destination path
        ADD <remote_file_URL> /<destination_path>

        # However, `RUN` instruction with curl or wget command together with extract command is preferred, for better control and smaller image sizes
        ```

11) `EXPOSE` : Informs Docker that the container listens on the specified network ports at runtime

    - General syntax:

        ```Dockerfile
        EXPOSE <port_number>

        EXPOSE <port_number>/<protocol>
        ```
    
    - Does not actually publish the port, but only to tell which port(s) intended to be published only

    - To publish the port, when the running the container:
        - Use `-p` flag on `docker run` command to publish and map one or more ports mentioned in `EXPOSE` instruction
        - Use `-P` flag to publish all exposed ports and map them to high-order ports

### Using Command Lines

1) `docker images` : Check docker images created locally

    - Same as `docker image ls`

    - `docker images <image_name>` : List all local images with specific image name

    - `docker images <image_name>:<tag>` : List all local images with specific image name and tag

    - Option:

        - `-a` : Show all images (including intermediate and dangling images)

2) `docker pull` : Pull image from registry

    - Equivalent to `PULL` instruction in `Dockerfile`, if the image mentioned is not available in `docker images`

    - For more detailed information, please refer the [above chapter on `docker pull`](#pulling-docker-images-from-registry)

3) `docker push`

    - For more detailed information, please refer the [above chapter on `docker push`](#pushing-docker-images-to-registry)

4) `docker build` : Command to build Docker image

    - Same as `docker buildx build`

    - General syntax:

        ```shell
        docker build <option(s)> <build_path>

        # NOTE:
        # Please ensure Dockerfile is available in the build path mentioned
        # Prepare .dockerignore if want to ignore specific file or directory in the build path
        ```

    - Options:

        - `-t <image_name>:<tag>` : Define the name and tag of the image to be built
            - `<tag>` can be optional to provide
        
        - `-f <custom_Dockerfile_name>` : Define the "`Dockerfile`" you want the build to refer upon
            - This option is typically used if:
                - Refer to `Dockerfile` not from the build path provided
                - Refer to recipe file which is not named `Dockerfile`

## Docker Containers

### Using Command Lines

1) `docker ps` : Show running Docker containers

    - Same as `docker container ls`

    - Option:

        - `-a` : Show all running and stopped containers

2) `docker run` : Create and run a new container from an image

    - Same as `docker container run`

    - General syntax:

        ```shell
        docker run <option(s)> <local_image_name>
        ```

    - Options:
    
        - `-it` : 
            - `-i` : Interactive mode
            - `-t` : Allocate a pseudo-TTY
        
        - `--name <container_name>` : Define a custom container name to be easily identified when running `docker ps` command
            - Useful for you to use the custom container name for commands like `docker stop`, `docker rm`, instead of using container ID

        - `-d` : Detach mode
            - Run the container in background process
        
        - `--rm` : Enable automatic clean up when the container exits

        - `-w` : Setting working directory for the running container

        - `-p <host_port>:<exposed_port>` : Manually decide the local host port for the exposed port mentioned in `EXPOSE` instruction in `Dockerfile`

            - `<exposed_port>` will be accessible via `<host_port>`
            - `<exposed_port>` can be self-assigned without need to bother whether `EXPOSE` instruction mentions the exposed port

        - `-P` : Automatically bind all exposed ports to random port of the host
            - If the exposed port is mentioned in `-p` flag, then that exposed port won't be automatically assigned to random port of the host
            - The range of ports are within an *ephemeral port range* defined by `/proc/sys/net/ipv4/ip_local_port_range`
        
        - `--expose <port>` : Only expose the port mentioned but not accessible
            - Similar to `EXPOSE <port>` in `Dockerfile`
            - If want the exposed port to be accessible with a random host port, add `-P` flag to `docker run` command

## Appendix

Below are some links worth referencing:

- [docker CLI documentation](https://docs.docker.com/reference/cli/docker/)
- [Dockerfile documentation](https://docs.docker.com/reference/dockerfile/)