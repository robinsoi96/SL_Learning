# Working with Files & Directories

## Listing Files and Directories

| Command | Explanation |
|:---:|---|
| `ls` | List all files and directories in the current directory, where all non hidden files and directories are not listed in new separate line respectively <br><br> You can run `ls <DIR_NAME>` to list all content in the directory `<DIR_NAME>` |
| `ls -a` | List all files including hidden files <br><br> Hidden file listed will have `.` in front of the filename listed <br><br> Extras: <br> When running `ls -a`, you will also see files named `.` and `..` <br> `.` refers to current directory & `..` refers to parent directory |
| `ls -A` | Same as `ls -a`, except it does not show current directory (`.`) and parent directory (`..`)|
| `ls -F` | This command can help you to identify whether the listed items are files or directories <br><br> If you see `/` at the end of the item listed, it is a directory. If not, it is a file. <br><br> For special files, you will see character such as `!` , `@` or `#` is append to the filename <br> <ul><li>`/` : Directory</li><li>`@` : Link or Symbolic link</li><li>`*` : Executable</li><li>`\|` : FIFO (First In, First Out) or pipe</li><li>`=` : Socket</li><li>(Nothing) : Regular non-executable file</li></ul>|
| `ls -l` | List where every files and directories are at separate line <br><br> For each filename in each line, it will also tell you the file type, permissions, number of links, owner, group, file size, last datetime modifed, and the filename <br><br> You can run `ls -lh`, so that the file size is in a human-readable format like KB,MB,GB instead of just raw bytes |
| `ls -g ` | List all files and directories with the group name <br> Owner name will not be displayed in the output |
| `ls -i ` | Print inde number of each files and directories |
| `ls -m` | List all files and directories separated by comma `,` |
| `ls -n` | List numeric UID and GID of Owner and Groups |
| `ls -r` | List all files and directories in reverse order |
| `ls -R` | Shortlist all directories content |
| `ls -t` | Sorted by modified time, started with the newest file |
| `ls --color` | Enforce colourize output of `ls` |

For more info on how to play around with `ls` command, can either run `man ls` in Linux system or search on the internet

**EXTRAS:**

There is `tree` command you can use, which is similar to `ls -R`, but creates visual output

- `tree` : Show content of directory in a hierarchical, tree-like format
- `tree -C` : Same as `tree` but enforce colourize the output
- `tree -d` : `tree` but list directories only

You may or may not have `tree` installed by default. If not, just install it if you want to.

## View Content of File

| Command | Explanation |
|:---:|---|
| `cat <filename>` | View all content of the file |
| `cat -n <filename>` | View all content of the file, where line numbers are reflected as well |
| `cat -b <filename>` | Same as `cat -n <filename>`, except it skips the numbering blank lines |
| `tac <filename>` | View all content of the file, but the last line will be on the top and the first line will be at the bottom |
| `nl <filename>` | Show all content of the file, but will only number the non-empty lines |
| `less <filename>` | Act as "pager" to display content of files one screen at a time, when the content is too long to fit in a single terminal <br><br> - Offers both `forward and backward scrolling` <br> - Press `q` to quit cleanly |
| `more <filename>` | Similar as `less` command mentioned above <br><br> **Differences compared to `less` command:** <br> - Offers `scrolling`, but scroll screen to screen only, `not flexible compared to the scrolling in less command` <br> - Press `q` to quit, but `not quit cleanly, leaving last displayed page` |

## Counting Words in File

| Command | Explanation |
|:---:|---|
| `wc <filename>` | This command counts number of lines in the file, number of words in the file, and number of characters in the file <br><br> You can also try with multiple files, e.g. `wc <filename1> <filename2>`. Here it performs the same as `wc <filename>`, except it prints the results for different filenames and also the total numbers |
| `wc -l <filename>` | Count the number of lines in the file |
| `wc -w <filename>` | Count the number of words in the file |
| `wc -c <filename>` <br> or <br> `wc -m <filename>` | Count the number of characters in the file |

## Copying Files and Directories

### Copy Files

| Command | Explanation |
|:---:|---|
| `cp <src_file> <dest_file>` | Copy `<src_file>` to `<dest_file>` <br><br> If `<dest_file>` does not exist, it will be created and having all content copied from `<src_file>`. However, if already exists, `<dest_file>` will be overwritten without any warning |
| `cp <src_file> <dest_directory>` | Copy `<src_file>` to destination directory `<dest_directory>` |
| `cp <src_file1> <src_file2> <src_file3> <dest_directory>` | Copy multiple files to destination directory `<dest_directory>` |

