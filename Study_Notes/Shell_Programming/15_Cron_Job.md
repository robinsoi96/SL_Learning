# Cron Jobs with Shell

If you need to repeat a task or a schedule, you can use the `cron` service.

Cron service is a **time-based job scheduling system** that **starts when the system boots**.

- The cron service checks to see if there are any scheduled jobs to run, and if so, it runs them.
- Every minute, cron jobs are often used to automate process or perform routine maintenance.
- You can schedule cron jobs by using `crontab` command.

## `crontab` Command

Usage of `crontab` command:

- `crontab -l` : List your cron jobs

- `crontab <CRON_FILE>` : Install a new crontab from `<CRON_FILE>`

    - **NOTE:** You can only have 1 `<CRON_FILE>` for this command, where the cron job will be overwritten if running the above command with another new `<CRON_FILE>`

    - To append new different cron file, run this command below:
    
        ```shell
        cat <CRON_FILE> | crontab -
        ```

    - To append new multiple different cron files, run this command below:
    
        ```shell
        cat <CRON_FILE_1> <CRON_FILE_2> ... <CRON_FILE_N-1> <CRON_FILE_N> | crontab -
        ```

- `crontab -e` : Edit your cron jobs

    - For this, you need to specify your text editor, e.g. `EDITER=vi` to set vim as the editor for cron jobs

- `crontab -r` Remove all of your cron jobs

Below is how you can edit the cron jobs in `<CRON_FILE>` or when running `crontab -e`
```shell
# Crontab format
<MINUTE> <HOUR> <DAY> <MONTH> <WEEK> <command>

# Explanation:
# <MINUTE> : Minute (0-59); * = Any
# <HOUR> : Hour in 24hr-format (0-23); * = Any
# <DAY> : Day of the Month (1-31); * = Any
# <MONTH> : Month of the Year (1-12); * = Any

# <WEEK> : Day of the Week (0-6); * = Any
#          0=Sun, 1 =Mon, ..., 6=Sat

# <command> : Command to be executed

# E.g.
# 0 7 * * 1 /opt/sales/bin/weekly-report
# The sample command above means it will run every Monday at 07:00

# E.g. 
# 0,15,30,45 * * * * /opt/sales/bin/weekly-report
# */15 * * * * /opt/sales/bin/weekly-report
# Both sample commands above are the same, where it runs every 15 minutes

# E.g.
# 0-4 * * * * /opt/sales/bin/weekly-report
# The sample command above run for first 5 minutes

# You can use Crontab shortcuts (special strings) as below
# Run `man 5 crontab` to check if special strings are available for your system

# Yearly Cron job
@yearly <command> # For yearly execution
@annually <command> # Same as above
0 0 1 1 * <command> # If above does not work for your system, use the regular one

# Monthly Cron job
@monthly <command> # For monthly execution
0 0 1 * * <command> # If above does not work for your system, use the regular one

# Weekly Cron job
@weekly <command> # For weekly execution
0 0 * * 0 <command> # If above does not work for your system, use the regular one

# Daily or every 12am Cron job
@daily <command> # For daily execution
@midnight <command> # Same as above
0 0 * * * <command> # If above does not work for your system, use the regular one

# Hourly Cron job
@hourly <command> # For hourly execution
0 * * * * <command> # If above does not work for your system, use the regular one

# Trigger once at startup
@reboot <command>
```