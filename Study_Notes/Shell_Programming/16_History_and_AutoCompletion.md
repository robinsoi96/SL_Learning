# Shell History & Tab Autocompletion

## Shell History

Every executed command is recorded to the shell history.

- Shell history can be displayed and recalled

- Some shells like bash keep their memory and on disk, usually are `~/.bash_history`, `~/.history` or `~/.histfile`
    - The mentioned file is written the history **on exit**
    - To know what is your history file path, just run `echo $HISTFILE`

### Manipulation with `history` command

1) `history` command **displays the shell history**

2) `HISTSIZE` controls the number of commands to retain in history

    - To check default `HISTSIZE`, run this command below:

        ```shell
        echo $HISTSIZE # By default, the value is 1000
        # This means it will only record up to 1000 commands in Shell history
        ```
    
    - To change the `HISTSIZE`, just run this command below:

        ```shell
        export HISTSIZE = <NUMBER>
        ```

3) **Manipluation with `!` syntax:**

    - `!N` : Rerun the command line in history number N

    - `!-N` : Rerun the command line in last Nth history number

    - `!!` : Rerun the previous (N-1) command line

    - `!<string>` : Rerun the most recent command starting with `<string>`

    - `!?<string>?` : Rerun the most recent command as it contains `<string>`

    - `!:N` : 
    
        - `!` here is equivalent to `!!`
        - `:N` here represents a word on the command line [e.g. `:0`=command, `:1`=first argument, etc]
    
    - `!^` : First argument of previous (N-1) command == `!:1`

    - `!$` : Last argument of previous (N-1) command

    - If add `:p` for all mentioned `!` syntax above, it will only print the 

4) `^<old_string>^<new_string>` : This **rerun the previous (N-1) command** but **`<old_string>` in the previous (N-1) command will be replaced with `<new_string>`**

5) **Shell History Search:**

    - `Ctrl + r` : Reverse shell history search

        - You can type character(s) and then keep pressing `Ctrl + r` to find the reverse search you want

        - Hit `Esc` to exit reverse search

    - `Ctrl + g` : Cancel the search

    - `Enter` : Execute the command

    - `Arrow keys (Up or Down)` : Change the command / Manually scroll history search
    
    - `history | grep <KEYWORD>` : List all command history with `<KEYWORD>`

## Tab AutoCompletion

`Tab` autocompletion is useful for below:

- Commands
- Files, directories, paths
- Environment variables
- Usernames (~)