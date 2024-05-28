 # SYSTEM INFORMATION
To determine which version of Debian you are using, you can check the contents of certain system files or use specific commands. Here are a few methods to find out the Debian version:

Method 1: Using lsb_release Command

The lsb_release command provides LSB (Linux Standard Base) and distribution-specific information.


    lsb_release -a

Method 2: Checking /etc/os-release

The /etc/os-release file contains operating system identification data.

    cat /etc/os-release

Method 3: Checking /etc/debian_version

The /etc/debian_version file contains the version of Debian.

    cat /etc/debian_version

Method 4: Using hostnamectl Command

The hostnamectl command is part of systemd and provides system information.

    hostnamectl

Method 5: Using dpkg Command

You can use dpkg to query the version of the base-files package, which provides the base system.

    dpkg-query -W -f='${Version}\n' base-files

Example Outputs and Interpretations

    lsb_release -a 


Distributor ID: Debian
Description:    Debian GNU/Linux 10 (buster)
Release:        10
Codename:       buster

     cat /etc/os-release 


PRETTY_NAME="Debian GNU/Linux 10 (buster)"
NAME="Debian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
VERSION_CODENAME=buster
ID=debian

    cat /etc/debian_version 

kali-rolling

    hostnamectl 


Static hostname: debian
Icon name: computer-vm
Chassis: vm
Operating System: Debian GNU/Linux 10 (buster)
Kernel: Linux 4.19.0-14-amd64
Architecture: x86-64

  


# GRUB-CONFIGURATION
Step 1 :Create a bootable USB

First of all, you need to download the latest ISO file from our website.
Then you can burn it using Balena Etcher or ROSA ImageWriter. They both work on GNU/Linux, Mac OS and Windows. We strongly recommend to use Etcher, but you can also use the DD command line tool if you prefer it.
Step 2 - Disk and partition identification
Once you entered the live mode, open terminal and type

    sudo fdisk -l

The output should be similar to this. /dev/sda is usually the first SSD or HDD. If you have an NVMe M.2, the disk will be named /dev/nvme0n1.

/dev/sda1 usually is the EFI partition, used for booting the OS in UEFI systems.
/dev/sda2 is Linux partition.

Step 3 - Create the mount folder
A mount folder is needed to perform this operation. So, in the same terminal window, type:
        
    mkdir /mnt/boot
Step 4 - Mount Partitions
Now it's time to mount the partitions. In the same terminal window, type
    
    
    sudo mount /dev/sda2 /mnt

For ParrotOS default filesystem is btrfs and it has subvolumes enabled. In the same terminal window, type;
    
    sudo mount -o subvol=@ /dev/sda2 /mnt

Mount the dev, proc, sys folders and the EFI partion in order to get access to the system.

In the same terminal window, type

    sudo mount --bind /dev /mnt/dev

    sudo mount --bind /proc /mnt/proc

    sudo mount --bind /sys /mnt/sys

    sudo mount /dev/sda1 /mnt/boot/efi

Step 5 - Chrooting and installing GRUB
Time to enter the system. In the same terminal window, type

    sudo chroot /mnt

Once in chroot environment, type

    grub-install /dev/sda
After the installation is finished, type exit so as to exit the chroot environment.

Step 6 - Unmounting partitions and rebooting system
After exiting the chroot environment, unmount all of the partitions and folders used. In the same terminal window type:

     sudo umount /mnt/dev

    sudo umount /mnt/proc

    sudo umount /mnt/sys

    sudo umount /mnt/boot/efi

    sudo umount /mnt



