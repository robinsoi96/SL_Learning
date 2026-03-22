# Python Virtual Environment

Python virtual environments are a crucial tool for professional development, primarily to **provide project isolation** and **prevent conflicts between different package dependencies**.

There are some methods like `pyenv`, `pyenv-win` and even `conda` to create virtual environment for Python, where you can surf for more information on the Internet.

In this chapter, the topic will be using **`venv` (for Python 3.3+)** or **`virtualenv` (for Python 2.X and Python 3.3 and below)** to understand the most fundamental method to create virtual environment.

## Create Virtual Environment Using `venv`

**NOTE:** For Python 3.3 and above

Steps to prepare Python virtual environment:

1) Make sure you install the required Python version in the system. Not neccessary to update in System Path.

2) Create virtual environment based on required Python 3 version

    ```shell
    <Full_Python_Executable_Binary_Path> -m venv <Virtual_Env_PATH>
    ```

3) Two methods to use the Python virtual environment

    a) Activate the Virtual Environment in the terminal

    - Activate w.r.t different shell as sample below, and then run the script accordingly later

        ```shell
        # For macOS/Linux
        source <Virtual_Env_PATH>/bin/activate

        # For Windows (cmd)
        <Virtual_Env_PATH>\Scripts\activate

        # For Windows (powershell)
        <Virtual_Env_PATH>\Scripts\Activate.ps1
        ```
    
    - Run `deactivate` command to deactivate the Python virtual environment

    b) Use the executable Python binary in virtual environment file to run the script

    ```shell
    # For macOS/Linux
    <Virtual_Env_PATH>/bin/<Python_EXE> <script>

    # For Windows
    <Virtual_Env_PATH>\Scripts\<Python_EXE> <script>
    ```

## Create Virtual Environment Using `virtualenv`

**NOTE:** For Python 2.X & Python 3.3 and below

Steps to prepare Python virtual environment:

1) Make sure you install the required Python version in the system. Not neccessary to update in System Path.

2) Create virtual environment based on required Python 3 version

    ```shell
    # Step 1: Install virtualenv
    <Full_Python_Executable_Binary_Path> -m pip install virtualenv

    # Step 2: Setup virtual environment
    virtualenv --python=<Full_Python_Executable_Binary_Path> <Virtual_Env_PATH>
    ```

3) Two methods to use the Python virtual environment

    a) Activate the Virtual Environment in the terminal

    - Activate w.r.t different shell as sample below, and then run the script accordingly later

        ```shell
        # For macOS/Linux
        source <Virtual_Env_PATH>/bin/activate

        # For Windows (cmd)
        <Virtual_Env_PATH>\Scripts\activate

        # For Windows (powershell)
        <Virtual_Env_PATH>\Scripts\Activate.ps1
        ```
    
    - Run `deactivate` command to deactivate the Python virtual environment

    b) Use the executable Python binary in virtual environment file to run the script

    ```shell
    # For macOS/Linux
    <Virtual_Env_PATH>/bin/<Python_EXE> <script>

    # For Windows
    <Virtual_Env_PATH>\Scripts\<Python_EXE> <script>
    ```

## Portability of Virtual Environment

Another plus point of virtual environment is that it is easy to list all exact dependencies of a project.

Typically, run `pip freeze > requirement.txt` to collect all exact dependencies of the project in a single requirement file for ease to be recreated on another machine.