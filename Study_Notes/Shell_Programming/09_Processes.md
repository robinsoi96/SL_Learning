# Processes in Linux/Unix

## Starting a Process

The operating system tracks processes through a `five digit ID` number known as `PID` or `process ID`.

- Each process in the system has a unique PID
- Used up PIDs can be used in again for a newer process since all the possible combinations are used
- At any point of time, `no two processed with the same PID exist` in the system because it is the PID that Unix uses to track each process.

You can use `ps` command to see what processes you are running and all processes on the system

When you start a process (run a command), there are two ways you can run it, either in `foreground` or `background`. 

The difference is how th process interacts with you at the terminal.

## Foreground Processes

By default, every command you executed is in the foreground.

When the command is running, you cannot run any other commands until the current command is done executed.

- `Ctrl + c` to kill foreground process
- `Ctrl + z` to suspend foreground process for most systems (To verify, run `stty -a`)

**NOTE:**
- When you log off or are disconnected from the system by a communication problem, your process will be termined
- If you have a long running process that you do not want terminated, you need to use the nohup command, where nohup stands for no HUP (Hang UP) 
- Th nohup command will be explained in later section

## Background Processes

Background process runs without keyboard input and waits until keyboard input is required.

The advantage of running a process in the background is that you can run other commands, where you do not have to wait until it completes to start another.

The simplest way to start a background process is to **add an ampersand (`&`) at the end of the command**.

### Running background process

1) When you run a background process, you will **instantly see an output line** where:

    - **1st field** is the **job number or ID**
    - **2nd field** is the **process ID (PID)**

2) After that, you will **see the output of the background process as the process is running in the background.**

3) When you **press Enter key after the background process has done its execution**, you will **see a line**, where:
    
    - **1st field** is the **job number or ID** 
        - `+` indicates the latest background job triggered
        - `-` indicates the last background job before the latest bckground job
        - **NOTE:** `+` and `-` can be used as job number
    - **2nd field** is the **status of the job or exit code of the job**
    - **3rd field** is the **command**

**NOTE:**

If you do not see the completion message of the background process command, it might be because your shell has been told not to show it to you.

- You can **enable monitoring** with the following command: `set -o monitor`
- To **disable the monitoring messages**, run this command: `set +o monitor`
- You can also **check all the shell options** with the following: `set -o`

## Moving Foreground Process to Background

While foreground process is running, before you can enter any commands, you have to suspend the foreground process to get a command prompt.

- The `suspend key` on most UNIX system is `Ctrl+Z`
- To check which key performs which function, can use `stty -a` command

When a foreground is suspended, a command prompt enables you enter a new command; the original process is still in memory but not getting any CPU time.

When you **suspend the current foreground process**, you will **see a line**, where the **1st field having number in the bracket indicating job number**.

To resume the job in background, use `bg` command as below:

```shell
    # Background a suspended foreground process
    bg %<job_number>
```

## Moving Background Process to Foreground

When you have a process that is in the background or suspended, you can use `fg` command as below to move it to foreground.

```shell
    fg %<job_number>
```

## Keeping Background Process Around (`nohup` Command)

`nohup` command **prevents your process from getting the HUP (Hang UP) signal** and enables it to **continue processing**.

There are 2 main methods to run `nohup` command:

1) Save the process output to default nohup.out file

```shell
    nohup <command> &
```

**NOTE:** <br>
If you keep on **running the same `nohup` syntax for different command** as above, the **output will only keep on appending to the default nohup.out file** assuming you run the commands in the same path, **unless you remove the previous nohup.out file** before you will be running the next one.

2) Save the process output to specific file

```shell
    nohup <command> > <filename> &
```

## Waiting for Background Process to Finish (`wait` Command)

There are 2 ways to wait for a background process to finish before doing something else.

1) Press Enter key every few minutes until you get the completion message

2) Use `wait` command

<br>

There are 3 ways to use `wait` command

1) With no options [Wait until all background jobs to finish]

```shell
    wait
```

2) With a process ID [Wait until the specific PID to finish]

```shell
    wait <PID>
```

3) With a job number prefixed with a percent sign [Wait until the specific job number to finish]

```shell
    wait %<job_number>
```

## Listing Running Processes

### `jobs` Command

The `jobs` command shows you the **processes you have suspended** and **the ones running in the background**.

All the jobs shown in `jobs` command can be manipulated using `fg` and `bg` commands.

**Important NOTE:** 

- The **most recent job** will have `+` sign behind the job number in the bracket
- The **most recent job before the most recent job** will have `-` sign behind the job number in the bracket

### `ps` Command

`ps` command stands for `Process Status`. By default only `ps` command without any argument, it shows those processes that you are running.

#### Common `ps` Options

One of the most commonly used flags for `ps` is the `-f` (full) options. Below table tells the column headings of the output of `ps -f` command.

| Column Heading in `ps -f` Command | Description |
|:---:|---|
| `UID` | User ID that this process belongs to (the person running it) |
| `PID` | Process ID |
| `PPID` | Parent process ID (the ID of the process that started it) |
| `C` | CPU utilization of process |
| *unlabelled* | `nice value` &mdash; used in calculating process priority <br><br> For more information on `nice value`, can refer to sections [`nice` Command](#nice-command) or [`renice` Command](#renice-command) |
| `STIME` | Proces start time (when it begins) |
| `CMD` | The command that started this process <br><br> `CMD` with `-f` is different from `CMD` without it; it shows any command line options and arguments |

Two more common options are `-e` (for every) and `-u` (for user). These 2 options **can combine with `-f` option**, but **cannot combine with each other**.

To check every process in the system, run `ps -ef`.

To check all processes run by specific user, run `ps -u <user> -f`.

For more information, may check with `man ps`.

#### BSD `ps` Command Options

`ps aux` is the command with BSD syntax.

Below are the table to explain all BSD syntax accordingly.

| BSD syntax option | Description |
|:---:|---|
| `a` | Shows information about all users |
| `x` | Shows information about processes without terminals (daemons and jobs running nohup) |
| `u` | Shows additional information or display in a more verbose format (acts like `ps -f`)|

### Visualize hierarchical relationship (tree relationship) between parent and child processes

1) `ps -eH`

    - Show tree relationship with **standard indentation**

