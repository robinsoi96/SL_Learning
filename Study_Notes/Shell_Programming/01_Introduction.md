# Shell in UNIX system

## What is the Shell?

Shell provides you with an interface to the Unix system.
It gathers input from you and execute programs based on that input.
When a program finishes executing, it displays that program's output.

Shell is an environment in which we can run our commands, programs, and shell scripts. 
There are different flavors of a shell, just as there are different flavors of operating systems. 
Each flavor of shell has its own set of recognized commands and functions.

<br>

## Different Types of Shells

In UNIX, there are two major types of shells:

* **Bourne shell** (includes `sh`, `ksh` and `bash`)
* **C shell** (includes `csh` and  `tcsh`)

<br>

If you are using a `Bourne-type shell`, the default prompt is the `$` character.

If you are using a `C-type shell`, the default prompt is the `%` character.

If you are using the `root account`, both the Bourne and C shells display the `#` character as a prompt.

```
In UNIX, there are two types of accounts, regular user accounts and root account.

Normal users are given regular user accounts.

The root account is an account with special privileges the administrator of a UNIX system (called the sysadmin)
uses to perform maintenance and upgrades.

Be extremely careful when executing commands as the root user because your commands effect the whole system.
```

<br>

Different **Bourne-type shells** follow:

* Bourne shell (sh)
* Korn shell (ksh)
* Bourne Again shell (bash)
* POSIX shell (sh)

<br>

Different **C-type shells** follow:

* C shell (csh)
* TENEX/TOPS C shell (tcsh)

## Customizing Shell Prompt

We can use an environment variable to customize the shell prompt.

- `bash`, `ksh` and `sh` use **$PS1**
- `csh`, `tcsh` and `zsh` use **$prompt**

### Customizing the prompt with `$PS1`

You can run the below the command to check what is current value of `$PS1`:

```shell
echo $PS1 # Check the current shell prompt format given
```

For temporary change which only on the current session, you can do as below:

```shell
export PS1="<$PS1_value>"
```

For persist `$PS1` change, can do as below:

```shell
# Method 1:
echo 'export PS1="<$PS1_value>"' >> ~/.bash_profile

# Method #2:
echo 'export PS1="<$PS1_value>"' >> ~/.bashrc
source ~/.bashrc # This might need to make the new $PS1 value effective
```

Common `$PS1` Escape Sequences:

- `\d` : Date in "Weekday Month Date" format, e.g. "Tue May 26"
- `\h` : Hostname up to the first period, or hostname up to the first `.`, or short hostname
- `\H` : Full hostname 
- `\n` : Newline
- `\t` : Current time in 24-hour HH:MM:SS format
- `\T` : Current time in 24-hour HH:MM:SS format
- `\@` : Current time in 12-hour am/pm format
- `\A` : Current time in 24-hour HH:MM format
- `\u` : Username of the current user
- `\w` : Current working directory
- `\W` : Basename of the current working directory
- `\$` : Displays `$` for normal users, and `#` for root user

Method to add colours:

- Use ANSI escape sequences (For more information, can explore on Internet)
- Enclosed with `\[` and `\]`