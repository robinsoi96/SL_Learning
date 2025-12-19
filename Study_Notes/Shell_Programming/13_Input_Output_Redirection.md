# Input/Output in Shell Programming

## Output

### Output to the Terminal

#### `echo`

Generic syntax using `echo` command:

```shell
echo <string>

echo $<variable_name>
```

Escape sequences for `echo` command:

| Escape sequence | Description |
|:---:|---|
| `\n` | Prints a newline character |
| `\t` | Prints a tab character |
| `\c` | Prints a string without a defaul trailing newline |

#### `printf`

1 major difference compared to `echo` command is that `printf` **explicitly requires the `\n` escape sequence at the end of the string, in order to print a newline**.

Basic syntax for `printf` command:

```shell
printf <format> <arguments>
```

- The *`<format>`* is a string that contains one or more of the formatting sequences
- The *`<arguments>`* are strings that correspond to the formatting sequences spcified in *`<format>`*
- The formatting sequences supported by `printf` command is **identical as in the C language `printf` function**

**Formatting sequences have the form:**

```
%[-]m.nx
```

- `%` starts the formatting sequence

- `x` identifies the formatting sequences type

	| Letter | Formatting Sequence Type |
	|:---:|---|
	| `s` | String |
	| `c` | Character |
	| `d` | Decimal (integer) number |
	| `x` | Hexademical number |
	| `o` | Octal number |
	| `e` | Exponential floating-point number |
	| `f` | Fixed floating-point number |
	| `g` | Compact floating-point number |

- Depending on the value of `x`, the integers `m` and `n` are interpreted differently

	- Usually, `m` is the minimum length of a field, and `n` is the maximum length of a field
	- If you specify a real number format, `n` is treated as the precision that should be used

- `-` left justifies a field. By default, all fields are right justified

### Output Redirection

#### Overwrite Redirection to a File (using `>`)

Generic syntax:

```shell
command > file
```

What it does:

- The output of the *`command`* is overwritten to *`file`*
- If *`file`* does not exist by default, *`file`* will be created

#### Appending Redirection to a File (using `>>`)

Generic syntax:

```shell
command >> file
```

What it does:

- The output of the *`command`* is appended to *`file`*

#### Using `tee` command (Redirect to a File and to Terminal)

Syntax to **overwrite** using `tee` command:

```shell
command | tee file(s)
```

Syntax to **append** using `tee` command:

```shell
command | tee -a file(s)
```

## Input

### Input Redirection

#### Using `<`

Generic syntax:

```shell
command < file
```

What it does:

- The content of *`file`* becomes the input for the *`command`*

#### Here Documents (using `<<`)

Generic syntax:

```shell
command << delimiter
document
delimiter
```

Explanation:

- *`document`* is the input text to be written to the *`command`*

- *`delimiter`* is written before `<<` as the beginning to get the manual input content in *`document`* and must be mentioned at the end.

	- *`delimiter`* can be any keyword, e.g. `EOF`, etc

Extras:

- To append manual input text to a file via command:

	```shell
	command >> file << delimiter
	document
	delimiter
	```

- To overwrite manual input text to a file via command:

	```shell
	command > file << delimiter
	document
	delimiter
	```

### Reading User Input

`read` command is used to read user input.

For more info, may search from internet, or run `man read` in Linux.

## File Descriptors

When you issue any command, three files are opened and associated with that command.

In the shell, each of these files is represented by a small integer called `file descriptor`.

A file descriptor is a **mechanism by which you can associate a number with a filename and then use that number to read and write from the file**. Sometimes, file descriptors **are called `file handles`**.

The three files opened for each command along with their corresponding file descriptors are:

- **Standard Input (STDIN)**, `0`
- **Standard Output (STDOUT)**, `1`
- **Standard Error (STDERR)**, `2`

### Implementation of file descriptors in I/O redirection

```shell
command 1> file # Equivalent to: command > file
# Not needed, redundant for statement above. Just extra info

command 1>> file # Equivalent to: command >> file
# Not needed, redundant for statement above. Just extra info

command 0< file # Equivalent to: command < file
# Not needed, redundant for statement above. Just extra info

command 2> file # STDERR of command overwritten to file

command 2>> file # STDERR of command append to file

command > file1 2> file2 # STDOUT written to file1; STDERR written to file2

# EXTRAS:
# Merge redirection:
# n>&m : Merges output from stream n with stream m
# n<&m : Merges input from stream n with stream m

command > file 2>&1 # Redirecting STDOUT and STDERR to the file
# Same as command &> file

command >> file 2>&1 # Redirecting STDOUT and STDERR, but appending to the file
# Same as command &>> file

# EXTRAS:
# You can use redirection with /dev/null (Null Device) as a "black hole" or "bit bucket" to discards all data written to it, or redirect output to nowhere

command > /dev/null # Discards standard output (STDOUT)
# Useful when you only care about whether a command succeeds or fails, not its output

command 2> /dev/null # Discards standard error (STDERR)
# Hides error messages while still showing the normal program output

command > /dev/null 2>&1 # Discard both STDOUT and STDERR
# This makes the command completely silent

## EXTRA KNOWLEDGE:
# /dev/null also useful to empty large log file without deleting it, together with cat command, as the sample command below
cat /dev/null > logfile
```