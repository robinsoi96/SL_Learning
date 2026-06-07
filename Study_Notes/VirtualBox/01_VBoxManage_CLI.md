# VBoxManage CLI

Before proceed to basic commands for `VBoxManage` CLI, a few things to mention as below:

- Click this [link](https://www.virtualbox.org/wiki/Downloads) to check on `VirtualBox` main documentation page and download
- Click this [link](https://www.virtualbox.org/manual/ch08.html) for official documentation of `VBoxManage` CLI

## Basic Commands

### Create new VM

`VBoxManage createvm` is the CLI to create VM.

Basic CLI sample:

```shell
VBoxManage createvm --name=<VM_name> --basefolder=<base_folder> --register
```

- `--register` : To register the VM. Run `VBoxManage registervm` if this option is not included
- `--basefolder` : For you to mention the base folder for the .vbox file
    - If you mentioned this option, the .vbox file path will be `<base_folder>/<VM_name>/<VM_name>.vbox`
    - Else, the .vbox file path will be `$HOME/VirtualBox VMs/<VM_name>/<VM_name>.vbox`

### Register VM

`VBoxManage registervm` is the CLI to register VM.

- However, if `--register` option is already included when running `VBoxManage createvm` command, can ignore this section

Basic CLI sample:

```shell
VBoxManage registervm <filename>
```

- `<filename>` : Provide the full .vbox file path for the VM created in `VBoxManage createvm`

### Unregister VM

`VBoxManage unregistervm` is the CLI to unregister the VM.

- **NOTE:** You must ensure that the VM is registered before you are able to run this command

Basic CLI sample:

```shell
VBoxManage unregistervm <UUID | VM_name>

# <UUID | VM_name> : Provide UUID or name of the VM registered
```

**Additional options:**

- `--delete` : Deletes the following files related to the VM automatically
    - All hard disk image files, including differencing files
    - All saved state files that the machine created, including one for each snapshot
    - XML VM machine definition file (in `.vbox` extension) and its backups
    - VM log files
    - The empty directory associated with the unregistered VM
- `--delete-all` : Deletes the files described in the `--delete` option, as well as all DVDs and Floppy disks located in the VM folder and attached only to this VM