### Copy Directories

The difference of `cp` command implementation for copying directories compared to copying files is that you just need to add `-r` option after `cp`.

You may add `-f` option to copy forcefully.

It act like the same way as copying files, except `Destination` got to be a directory.

If you want to copy multiple files and directories to a single destination directory, all your `Source` can be the files and directories you want to copy.

## Moving / Renaming Files and Directories

You can use `mv` sample commands as below to rename or move file or directory

**Moving / Renaming File:**
```
mv <src_file> <dest_file>
```

**Moving / Renaming Directory:**

```
mv <src_directory> <dest_directory>
```

<br>

Below are the sample command to move multiple directories and files to a single destination directory:

```
mv <Source1> <Source2> <Source3> <Destination>
```

NOTE:

- `<Source>` can be either file or directory
- `<Destination>` can only be a directory

## Making Files and Directories

- `touch <filename>` to make new empty file
- `mkdir <filename>` to make single level directory
- `mkdir -p <filename>` to make multi-level directory

**EXTRAS:**

- `<editor><filename>` to use editor (e.g. vim, nano, etc) to create and then save content to make new file
    
    - On how to utilizing different editors, please check on internet

## Removing Files and Directories

- `rm <filename>` to remove file
- `rmdir <directory>` to remove empty directory
- `rm -r <filename>` to remove file / directory recursively
- `rm -rf <filename>` to remove file / directory recursively and forcefully

## File Archiving Utility

| Command used | File format | Extract Command | Archive or Compress Command |
|:---:|:---:|:---:|:---:|
|`tar` command with `-z` option| .tar.gz / .tgz | `tar -zxvf <FILE>.tar.gz` <br><br> `-k` : Keep existing `<FILE>` | `tar -zcvf <FILE>.tar.gz <DIRECTORY>` |
|`tar` command with `-j` option| .tar.bz2 | `tar -jxvf <FILE>.tar.bz2` <br><br> `-k` : Keep existing `<FILE>` | `tar -jcvf <FILE>.tar.bz2 <DIRECTORY>` |
|`tar` command with `-J` option| .tar.xz | `tar -Jxvf <FILE>.tar.xz` <br><br> `-k` : Keep existing `<FILE>` | `tar -Jcvf <FILE>.tar.xz <DIRECTORY>` |
|`tar` command | .tar | `tar -xvf <FILE>.tar` <br><br> `-k` : Keep existing `<FILE>` | `tar -cvf <FILE>.tar <DIRECTORY>` |
| `gunzip` / `gzip` <br><br> Extras: <br> `gzcat` / `zcat` : `gunzip -c` to view compressed files | .gz | `gunzip <FILE>.gz` <br><br> EXTRAS: <br> **Recursively decompress all files in directory <br> `gunzip -r <DIRECTORY>` <br><br> `-k` : Keep existing file | `gzip <FILE>` <br><br> EXTRAS: <br> **Recursively decompress all files in directory <br> `gzip -r <DIRECTORY>` |
| `unzip` / `zip` | .zip | `unzip <FILE>.zip` | `zip -r <FILE>.zip <DIRECTORY/FILE>`|

## Check Disk Usage by File 

- `du [FILE]` : Estimates file usage
- `du -k [FILE]` : Display sizes in kilobytes
- `du -h [FILE]` : Display sizes in human readable format

## Comparing Content of Files

- `diff file1 file2` : Compare two files

    - `<LineNum_file1><Action><LineNum_file2>`, where `<Action>` can be (`a`)dd , (`c`)hange or (`d`)elete

    - `<` : Diff line from file1

    - `---` : Separator between two files' lines in a change hunk

    - `>` : Diff line from file 2

    - Here only explain on `diff` command, you may explore yourself on `diff -u` (Unified Format), `diff -c` (Context Format), `diff -y` (Side-by-side), `diff -q` (Brief Output, where only report if files differ)

- `sdiff file1 file2` : Side-by-side comparison

    - `|` : Differing line(s)
    - `<` : Additional line from file1
    - `>` : Additional line from file2

- `vimdiff file1 file2` : Highlight differences in vim

    - Important command modes:

        - `Ctrl+w w` : Go to next window
        - `:q` : Quit (close current window)
        - `:qa` : Quit all (close both files)
        - `:qa!` : Force quit all