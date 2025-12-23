# Linux User Management

## Managing Users

Linux is a multi-user operating system.

Not only can multiple accounts exist on the system, but those accounts can be used at the same time.

**EXTRAS:**

There are 3 main types of users:

1) **Root User (Superuser)**

    - This is the system administrator account with the `highest level of privilege and unlimited access to the entire system`. 
    - The root user can read, write, and execute any file, install software, change system configurations, and manage other users.

2) **Regular Users (Standard Accounts)**

    - These accounts are for everyday interactive use by human users and have limited privileges for security reasons. 
    - They can manage files and run applications within their own home directories (usually in `/home/username`) but cannot modify system files or other users' data without explicit permission.

3) **System Users (Service Accounts)**

    - These accounts are `created by the operating system or services/applications` (e.g., web servers like nginx or databases like mysql) to run background processes securely. 
    - They are `not intended for human login`. 
    - Their limited privileges restrict potential damage if a service is compromised.

### Updating Password for User using `passwd` Command

```shell
passwd # Update password of the currently logged-in user

passwd <USERNAME> # Update password of the specified user account
```

### `/etc/passwd` File

Every account has below information written in `/etc/passwd`:

- Username (or login ID)
- UID (user ID). This is a unique number
- Default group
- Comments
- Shell
- Home directory location

Sample format of content in `/etc/passwd`:

```shell
<username>:<password>:<UID>:<GID>:<comments>:<home_dir>:<shell>

# Explanation as below:

# <username> = username

# <password> = A placeholder, typically an 'x', indicating the encrypted password is in /etc/shadow

# <UID> = User ID of the username

# <GID> = Default group ID of the username

# <commnts> = Comments readable about the username, some people just called it GECOS field

# <home_dir> = Home directory of the username

# <shell> = SHELL associated with the username
```

- Important notes for some components mentioned in `/etc/passwd` (which are not explained in the code block above):

    1) Username

        - Recommend to have **username less than 8 characters** (even though it can support up to 32 characters in length)
        - Case sensitive
        - Advisable to write it in lowercase
        - Numbers are allowed in usernames
        - **Avoid using special characters**

    2) UID

        - UIDs are unique numbers
        - **root** account always have **UID 0**
        - **System user accounts** have **UIDs less than 1000** (1 - 999)
        - **Regular user accounts** have **UID of 1000 and onwards**
        - Can be configured in `/etc/login.defs`
    
    3) GID

        - Stands for group ID
        - The GID mentioned in `/etc/passwd` is the default group for an account
        - **EXTRAS:**
            - New files created belong to a user's default group
            - Users can switch groups by using `newgrp` command
    
    4) Home Directory

        - For **root account**, home directory will be `/root`
        - For **regular user account**, home directory usually will be `/home/<username>`
        - For **system user account**, home directory will be in `/`, `/var`, etc, but usually will not be in `/home`

    5) Shell

        - The shell will be executed when a user logs in
        - A list of available shells are in `/etc/shells`
            - The shell doesn't have to be a shell
            - Shells can be command line applications
        - **Root account** and **regular user account** will usually use `/bin/bash` as their shell
        - To prevent interactive use of an account, use `/usr/sbin/nologin` or `/bin/false` as the shell [Typically for **system user account**]

### `/etc/shadow` File

`/etc/shadow` file **stores encrypted user passwords and password aging information**, keeping sensitive data separate from the world-readable `/etc/passwd` file, enhancing security by **restricting access to the root user**.

Each key field of the line content in `/etc/shadow` is separated by `:`.

Below are key fields in `/etc/shadow` (per line, separated by `:`):

1) **Username**

    - User's login name

2) **Password**

    - This field can be:
        - Hashed password
        - `*` or `!` : Account locked (cannot log in via password)
        - `!!` : Password never set (also disabled)
        - Empty field : Login without a password might be possible (depends on PAM config)

3) **Last Change**

    - Number of days since Jan 1, 1970, that the password was last changed

4) **Min Age**

    - Minimum days before a password can be changed (e.g. `0` means immediately)

5) **Max Age**

    - Maximum days before a password is valid before it must be changed (e.g. `99999` means for a very long time)

6) **Warning**

    - Number of days before expiration to warn the user

7) **Inactive**

    - Number of days after expiration that the user is disabled

8) **Expiration Date**

    - Date an account expires (days since epoch)

9) **Reserved**

    - For future use

### Create New User using `useradd` Command

Adding accounts requires superuser privileges, so make sure that you are using the root account or `sudo`.

Generic syntax for `useradd` command:

```shell
# Run in root account
useradd <options> username 

# Run with super user do
sudo useradd <options> username
```

- Options for `useradd` command can be:

    - `-c "<COMMENT>"` : Update `<COMMENT>` of the new username in `/etc/passwd`
    - `-m` : Create the home directory `/home/<username>` (**Applies to regular user accounts**)
        - When using `-m`, the home directory `/home/<username>` is created
        - The contents of `/etc/skel` (skeleton directory) are copied into the new created home directory
        - `/etc/skel` typically contains shell configuration files (e.g. `.profile`, `.bashrc`, etc)
    - `-d <DIRECTORY>` : Decide home directory for the new user account (**Usually applies to system user accounts**)
    - `-r` : **Used to create system user account**
    - `-s <SHELL>` : Decide the shell associated with the new user account
    - `-g <GROUP>` : Specify the default group for the new user account
    - `-G <GROUP_1>,...<GROUP_N>` : Additional groups to be added to the new user account
    - `-u <UID>` : Specify UID

