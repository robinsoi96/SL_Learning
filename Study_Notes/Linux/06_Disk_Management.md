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

## Swap Space

Swap space is a **dedicated area on a disk (partition or file) used as virtual memory**, extending your system's RAM by temporarily storing inactive data from RAM when the physical memory runs low.

### How Swap Space Works?

1) When physical memory (RAM) is full, the OS selects some memory pages that are inactive or least recently used (using algorithms like LRU &mdash; Least Recently Used)
2) These pages are written from RAM to the swap space on the disk
3) When those pages are needed again, they are read back from the swap space into RAM
4) This process of moving pages between RAM and disk is called swapping or paging

**NOTE:**
- Despite its usefulness, accessing swap space is much slower than RAM due to disk I/O delays
- OS combines RAM and swap space to create a larger virtual memory pool

### Preparing Swap Space in Linux

You can use `mkswap` command to crete the swap space.

```shell
mkswap /<swap_space_file_path>
```

To enable the swap partition, run this command : `swapon /<swap_space_file_path>`.

Run `swapon -s` to see the swap devices in use.

Use `swapoff` command to deactivate swap space.
- `swapoff /<swap_space_file_path>` : Disable specific swap partition or file
- `swapoff -a` : Disable all currently active swap spaces

## `/etc/fstab` &mdash; The File System Table

The `/etc/fstab` (filesystem table) file is a critical system configuration file in Linux that **stores information about available disks and partitions, defining how they should be automatically mounted when the system boots up**.

Each entry or line of the file is made up of 6 fields (separated by space or tab):
1) device
2) mount point
3) file system type
4) mount options
5) dump
6) fsck (file system check) order

More information on `/etc/fstab` entries, can refer to below links:
- [fstab(5) — Linux manual page](https://man7.org/linux/man-pages/man5/fstab.5.html)
- [Understanding /etc/fstab](https://www.geeksforgeeks.org/linux-unix/understanding-etc-fstab/)
- [An introduction to the Linux /etc/fstab file](https://www.redhat.com/en/blog/etc-fstab)
- [The /etc/fstab file on Linux Explained](https://www.computernetworkingnotes.com/linux-tutorials/the-etc-fstab-file-on-linux-explained.html)

## `blkid` Command

`blkid` command is a powerful utility used to **identify and display attributes of block devices**, such as hard drives, SSDs, and USB drives.

The command provides crucial metadata attributes (tokens) stored within the device's content metadata, inclduing:
- **`UUID`(Universally Unqiue Identifier)** : A unique 128-bit identifier for the device or partition
- **`TYPE`** : The filesystem type (e.g. `ext4`, `swap`, etc)
- **`LABEL`** : A human-readable label if one has been assigned to the partition
- **`PARTUUID`** : A unique identifier for the partition itself

## `lsblk` Command

1) `lsblk` : Show information of block devices

    - The information shown are:

        - `NAME` : Device name
        - `MAJ` : Corresponding major device number
        - `MIN` : Corresponding minor device number
        - `RM` : Whether the device is removable [**1 = removable**]
        - `SIZE` : Size of device
        - `RO` : Whether the device is read only [**1 = read only**]
        - `TYPE` : Type of device
        - `MOUNT` : Device's mount point

2) `lsblk -a` : Show information of all block devices including the empty ones

3) `lsblk -b` : Same as `lsblk`, but display the exact number of bytes for the size of device

4) `lsblk -z` : Print zone model of block devices

5) `lsblk -d` : Show information of block devices without slave entries

6) `lsblk -i` : Make `lsblk` use ASCII characters for tree formatting

7) `lsblk -m` : Display informatin about devices' owner, group and mode

8) `lsblk -f` : Provides more advanced information specially about the data inside the partitions

    - The information shown are:

        - `NAME` : Device name
        - `FSTYPE` : The type of filesystem (e.g. `ext4`, `xfs`, `vfat`)
        - `LABEL` : The volume label assigned to partition
        - `UUID` : Universally Unique Identifier
        - `FSAVAIL` : Available space in the filesystem
        - `FSUSE%` : Percentage of space used
        - `MOUNTPOINT` : Device's mount point

9) `lsblk -o <Column(s)_to_display>` : 

    - Print all information columns mentioned for block devices
    - `,` as delimiter for different columns
    - Common columns can be `NAME`, `MAJ:MIN`, `FSTYPE`, etc

## Labelling a file system

Use `e2label` command to label a file system

```shell
e2label /<device_path_name> "<label>"

e2label /<device_path_name> "" # If to clear a label
```