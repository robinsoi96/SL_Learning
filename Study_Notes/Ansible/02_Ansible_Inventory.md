# Ansible Inventory

Ansible inventory is a file or script written on control node to **specify a list of managed hosts to communicate with to run automation tasks**.

By default, the location of inventory file is `/etc/ansible/hosts`.

- However, usually, we won't use `/etc/ansible/hosts` as our inventory file
- Inventory file source can be specified using `-i` option in the command line or by editing the configuration system `ansible.cfg`

## Ansible Inventory File Formats

Ansible inventory files can be written in `INI` or `YAML` format.

### `INI` Format

Usually used for **simple inventories with few variables**

1) With typical simple syntax:

    ```ini
    <ungrouped_managed_host>

    [<group_name_1>]
    <group_1_managed_host>

    [<group_name_2>]
    <group_2_managed_host>
    ```

    - Every grouped managed host is written under its respective `[<group_name>]`
    - If the managed host is not to be grouped or belong to `ungrouped` group, then the mentioned host will not need to have dedicated `[<group_name>]` above it
    - **NOTE:** All mentioned hosts are under `all` group to indicate all managed hosts mentioned

2) Parent/Child group relationships:

    ```ini
    [<parent_group>:children]
    <child_group>
    ```

    - Use `:children` suffix to define a parent group that contains other child group(s)

3) Assigning host variables and group variables:

    - Assign host variables:
        ```ini
        [<group_name>]
        <managed_host> <host_variable_key_1>=<host_variable_value_1> <host_variable_key_2>=<host_variable_value_2>
        ```
        - Written in 1 line to assign host variable with managed host defined
    
    - Assign group variables:
        ```ini
        [<group_name>:vars]
        <group_variable_key_1>=<group_variable_value_1>
        <group_variable_key_2>=<group_variable_value_2>
        ```
        - `:vars` indicates section for group variables, but note that each group variable per line
    
    - Host variable will always take precedence and override the group variable

### `YAML` Format

Used for **complex configurations, nested groups, and dynamic inventories that require complex data structures like lists or directonaries**

1) With typical simple syntax:

    ```yaml
    all:
        ungrouped:
            hosts:
                <ungrouped_managed_host>:
        <group_name_1>:
            hosts:
                <group_1_managed_host>:
        <group_name_2>:
            hosts:
                <group_2_managed_host>:
    ```

    - `all:` is optional to be written, but better to include to indicate a list of all managed hosts
    - `ungrouped:` is to group managed hosts which are not belong to any group mentioned
    - **Things to take note:**
        - `hosts:` is required to be written below respective group name to allow listing of managed hosts within respective group
        - When writing the managed host, `:` is required to add behind it

2) Parent/Child group relationships:

    ```yaml
    <parent_group>:
        children:
            <child_group>:
    ```

    - Use `children:` entry to nest child group(s) under a parent group
    - **EXTRAS:** `all:` is also considered a group, so you can use `children:` entry in YAML file as sample below:
        ```yaml
        all:
            children:
                <parent_group>:
                    children:
                        <child_group>:
        ```

3) Assigning host variables and group variables:

    - Assign host variables:
        ```yaml
        <group_name>:
            hosts:
                <managed_host>:
                    <host_variable_key_1>: <host_variable_value_1>
                    <host_variable_key_2>: <host_variable_value_2>
        ```
        - Host variables are written under managed host section
    
    - Assign group variables:
        ```yaml
        <group_name>: 
            vars:
                <group_variable_key_1>: <group_variable_value_1>
                <group_variable_key_2>: <group_variable_value_2>
        ```
        - Use `vars:` entry to nest all group variables under the group
    
    - Host variable will always take precedence and override the group variable

## Appendix

Reference link:

- [Building Ansible inventories](https://docs.ansible.com/projects/ansible/latest/inventory_guide/index.html)