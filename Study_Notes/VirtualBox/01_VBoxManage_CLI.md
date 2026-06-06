# VBoxManage CLI

Before proceed to basic commands for `VBoxManage` CLI, a few things to mention as below:

- Click this [link](https://www.virtualbox.org/wiki/Downloads) to check on `VirtualBox` main documentation page and download
- Click this [link](https://www.virtualbox.org/manual/ch08.html) for official documentation of `VBoxManage` CLI

## Basic Commands

### Create new VM

`VBoxManage createvm` is the CLI to create VM.

Basic CLI sample:

```shell
VBoxManage createvm --name=<VM_name> --register
```

- `--register` : To register the VM. Run `VBoxManage registervm` if this option is not included