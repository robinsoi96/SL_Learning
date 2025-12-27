# Linux Boot Processes

## Stages of Linux Boot Process

<img src="./images/Linux_Boot_Process.png" alt="Summarized Linux Boot Processes">

### BIOS / UEFI

Difference between BIOS and UEFI:

- `BIOS` = Basic Input/Output System (**Older Firmware**)
- `UEFI` = Unified Extensible Firmware Interface (**Modern Replacement**)
- Key Differences:
    1) Interface & Control:
        - BIOS : Text-based, keyboard-only interface, older-style menus
        - UEFI : Graphical, mouse-supported interface, more user-friendly
    2) Boot Speed:
        - BIOS : Slower, sequential hardware initialization
        - UEFI : Faster, can initialize hardware in parallel, optimized for SSDs
    3) Security:
        - BIOS : Lacks inherent security features, vulnerable to malware
        - UEFI : Includes Secure Boot, verifying digital signatures to block malicious code
    4) Disk & Partition Support:
        - BIOS : Uses MBR, limited to 2TB drives and 4 primary partitions
        - UEFI : Uses GPT, support massive drives (exabytes) and up to 128 partitions
    5) Processor Mode:
        - BIOS : 16-bit mode
        - UEFI : 32-bit or 64-bit mode, allowing more modern operations
    6) Boot Process:
        - BIOS : Boots from the Master Boot Record (MBR) sector
        - UEFI : Boots from .efi files stored on an EFI System Partition (ESP)
- Now, most systems are using UEFI, eventhough some people may call it as "BIOS" for simplicity

BIOS/UEFI is a special type firmware used in the booting process, and it is the **first piece of software that is run when a computer is powered on**.

- It is operating system independent, meaning it is not unique to the Linux OS

The primary purpose of BIOS/UEFI is to **find and execute the bootloader**

- BIOS/UEFI will try to find and set up connected storage devices while looking for media files that can be used to boot the computer.
    - In legacy BIOS systems, the partition scheme used to locate the operating system files is called Master Boot Record (MBR), which has a limitation of 2TB disks
    - In modern UEFI systems, it is done through EFI partition and GPT (GUID Partition Table) on bigger drives (>2TB)

- BIOS will look into the MBR on the first storage device to find the bootloader (like GRUB)

- UEFI does not go through the MBR but rather goes directly to the bootloader location in the EFI System Partition (ESP)
    - It can find the bootloaders on a certain predefined folder path (/EFI/)

BIOS/UEFI performs a `POST (Power-On Self-Test)` to perform **basic device check** on the most important hardware components which includes the RAM, CPU, and storage devices (HDD, SSD, and USB).

- If something goes wrong (e.g. broken GPU), POST will abort the booting process and signal the user with a series of beeps or error codes
- If POST succeed, it will proceed to the bootloader

BIOS/UEFI knows about the bootable devices, and the boot device search order can be changed by entering the configuration for the BIOS/UEFI.

- The key to enter BIOS/UEFI configuration will vary from one hardware manufacturer to another

### Bootloader

A bootloader is a crucial compoenet in the Linux boot process that **initializes the system by loading Linux kernel and passing necessary boot parameters**.

- It is the first software that runs once the system's BIOS/UEFI firmware completes the Power-On Self-Test (POST) and finds a bootable disk

Tasks of bootloader:

- Select from multiple kernels
- Switch between sets of kernel parameters
- Provide support for booting different operating systems
- Load initrd/initramfs to prepare the system before mounting the root filesystem
- Pass kernel arguments such as ro (read-only root), quiet (disable verbose boot messages), nomodeset (disable graphics drivers for troubleshooting)
- Recover from boot failures by providing a minimal recovery shell in case of errors (GRUB rescue mode)

Bootloader in Linux:

- `GRUB` (Grand Unified Boot Loader) - A near-universal normal on Linux systems, with BIOS/MBR and UEFI versions
- `LILO` (Linux LOader) - One of the primary Linux bootloaders. ELILO could be a UEFI version
- `SYSLINUX` - It may be organized to run from many alternative styles of filesystems
- `LOADLIN` - Boots a kernel from DOS
- `System-boot` - A straightforward UEFI boot manager
- `coreboot` - A superior replacement for the computer BIOS which will embody a kernel
- `Linux Kernel EFISTUB` - A kernel plug-in for loading the kernel directly from associate EFI/UEFI System Partition
- `EFI Linux` - A UEFI boot loader meant to function as a model and reference for different UEFI boot loaders

### Linux Kernel

