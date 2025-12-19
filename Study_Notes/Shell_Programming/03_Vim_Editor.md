# Vim Editor

Vim editor is 1 of the most common test editor used in Linux system.

If your system has no vim editor, you can opt to install it.

## 3 Modes in Vim Editor

There are 3 modes:
- Command mode
- Insert mode (edit mode)
- Extended command mode

**NOTE: When you open the vim editor, it will be in the command mode by default**

**EXTRAS:** You can run `vimtutor` in the terminal to see full documentation on using vim editor

### Command Mode

Below are some basic way to implement in command mode

| Key | Command Mode Action|
|:---:|---|
| `gg` | Go to the beginning of the page |
| `G` | Go to the end of the page |
| `w` | Move the curosr forward, word by word |
| `b` | Move the cursor backward, word by word |
| `nw` | Move the cursor forward to n words <br><br>E.g `4w` --> move cursor backward to 4 words |
| `nb` | Move the cursor backward to n words <br><br> E.g. `4b` --> move cursor backward to 4 words |
| `k` | Move cursor up one line |
| `j` | Move cursor down one line |
| `^` | Go to beginning of the line |
| `$` | Go to end of the line |
| `u` | Undo the last change (word) |
| `U` | Undo the previous changes (entire line) |
| `Ctrl + R` | Redo the changes |
| `yy` | Copy a line |
| `nyy` | Copy n lines <br><br> E.g. `4yy` ---> Copy 4 lines |
| `y<POSITION>` | Copy the `<POSITION>` <br><br> `<POSITION>` can be: <ul><li>`nw` : Copy n words, where n = number of word</li><li>`iw` : Copy the word where the cursor is positioned</li><li>`$` : Copy from the cursor till the end of line</li><li>`t<char>` : Copy from the cursor till the character `<char>`, where `<char>` is not included</li><li>`n + SPACEBAR` : Copy n numbers of characters, where n is number of characters to be copied</li></ul> |
| `p` | Paste after the cursor position |
| `P` | Paste before the cursor position |
| `dw` | Delete  the word letter by letter (like Backspace) |
| `x` | Delete the word letter by letter (like DEL key) |
| `D` | Delete from the current cursor position in the line |
| `dd` | Delete entire line |
| `ndd` | Delete n number of lines from the cursor position <br><br> E.g. `4dd` --> Delete 4 lines from the cursor position |
| `yyp` | Copy paste |
| `ddp` | Cut paste |
| `/<KEYWORD>` | To search a word in the file <br><br> You can hit `n` for next search & `N` for previous search of the same word in the file |
| `?<KEYWORD>` | Reverse of `/<KEYWORD>` <br><br>To search a word in the file <br><br> You can hit `N` for next search & `n` for previous search of the same word in the file |
| `~` | Reverse the case of a character where cursor is pointing |
| `r<CHARACTER>` | Replace the character where cursor is pointing with `<CHARACTER>`|
| `cw` | Remove the word where cursor is pointing, and then proceed to insert mode for you to update accordingly |
| `cc` | Remove the entire line where cursor is pointing, and then proceed to insert mode for you to update accordingly |
| `c$` | Remove the remaining end of the line where cursor is pointing (the text before cursor position remains), and then proceed to insert mode for you to update accordingly |
| `C` | Same as `c$` |
| `v` | Visual Mode <br><br> Useful to copy multiple lines with ease <br><br> Hit `v` to indicate the starting position to be copied, and then use navigation keys (e.g. `h`, `j`, `k`, `l` or arrow keys) to map what to be copied, and then lastly hit `y` to copy the content highlighted in visual mode |

NOTE: You can always search in the internet for more other info which is not listed in the table above

### Insert Mode

To edit the content of the file in vim editor, press `i` to proceed.

After pressing `i`, you are in insert mode or edit mode. There, you can start writing your content.

**EXTRAS:**

- `i` : Insert at the cursor position
- `I` : Insert at the beginning of the line
- `a` : Append after the cursor position
- `A` : Append at the end of the line
- `<number>i<Text> + Esc` : Insert `<Text>` for `<number>` times starting from cursor position to the file

To exit insert mode, just hit `Esc` button.

### Extended Command Mode

To use extended command mode, press `Esc` with key `:`

Below are some basic implementation for extended command mode

| Key | Extended Command Mode Action |
|:---:|---|
| `:w` | Save changes |
| `:w!` | Forces the file to be saved |
| `:q` | Quit without saving |
| `:q!` | Quit forcefully without saving |
| `:wq` | Save and quit |
| `:wq!` | Save and quit forcefully |
| `:x` | Same as `:wq!` |
| `:n` | n here is to type a number <br><br> E.g. `:4` --> Go to line no.4|
| `:$` | Position the cursor on the last line |
| `:se nu` | To show the line numbers in the file |
| `:se nonu` | To remove line numebrs shown in the file from previous key `: se nu` |
| `:help [command]` | Get help on the `[command]` <br><br> Run `:q` to quit the help menu |

NOTE: You can always search in the internet for more other info which is not listed in the table above