# Text Filters

## The `head` Command

| Common `head` command usage | Explanation |
|:---:|---|
| `head <filename>` | Print **first 10 lines of the file** |
| `head -<number> <filename>` <br> or <br> `head -n <number> <filename>` | Print **first \<number> lines of the file** |
| `<command> \| head` | Show **first 10 lines of output of `<command>`** |
| `<command> \| head -<number>` <br> or <br> `<command> \| head -n <number>` | Show **first \<number> lines of output of `<command>`** |

## The `tail` Command
| Common `tail` command usage | Explanation |
|:---:|---|
| `tail <filename>` | Print **last 10 lines of the file** |
| `tail -<number> <filename>` <br> or <br> `tail -n <number> <filename>` | Print **last \<number> lines of the file** |
| `<command> \| tail` | Show **last 10 lines of output of `<command>`** |
| `<command> \| tail -<number>` <br> or <br> `<command> \| tail -n <number>` | Show **last \<number> lines of output of `<command>`** |
| `tail -f <filename>` | Follow the file and displays data as it is being written to the file (in real time) |

## The `grep` Command

| Command `grep` command usage | Explanation |
|:---:|---|
| `grep <keyword> <filename>` | Displays all lines with `<keyword>` in the file |
| `grep -i <keyword> <filename>` | Display all lines with `<keyword>` (case-insensitive) in the file |
| `grep -n <keyword> <filename>` | Displays all lines with `<keyword>` in the file, and showing the line number as well |
| `grep -v <keyword> <filename>` | Displays all lines **without** `<keyword>` in the file |
| `grep -c <keyword> <filename>` | Count the number of lines with `<keyword>` in the file |
| `<command> \| grep <keyword>` | Displays all lines of output of `<command>` with `<keyword>` |
| `grep -r <keyword> <directory>` | Display all lines with `<keyword>` in the file of the `<directory>` |

**NOTE:** If the `<keyword>` is more than just 1 word (e.g. New York), then your sample `grep` command will look as below:

```
    grep '<keyword>' <filename>
```

## The `tr` Command

Basic syntax of `tr` command is as below:

```
    tr '<set1>' '<set2>'
```

- `<set1>` is the character set to be transliterated (changed / replaced)
- `<set2>` is the final character set transliterated (changed / replaced)
- In short, `<set1>` --> `<set2>`
- Character sets can be solely characters, or characters with wildcard, or special characters
- To make sure `tr` works well regardless version installed in Linux, it is best to have both `<set1>` and `<set2>` having same number of character sets
- `tr` command has many options to play around with. For more info, can search on internet, or run `man tr` or `tr --help`.

## The `sort` Command

`sort` command basically sorts the lines of output in order.

For more info, can run `man sort` or `sort --help`

## The `uniq` Command

`uniq` command removes duplicate lines of the output, but `only able to remove continuous duplicate lines`.

For more info, can run `man uniq` or `uniq --help`

## The `cut` Command

Below are the most commonly used options with `cut` command:

| Option | Description |
|:---:|---|
| `-b`, --bytes=LIST | Selects only the `bytes` specified in LIST |
| `-c`, --characters=LIST | Selects only the `characters` specified in LIST |
| `-d`, --delimiter=DELIM | Uses DELIM as the `field delimiter` character instead of the tab character (by default) |
| `-f`, --fields=LIST | Selects only the `fields` specified in LIST, `separated by the delimiter character` (default is tab, or delimiter decalred in `-d`) |
| `-n` | `Do not split multi-byte characters` (no effect unless `-b` or `-c` is specified) |
| `--complement` | Invert the selection of fields/characters. <br> `Print the fields/characters not selected`.|
| `--output-delimiter` | `Changes the output delimiter for fields` in the cut command bash. |

**NOTE:** <br>
For more detailed examples, can refer to <a href="https://www.geeksforgeeks.org/linux-unix/cut-command-linux-examples/">`cut` command in Linux with examples</a>

## The `find` Command

`find` command is used to find the files or directory's path.

Generic syntax of `find` command:

```
find <starting_directory> <option> <expression>
```

**Options that can be used with `find` command:**

| Option | Usage |
|:---:|---|
| `-name` | For searching a file with particular naming pattern <br><br> Use case: `-name "<PATTERN>"` |
| `-iname` | For searching a file with particular naming pattern, but ignore the case <br><br> Use case: `-name "<PATTERN>"` |
| `-inum` | For searching a file with particular inode number |
| `-type` | For searching a particular type of file <br><br> Use case: `-type [file_type]` <br><br> File type can be in: <ul><li>`f` : Regular file</li><li>For the rest file type, can refer to [my note of file type](./04_Manipulating_File_Attributes.md#identify-file-type)</li></ul> <br><br> You can use `-xtype l` to check if the symbolic link is broken by testing what it points to |
| `-user` | For files whose owner is a particular user |
| `-group` | For files belonging to particular group |
| `-ls` | Performs `ls` on each of the found items |
| `-mtime` | Finds files that are days old <br><br> Use cases: <ul><li>`-mtime <DAYS>` : Modified exactly the amount of days ago</li><li>`-mtime -<DAYS>` : Modified within the amount of days</li><li>`-mtime +<DAYS>` : Modified more than the amount of days ago</li></ul> |
| `-size` | Find the files with matching size mentioned <br><br> Syntax to use: `-size [prefix][number][unit]` <br><br> For `[prefix]`, it can be: <ul><li>`+` : Find all files greater than</li><li>`-` : Find all files smaller than</li><li>Leave it blank : Find all files exactly or around the size given</li></ul> <br><br> For `[number]`, it is just number you set <br><br> For `[unit]`, it can be: <ul><li>Leave it blank : 512-byte blocks</li><li>`c` : Bytes</li><li>`k` : Kilobytes (1024 bytes)</li><li>`M` : Megabytes (1024KB)</li><li>`G` : Gigabytes (1024 MB)</li><li>`w` : Two-byte words</li></ul> |
| `-newer` | Finds files that are newer than the file mentioned <br><br> Use case: `-newer <FILE>`|
| `-exec` | Run command against all the files that are found <br><br> General structure to use the command: <br> `find [path] [criteria] -exec [command] {} [terminator]` <br><br> `[path]` : Directory to perform `find` command <br><br> `[criteria]` : Either 1 of the action as mentioned in the rows above, e.g. `-name "*.txt"` <br><br> `[command]` : Command to be executed for all files listed by `[criteria]` <br><br> `{}` : Placeholder, represents the current file path found by `find` <br><br> `[terminator]` can be: <ul><li>`\;` : Executes `[command]` once for each file found</li><li>`+` : Combines multiple files into a single `[command]` execution (more efficient for many files)</li></ul> <br><br> **EXTRA:**<br>You can change to `-ok` instead `-exec` to prompt for confirmation before each action, e.g. you can do it with safe deletion in scenario where `rm` command is in `[command]`|

**NOTE:** For more information, can always search on internet

## The `locate` Command

General syntax:

```shell
locate <PATTERN>
```

- List all files that match pattern
- Faster than the `find` command
- Queries an index
- Results are not in real time, but based on pre-built database (require `updatedb` command to update before running it)
- May not be enabled on all Linux systems, which you need to install if not available
- If you want to search on real-time accurately, `find` is a better choice even though it will be slower than `locate`