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

## Appendix

Reference link:

- [Building Ansible inventories](https://docs.ansible.com/projects/ansible/latest/inventory_guide/index.html)