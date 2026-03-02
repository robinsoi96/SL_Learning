# Ansible Playbook

Ansible Playbook provides a **repeatable, reusable, simple configuration management and multimachine deployment system** that is well suited to deploying complex applications.

- Written in YAML file
- Consist an ordered list of one or more plays
    - Each play maps a group of hosts to a series of tasks, variables, and handlers to achieve a desired state

## Ansible Playbook Structure

Typical example of playbook structure with 1 play:

```yaml
- name: <Name of the play> # Define the name of play, e.g. Install Apache
  hosts: <group_name> # Specify the group name in inventory
  tasks: # An ordered list of tasks to be executed, below example runs tasks in sequence
    - name: <Description of task 1>
      <module_name_1>:
        <module_parameter>: <module_parameter_value>
    - name: <Description of task 2>
      <module_name_2>:
        <module_parameter>: <module_parameter_value>
```

- Here, you can write 2 or more plays in the same playbook. Just take note that each play triggered sequentially
- If want different plays to run in parallel, then write in different playbooks respectively