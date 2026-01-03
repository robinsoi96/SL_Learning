# Linux Disk Management

## Partitions

**Disks can be divided into parts, called `partitions`**.

Partition **allows you to allocate different section of the disk for different purposes**.

- As a system administrator, you can decide what partitioning scheme to use.

- Having seperate partitions is one way to prevent one part of the system from adversely affecting another part of the system.

### Most Common Partitioning Scheme in Linux

1) **`MBR` [Master Boot Record]**

    - Can only address  2TB of disk space
    - Allows up to 4 primary partitions
        - If you need more than 4 partitions, then 1 of the primary partition will be for you to create extended partitions
        - Extended partitions allows you to create unlimited logical partitions
    - Being phased out by GPT

2) **`GPT` [GUID (Global Unqiue Identifier) Partition Table]**

    - Replacing the MBR partition scheme
    - Part of the UEFI (Unified Extensible Firmware Interface) standard
        - UEFI is replacing the traditional BIOS, however, GPT has been used on some BIOS systems primarily due to disk size limitations of MBR partition tables
    - There are no primary and extended partitions with GPT
    - Supports up to 128 partitions
    - Supports up to 9.4 ZB disk sizes
    - Not supported by older operating systems
    - May require newer or special that supports GPT

### Mount Point

A mount point is simply a **directory used to access the data on a partition**.

- In Linux, `/` is always a mount point

    - Any additional partitions will be mounted on mount points below `/` in the directory tree
        - Sample explanation:
            - If you allocated a partition for home directory, then the partition will be mounted at `/home`
            - Any files or directories that are at or below the `/home` mount point will reside on that partition
            - For example, the file in the home directory `/home/username`, will be on the partition mounted at `/home`
            - If you disconnect or unmount that partition `/home` and mount it to another directory (mount point) `/export/home`, all the data will be available at the new mount point, and you will see `/export/home/username`
    
    - You can also mount partitions over existing data, but the files or directories created before it is mounted will not be accessible
        - Sample explanation:
            - You created a new directory `/home/username` before `/home` is mounted
            - When `/home` is mounted, you will not see `/home/username`
            - After the partition `/home` is unmounted, then you will be able to see `/home/username` again
    
    - Command to mount drives:

        ```shell
        mount <device_path_name> <mount_point>
        ```

    - Command to unmount drives:

        ```shell
        umount <device_path_name> # Option #1: Unmount the device

        umount <mount_point> # Option #2: Unmount the mount point
        ```

## `fdisk` Utility

You will most likely need to use a standard Linux tool to manipulate disks after the initial installation.

The `fdisk` utility has been traditionally used to create and modify partitions on a disk.

- There are also alternatives like `gdisk`, `parted`
- Earlier versions of `fdisk` did not support GPT, but the latest versions of `fdisk` support GPT

To manage the partitions on a disk with the `fdisk` utility, simply provide the device path you wish to manage as an argument to the command.

```shell
sudo fdisk <device_path_name>

# Once executed, you will see a command prompt
# Type `m` to understand the manual of fdisk command usage

# NOTE: you can utilize fdisk to create both MBR and GPT partitions
# You can always more using man command or search the internet
```

`fdisk` needs to be executed with root privileges
- `fdisk -l` : List all disks
- `fdisk -l <device_path_name>` : Lists the partition tables for the specified disk
- `man fdisk` : Check manual page of `fdisk` command
- `fdisk -h` : See the help message and listing of all options in `fdisk` command

## File Systems

Before a partition can be used by Linux system, it will need a file system.

The extended file system , or `ext` for short, was created specially for Linux.
- `ext2`, `ext3` and `ext4` are later releases.
- These series of file systems are the most commonly used file systems on Linux systems
- Often found as the default file systems on Linux distributions

- If you have special needs, you should research some of the other popular file systems available in Linux:
    - ReiserFS
    - JFS
    - XFS
    - ZFS
    - Btrfs

### Command to create file system

```shell
mkfs -t <File_System_Type> <device_path_name> # Option #1

mkfs.<File_System_Type> <device_path_name> # Option #2

# NOTE:
# You can run command `ls -l /sbin/mkfs*` to check all available file system types
```

### `ext4` VS `FAT32` VS `NFTS`

| File System | Supported File Size | Compatibility | Ideal Usage |
|---|:---:|:---:|:---:|
| FAT32 (`vfat` for Linux mkfs command) | up to 4 GB | Windows, Mac, Linux | For maximum compatibility |
| NTFS (`ntfs` for Linux mkfs command) | 16 EiB to 1 KB | Windows, Mac (read-only), most Linux distributions | For internal drives and Windows system file |
| ext4 (`ext4` for Linux mkfs command) | 16 GiB to 16 TiB | Windows & Mac (requires extra drivers to access), Linux | For files larger than 4GB |

## `mount` VS `df -h` Commands

- `mount` : List all devices currently mounted (not only show physical file systems, but also virtual (RAM based) file systems)
- `df -h` : Disk-free command, reports mounted file system usage

**EXTRAS:** 
- Manual mount (running `mount <device_path_name> <mount_point>` command) will not persist between reboots
- In order to make mounts persist beween reboots, add an entry in `/etc/fstab` file