Once the bootloader (e.g. GRUB, LILO or SYSLINUX) loads the Linux kernel into memory (RAM), the kernel initialization process begins.

The Linux kernel is **responsible for hardware detection, memory management, device driver loading, and starting system services**.

- Kernel Initialization and Boot Options:

    1) CPU examination
    2) Memory examination
    3) Device bus discovery
    4) Device discovery
    5) Auxiliary kernel system setup
    6) Root filesystem mount
    7) User-space begin

- When the Linux kernel starts, it receives a group of text-based kernel parameters containing some further system details.

    - Common Kernel Boot Parameters:
        - ro (Read-Only Mode)
        - rw (Read-Write Mode)
        - quiet
        - splash
        - nomodeset
        - init=/bin/bash
        - noapic / nolapic
        - maxcpus=1
        - pci=noacpi
        - fsck.mode=force
        - loglevel=3
    
    - For Offical Linux Kernel Parameters, can refer to this [documentation](https://docs.kernel.org/admin-guide/kernel-parameters.html)
    
    - The kernel parameters can be modified temporarily or permenantly

        - **Temporarily**

            1) Reboot your system and wait for the GRUB menu to appear (you might need to press `Esc` or `Left-Shift` if it doesn't show automatically)

            2) Highlight the desired kernel entry and press `E` key to edit

            3) Locate the line starting with `linux`(or `linuexefi`) and move the cursor to the end of the line

            4) Add your parameters, ensuring a space before each new parameter and no spaces around `=` sign

            5) Press `Ctrl+x` or `F10` to boot the system with the modified parameters

        - **Permanently**

            1) Edit GRUB configuration file (typically `/etc/default/grub`) with root privileges

            2) Find the line that starts with `GRUB_CMDLINE_LINUX_DEFAULT` or `GRUB_CMBLINE_LINUX` and add your desired parameters insides the double quotes

            3) Save and exit the editor

            4) Update the GRUB configuration to apply the changes
                - **Ubuntu/Debian:** `sudo update-grub`
                - **RHEL/SUSE/Fedora:** `sudo grub2-mkconfig -o /boot/grub2/grub.cfg` (or use `grubby` utility)
            
            5) Reboot the system for the changes to take effect
        
        - After booting, can verify the current active kernel parameters by running `cat /proc/cmdline`

Before mounting the actual root filesystem, the Linux kernel loads an initial, temporary filesystem called initrd or initramfs.

- `initrd` (Initial RAM Disk) – A compressed block-based filesystem that includes essential drivers and utilities needed for booting.

- `initramfs` (Initial RAM Filesystem) – A modern replacement for initrd, it is a cpio archive that does not require mounting and loads directly into RAM.

Kernel ring buffer contains messages from the Linux kernel

- Use `dmesg` command 
- Check logs in `/var/log/dmesg`

**EXTRAS:**
- All files required to boot the Linux system are stored in `/boot` folder
- The linux kernel is typically named `vmlinux` or `vmlinuz`(if compressed)

### Init / Systemd

When the kernel is initialized, he subsequent Linux boot process action progresses into the init system, which handles system services, processes, and sessions. 

- The init system **takes care of provisioning all required background services such as networking, logging, and the system daemons in the right sequence**.

2 major types of Init Systems in Linux:

1) **SysVinit** (System V Init)

    - The oldest Linux distributions have this init system as a component
    - Administers `runlevels (0-6) using /etc/inittab` [NOTE: runlevels can be configured differently across different distros, so please check for more on the Internet]
    - Sequential startup: Each service is started on its own, which increases boot time
    - In widespread use with older distros like RHEL 5, CentOS 5, Debian 6

2) **systemd** (Modern Standard in Linux Boot Process)

    - Default init system in many distributions today like RHEL, Ubuntu, Debian, Fedora
    -   Parallel service startup (improves performance compared to SysVinit)
    - `Uses targets instead of traditional runlevels`
    - Manages cgroups (Control Groups) enabling better resource control

**Generic Runlevels in `SysVinit`**:

| Runlevel | Description |
|:---:|---|
| 0 | Halt/Shutdown the system |
| 1 | Single-User Mode (Maintenance), root only, no networking, great for recovery |
| 2 | Multi-User Mode (no network/GUI) |
| 3 | Full Multi-User Mode with Networking (CLI/Text-based) |
| 4 | Unused/Customizable (can be defined by admin) |
| 5 | Multi-User Mode with Graphical Interface (GUI), common default |
| 6 | Reboot the system |

- NOTE: DIfferent distros may have each runlevel defined differently

