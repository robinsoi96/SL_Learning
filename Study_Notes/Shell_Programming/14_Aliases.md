# Shell Aliases

Aliases are known as **shortcut keys** you set for commands to be executed.

- Use for long commands
- Use for commands you type often

Command to check all aliases set:

```shell
alias
```

Command to create aliases:

``` shell
# Temporary set alias in the current session only
alias <ALIAS_NAME>='<COMMAND>'

# Persist changes for aliases set
# Method 1:
echo 'alias <ALIAS_NAME>="<COMMAND>"' >> ~/.bash_profile
# Method #2:
echo 'alias <ALIAS_NAME>="<COMMAND>"' >> ~/.bashrc
source ~/.bashrc # This might need to make the new $PS1 value effective
```

Command to remove alias:

```shell
# Remove specific alias
unalias <ALIAS_NAME>

# Remove all aliases
unalias -a
```