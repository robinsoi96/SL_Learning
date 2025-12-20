# Variables

## Defining Variables

To define a single string variable value:

```bash
varName=varValue
```

If variable value consists of spacing:

```bash
varName="varValue"
```

Method to access the defined variable's value

```bash
echo $varName
```

## Array Variables

To define array variable:

```bash
varName[index]=varValue
```

Method to access defined array variable:

```bash
echo ${varName[index]}
```

Method to access all items in the array variable:

```bash
# Method 1
echo ${varName[*]}

# Method 2
echo ${varName[@]}

# Both will display same output

# However, if one of your item in the array variable has an extra spacing, Method 1 will see extra 1 item, which is not accurate

# Therefore, Method 2 is much preferred
```

## Read-only Variables

Shell provides a way to mark variables as read-only by using the `readonly` command.

After a variable is marked read-only, its value cannot be changed.

Sample bash pseudocode:

```bash
FRUIT=kiwi # Define FRUIT to be "kiwi"
echo $FRUIT # Print "kiwi"

FRUIT=apple # Value of FRUIT able to change to "apple"
echo $FRUIT # Print "apple"

readonly FRUIT # Set FRUIT to be read-only variable

FRUIT=pineapple # Here, it will fail before proceed to next line, because it has set to read-only before this line
echo $FRUIT
```

**NOTE:** variable decalred with `readonly` command cannot be unset or modified within the same shell session

## Unsetting Variables

Unsetting a variable is to tell shell to remove the variable from the list of variables it tracks.

Command to unset variable:

```bash
unset varName
```

**NOTE:** You cannot unset a variable that is marked `readonly`

## Types of Variables

When a shell is running, there are 3 main types of variables:

- Local variables
- Environment variables
- Shell variables

### Local Variables

- Present within the current instance of the shell
- Not available to programs that are started by the shell
- The variables mentioned on the chapters above are local variables

### Environment Variables

- Available to any child process of the shell
- Some programs need environment variables in order to function correctly

### Shell Variables

- Special variables set by the shell
- Required by the shell in order to function correctly

### Comparison of Local, Environment, and Shell Variables

| Attribute | Local Variables | Environment Variables | Shell Variables |
|---|:---:|:---:|:---:|
| Accessible by child process | No | Yes | Yes |
| Set by users | Yes | Yes | No |
| Set by shell | No | No | Yes |
| User modifiable | Yes | Yes | No |
| Required by the shell | No | No | Yes |

## Exporting Environment Variables

```bash
export envVarName # This is the method to export environment variable

# Method to set a new environment variable
envVarName=value ; export envVarName

# Another method to set new environment variable
export envVarName=value

# Method to add on new value on top of existing environment variable

# Let's use PATH as an example, and add /bin to PATH
PATH=/bin:$PATH ; export PATH

# Or can do like this
export PATH=/bin:$PATH

# Print environment variable
echo $envVarName

# Command to print all environment variables
env # Method #1
printenv # Method #2
```

## Special Shell Variables

There are some common shell variables, e.g. `$PWD`, `$RANDOM`, `$PATH`, `$UID`, `$HOME`, `$SECONDS` etc. (where you can study for more in internet).

Now, would like to highlight on useful special shell variables for shell scripting in sub-chapter below.

### Special Shell Variables

| Variable | Description |
|:---:|---|
| `$0` | The name of the command being executed <br><br> For shell scripts, this is the path with which it was invoked |
| `$n` <br><br>where `n` is from 1 to 9| The variable correspond to the arguments with which a script was invoked <br><br> E.g.: <br> `$1` = first argument to the script |
| `$#` | The number of arguments supplied to the script |
| `$*` | All the arguments are double quoted <br><br> Sample command: <br> ./File.txt A B "C B" E <br><br> `$*` will view the arguments as: <br> "A B C B E"|
| `$@` | All the arguments are individually double quoted <br><br> Sample command: <br> ./File.txt A B "C B" E <br><br> `$*` will view the arguments as: <br> "A" "B" "C B" E"|
| `$?` | The exit status of the last command executed |
| `$$` | The process number of the current shell <br><br> For shell script, this is the process ID under which they are executing |
| `$!` | The process number of the last background command |