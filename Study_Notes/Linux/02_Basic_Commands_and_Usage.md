# Linux Basic Commands & Usage

This section only shares on basic common commands and usage across any Linux distribution.

## Linux Basic Commands

**NOTE:** Linux commands are **case-sensitive**

| Linux Command | Description |
|:---:|---|
| `pwd` | Display rresent working directory or current directory |
| `cd` | Changes directory path <br><br> Command line usage: <br> `cd <dir>`, where `<dir>` is the directory path you wish to change to <br><br> `cd ~` : Navigate the home directory of user account <br> `cd -` : Navigate to previous directory you went <br> `cd ..` : Navigate to parent directory <br> `cd` : Back to home directory of user account <br> `cd .` : Navigate to current directory (usually redundant to do so) |
| `ls` | List directory contents <br><br> More detailed implementation, can refer to [my personal note on `ls` command](../Shell_Programming/02_Working_with_Files_and_Directories.md#listing-files-and-directories) |
| `cat` | Concatenates and display files <br><br> More detailed information, can refer to [my personal note on `cat` command](../Shell_Programming/02_Working_with_Files_and_Directories.md#view-content-of-file) |
| `clear` | Clears the screen |
| `exit` | Exit the shell or the current session |

## Directory Shortcuts

- `.` : Current directory
- `..` : Parent directory
- `~` : Home directory of user account

## Check Manuals for the Command

1) Using `man` command

    - Used to display documentation for a given command

    - General usage as below:

        ```
        man <command>
        ```

        - Keyboard Commands:
        
            - `enter` : move down by 1 line
            - `space` : move to the next page
            - `q` : quit
            - `up key` : scroll up by 1 step
            - `down key` : scroll down by 1 step
            - `g` : Move to the top of the page
            - `G` : Move to the bottom of the page
    
    - `man -k <keyword>` is used to search the manual page descriptions for a specific keyword, which works equivalent to `apropos` command

2) Using `-h` or `--help`

    - Add them behind the command
    - Similar to `man` command, but shorter manual
    - Try `-h` if `--help` does not work for some commands, and vice versa

## How to check all executable programs available in your Linux environment?

- Examine your `$PATH` environment variable, by running `echo $PATH` command

    - `:` in the `echo $PATH` output is the delimiter to separate different directories in `$PATH` environment
    - Every directory in `$PATH` environment is where commands and executable programs are installed or located at

- Run `which <command/executable_file>` to check where is the command or executable file located

**NOTE:**

- If the command or executable file is within the directories under `$PATH` environment variable, then you can run the command or executable file directly, e.g. running `<command>` directly in the terminal

- However, if not available within the directories under `$PATH` environment variable, then you need to mention the directory where the command or executable file is installed, e.g. run `<Directory_of_command>/<command>` in the terminal