2) `ps -e --forest`

    - Show tree relationship with **ASCII art lines** (`\_`)
    - Optionally, you can run `ps -ef --forest` or `ps auxf` for full detail

3) `pstree`

    - Show tree relationship with **graphical tree** (`─┬─`) for readability

        - **NOTE:** By default, it merges identical branches (e.g., if you have 10 `apache2` processes, it shows `10*[apache2]`) to keep the output compact
    
    - `pstree -p` : Shows Process IDs (PIDs).
    - `pstree -u <USER>` : Shows user transitions.
    - `pstree -h` : Highlights the current process and its ancestors.
    - `pstree -a` : Includes full command-line arguments in the tree view for more detail.

## Killing a Process (`kill` Command)

Generic syntax to run `kill` command:

```shell
# Method #1 : with job number
kill [-SIG] %<job_number> 
# Method #2 : with PID
kill [-SIG] <PID>

# SIG == signal
# To check all available signal, run the below command
kill -l
# From there, you can see as the listing consists as below:
# <NUM>)SIG<NAME>
# The SIG in [-SIG] mentioned can be either <NUM> or <NAME>
```

There are 2 methods to run `kill` command:

1) With job number

```shell
    kill %<job_number>
```

2) With process ID

```shell
    kill <PID>
    # Equivalent to kill -15 <PID>
    # Also, equivalent to kill -TERM <PID>
```

`kill` commands as above will **send the `TERM` signal** to its child processes if applicable **to shut down the process** and eventually itself.

- One thing to note, a **process can choose to ignore the `TERM` signal from `kill` command**.

If a process ignore a regular `kill` command, you can use `kill -9` command accordingly as below syntax examples.

```shell
    kill -9 %<job_number> # Method #1
    
    kill -9 <PID> # Method #2

    ## EXTRAS: kill -9 == kill -KILL
```

- This will forces the process to end
- However, if you only run `kill -9` command on a process but forgot to run the same for its child process, then its child process will become an orphan process
- In that case, you will run another `kill -9` commands for all remaining orphan processes
- Therefore, it is best to ensure the main process is done with `kill -9` command including the respective child processes to avoid orphan processes

## `nice` Command

`nice` command is used to **set priority of the new command**.

```shell
    nice <priority_number> <new_command>
```

**NOTE:** <br>
- *`<priority_number>`* is `nice value` ranges from **-20 to 19**, where -20 is the highest priority (least "nice") and 19 is the lowest priority (most "nice")
- **INFO:** The default nice value is typically 0
- You may run **`ps` command with `-l` option to check the nice value (NI)** of the new command executed

## `renice` Command

`renice` command is used to **change priority of an already running process**.

`-n` option is used to tell the new `nice value`.

Below are 3 cases of using `renice` command:

1) Change priority of a process (use `-p` option)

```shell
    renice -n <new_nice_value> -p <PID>
```

2) Adjust priority of all processes belong to specific user (use `-u` option)

```shell
    renice -n <new_nice_value> -u <UID_or_User_ID_number>
```

3) Adjust priority of all processes belong to specific process group (use `-g` option)

```shell
    renice -n <new_nice_value> -g <GID_or_Group_ID_number>
```

**NOTE:** <br>
- *`<new_nice_value>`* is `nice value` ranges from **-20 to 19**, where -20 is the highest priority (least "nice") and 19 is the lowest priority (most "nice")
- **INFO:** The default nice value is typically 0
- You may run **`ps` command with `-l` option to check the nice value (NI)** of the new command executed

## `top` Command

`top` command is used to show all the running processes within the working environment of Linux.

It works very similar to Task Manager in Windows OS.

To quit the `top` command, just enter `q`.

Key in `?` for help.

**EXTRAS:** `htop` is very similar to `top`, except it is more colourful and interactive with Function keys

## Types of Processes

### Parent and Child Process

The 2nd and 3rd column of the `ps -f` comamnd shows `process id (PID)` and `parent's process id (PPID)` number.

**For each user process, there's a parent process in the system**, with most of the commands having shell as their parent.

When a **child** is forked or created from its parent, it **receives a copy of the parent's environment, including environment variables**. The child **can change its own environment, but those changes do not reflect in the parent and go away when the child exits**.

### Zombie and Orphan Process

After completing its execution a child process is terminated or killed and SIGCHLD updates the parent process about the termination and thus can continue the task assigned to it.

But at times **when the parent process is killed before the termination of the child process** (e.g. force kill the parent process using kill -9 command, but did not kill its child proceess), **the child processes become orphan processes**, with the parent of all processes "init" process, becomes their new pid.

A **process which is killed but still shows its entry in the process status or the process table** is called a **zombie process**, they are dead and are not used.

### Daemon Process

They are **system-related background processes** that often run with the permissions of root and services requests from other processes, they most of the time run in the background and wait for processes it can work along with (e.g. print daemon).

When `ps -ef` is executed, the process with `?` in the `tty` field are daemon processes.