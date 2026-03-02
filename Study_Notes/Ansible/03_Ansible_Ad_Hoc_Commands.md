# Ansible Ad Hoc Commands

Before proceed to [Ansible Playbooks](./04_Ansible_Playbook.md) which is in the next chapter, Ansible ad hoc commands uses `ansible` command line tool to **automate single task on one or more managed nodes**.

A few things to take note:

- Ad hoc commands are great for simple quick test
- Ad hoc commands are great for tasks you repeat rarely
- Ansible playbooks are preferrable for automation and more complex tasks, since it is declarative and repeatable

## Ansibe Ad Hoc Command Syntax

General syntax for `ansible` ad hoc command:

```shell
ansible <host_pattern> -i <inventory_file(s)> -m <module> -a "<module_arguments>" <other_options_if_applicable>
```

Options explanation:

1) `<host_pattern>` : Specifies the target host(s)
    - It can be: 
        - `all` for all managed hosts
        - any group name mentioned in inventory file
        - any host name mentioned in inventory file
        - any IP of the managed host

2) `-i <inventory_file>` : Specify the reference Ansible inventory file

3) `-m <module>` : Specify ansible module

4) `-a "<module_arguments>"` : Tell the arguments for the module specified in the command

5) `<other_options_if_applicable>` : Provide other options to the ad hoc command if needed
    - There are some commonly used other options as below:
        - `--become` : run the command with superuser privilege
            - `--ask-become-pass` or `-K` : will prompt for password to proceed with superuser privilege
        - `-u <username>` : connect the managed host as `<username>`