- `/etc/inittab` file is used to set the default run level for the system by setting the runlevel number on the `initdefault` line

- Run the command `telinit <RUNLEVEL_NUMBER>` with root privilege to execute the system's runlevel

    - Value options for `<RUNLEVEL_NUMBER>`:
        - `0` : Halt or power off the system
        - `1`/`S`/`s` : Switch to single-user (maintenance/rescue) mode
        - `2`,`3`,`4`,`5` : Switch to the specified multi-user runlevel. These are typically used for specific system configurations (e.g., runlevel 3 is often multi-user text mode, 5 is multi-user graphical mode).
        - `6` : Reboot the system
        - `q`/`Q` : Tell the `init` process to re-examine the `/etc/inittab` file for changes (**applicable to older systems using SysVinit**)

- The applications that are started by init are located in the `/etc/rc.d` folder
    - Within this directory there is a separate folder for each run level, eg `rc0.d`, `rc1.d`, ..., `rc6.d`.

**System Targets in `systemd`**:

- Check all available system targets in `/lib/systemd/system`

- Run command `systemctl set-default <SYSTEM_TARGET>` to set the default system target

    -   Optionally, you can create a symlink to the desired target from `/etc/systemd/system/default.target`

- Run command `systemctl isolate <SYSTEM_TARGET>` to execute the system target

- Run command `systemctl cat <SYSTEM_TARGET>` to check detailed information on a specific target

- Commands to check system targets:
    - `systemctl list-units --type=target` : Lists **all currently active targets** on the system
    - `systemctl list-units --type=target --all` : Lists **all installed targets, including both active and inactive ones**. This is generally the most comprehensive way to see all possible targets.
    - `systemctl list-unit-files --type=target --all` : Lists **all target unit files and their enable/disable status**, which can sometimes show even more targets than `list-units`
    - `systemctl get-default` : Shows the **default target that the system boots into**

## Two Types of Booting

### Cold or Hard Booting

Cold booting refers to the state in which a **computer is switched on after being completely powered off**.

During this process, the system performs a full power-on self-test (POST), initializes hardware devices, and loads the operating system from storage into RAM.

### Soft or Warm Booting

Warm booting, also known as a soft boot or restart, **reboots a computer system without completely shutting it down and is usually triggered through an OS restart command or a key combination**.

It skips some hardware initialization steps since the components are already powered and initialized, offering a quicker restart compared to a full cold boot.

## `shutdown` Command

**NOTE:** `shutdown` command is executed in root privilege

Generic syntax of `shutdown` command:

```
shutdown <options> <time> "<message>"
```

- `<options>` available:
    - `-h` : Halt the system after shutting down all process
    - `-P` : Powers off the machine completely after shutdown (this is the default behavior on most modern systems)
    - `-r` : Reboots the system after it has been brought down
    - `-c` : Cancels a scheduled shutdown; Usage: `shutdown -c`

- `<time>` options:
    - `now` : Right now
    - `+<NUM>` : To be done in `<NUM>` minutes
    - `HH:MM` : To be done at `HH:MM` in 24 hour format

- `<message>`: 
    - Custom message to broadcast to all logged-in users
    - `<time>` argument is required to be specified

- **EXTRAS:**
    - `shutdown -P now` comamnd == `poweroff` command
    - `shutdown -r now` command == `reboot` command

## What is Dual Booting?

**When a computer has two or more operating systems installed in a single computer**, it is known as dual booting.

Comparison between booting and dual booting

| Parameter | Booting (Single Booting) | Dual Booting |
|:---:|---|---|
| Definition | The process of starting up a computer  | The process of installing and running multiple operating systems on a single computer |
| Purpose | Loads the operating system into memory and initializes the computer  | Allows users to choose between different operating systems at startup |
| OS | Only one operating system is installed and runs on the computer | Multiple operating systems are installed on different partitions or drives |
| Configuration | The computer is configured to boot directly into the installed operating system | The computer is configured with a boot loader to choose between different operating systems |
| Setup Complexity | Relatively simpler, as there is only one operating system to configure  | Requires additional setup and configuration to manage multiple operating systems |
| Resource Utilization | Utilizes the full resources of the computer for a single operating system  | Resources are divided among the installed operating systems, potentially affecting performance |

## Appendix

Reference links:

- <a href="https://www.geeksforgeeks.org/linux-unix/how-linux-kernel-boots/">How Linux Kernel Boots?</a>
- <a href="https://www.geeksforgeeks.org/operating-systems/booting-and-dual-booting-of-operating-system/">Booting and Dual Booting of Operating System</a>