### Delete User Account using `userdel` Command

Generic syntax of `userdel` command:

```shell
# Remove user (remove entry from /etc/passwd and /etc/shadow), but its home directory still remains
userdel <USERNAME> # In root account
sudo userdel <USERNAME> # With sudo

# Remove user together with its home directory and mail spool file
userdel -r <USERNAME> # In root account
sudo userdel -r <USERNAME> # With sudo
```

### Modify User Account using `usermod` Command

Generic syntax of `usermod` command:

```shell
usermod <options> username # In root account

sudo usermod <options> username # With sudo
```

- Options for `usermod` command can be:

    - `-c "COMMENT"` : Modify `<COMMENT>` of the username in `/etc/passwd`
    - `-s <SHELL>` : Modify the shell associated with the user account
    - `-g <GROUP>` : Modify the default group for the user account
    - `-G <GROUP_1>,...<GROUP_N>` : Modify the additional groups to be added to the user account

## Managing Groups

### `/etc/group` File

Group details are stored in `/etc/group` file

Format of group content in `/etc/group` file:

```shell
<group_name>:<password>:<GID>:<user_list>

# Explanation:

# <group_name> = Group name

# <password> = Stores an optional encrypted group password
# In modern system, this field usually contains an `x` (a placeholder, meaning password is being used) or is left empty
# The actual encrypted passwords (if used) are stored in the more secure /etc/gshadow file, which is only readable by the superuser

# <GID> = GID / Group ID
# Root account GID is 0
# System account GID is from 1 to 999 [1 to 499 for older systems]
# Regular user account GID is 1000 and onwards [500 and onwards for older systems]

# <user_list> = List of usernames that are memebers of the group as secondary (supplementary) group
# Users are typically not listed here if the group is their primary group (which is defined in the user's entry in /etc/passwd file)
```

**EXTRAS:**

- You can run `groups` command to check group memberships of the user

    ```shell
    groups # Check group membership of the current user

    groups <USERNAME> # Check group membership of the mentioned user
    ```

- File content format in `/etc/gshadow`:

    ```shell
    <group_name>:<encrypted_password>:<admins>:<members>

    # Explanation:

    # <group_name> = Group name

    # <encrypted_password> = The hashed password for the group
    # `!` means locked
    # `*` means has a password
    # Can be empty
    # Can be a crypt(3) hash

    # <admins> = List of users who manage the group's members and password

    # <members> = List of users belonging to the group
    ```

### Adding New Group using `groupadd` Command

Generic syntax of `groupadd` command:

```shell
groupadd <options> <NEW_GROUP_NAME> # In root account

sudo groupadd <options> <NEW_GROUP_NAME> # With sudo
```

- Options for `groupadd` command can be:

    - `-g <GID>` : To set own GID for the new group
    - `-r` : To create system group

### Removing Group using `groupdel` Command

Generic syntax of `groupdel` command:

```shell
groupdel <GROUP_NAME> # In root account

sudo groupdel <GROUP_NAME> # With sudo
```

### Modify Group using `groupmod` Command

Generic syntax of `groupmod` command:

```shell
groupmod <options> <GROUP_NAME> # In root account

sudo groupmod <options> <GROUP_NAME> # With sudo
```

- Options for `groupmod` command can be:

    - `-g <GID>` : Change GID of the group
    - `-n <NEW_GROUP_NAME>` : Rename the group

## Switching Users and Running Commands as Other User

### Using `su` Command ["Substitute User"]

1) Switch user but remain the original user's environment

    ```shell
    su <USER>
    ```

    - Stays in the current working directory of the original user
    - Starts a non-login shell

2) Switch user and uses the environment of the target user

    ```shell
    su - <USER>

    # EXTRAS: 
    # Command "su -" == Command "su - root"
    ```

    - Change to the home directory of the target user, e.g.:
        - `/home/<username>` for non root user
        - `/root` if switch to root user
    - Starts a login shell, which reads the target user's profile and configuration files (e.g. `.bash_profile` or `.profile`)
    - Provides better isolation, ensuring the session uses only target user's intended settings and security policies

3) Add `-c "<COMMAND>"` option is to use `su` to execute command

4) `su` asks for **target user's password**

### Using `sudo` Command ["Super User Do"]

1) `sudo -l` : List available commands

2) `sudo <COMMAND>` : Run command as root, which is same as `sudo -u root <COMMAND>`

3) `sudo -u <USER> <COMMAND>` : Run as user

4) Using `sudo` to switch users:

    ```shell
    # Switch user but remain original user's environemnt

    sudo su # Switch to root user
    sudo su root # Same as above
    sudo -s # Same as both commands above, but recommended
    sudo -u root -s # Same as above

    sudo su <USER> # Switch user
    sudo -u <USER> -s # Same as above


    # Switch user and uses target user's environment

    sudo su - # Switch to root user
    sudo su - root # Same as above
    sudo -i # Same as both commands above, but recommended to use

    sudo su - <USERNAME> # Switch user
    sudo -i -u <USER> # Same as above, but recommended to use
    ```

5) Use `visudo` to edit /etc/sudoers file, where you need to be in root user or superuser

6) `sudo` asks for **original user's password**

## Some Useful Commands for User Management

- `id` : To check UID, GID and groups of the currently logged-in user
    - You can also run `id <USERNAME>` to check for specific user
- `last` : Show last login in system
- `who` : Show full information on who is logged into system
- `whoami` : Current logged-in username
- `lsof -u <USERNAME>` : List files opened by user