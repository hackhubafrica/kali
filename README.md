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

  

