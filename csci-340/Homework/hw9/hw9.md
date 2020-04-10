I am running Ubuntu 18.04 directly from an Acer laptop, not in an virtual environment. As such, I have no virtual devices- only physical.

## 1. Device Information

### a) Program lsblk

***lsblk*** stands for "List Blocks". It gives information about different block devices

| Column name | Description |
|-|-|
| NAME | unique device name
| MAJ | major device number; typically refers to a driver
| MIN | minor device number; usually a distinct instance of a driver
| RM | flag stating whether a device is removable
| SIZE | size of the device
| RO | flag stating whether a device is read-only
| TYPE | device type
| MOUNTPOINT | where the device is mounted in the linux filesystem

- There are many different device types, including drive, partition, loop device, multi-devices (like RAID), and device mappers (lvm). Some of these I recognize. Others are new, like device mappers.
- From a Windows-user perspective, the mount point is a very strange concept. In Windows, all storage devices are mounted from a root position and have their own file systems, barring symlinks (C:\, D:\, X:\, etc.). Seeing storage devices share the same filesystem was very confusing at first.

```
NAME                  MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
loop0                   7:0    0 120.4M  1 loop /snap/docker/423
loop1                   7:1    0  14.8M  1 loop /snap/gnome-characters/399
loop2                   7:2    0  91.4M  1 loop /snap/core/8689
loop3                   7:3    0   4.3M  1 loop /snap/gnome-calculator/704
loop4                   7:4    0   3.7M  1 loop /snap/gnome-system-monitor/135
loop5                   7:5    0   3.7M  1 loop /snap/gnome-system-monitor/127
loop6                   7:6    0  14.8M  1 loop /snap/gnome-characters/495
loop7                   7:7    0    55M  1 loop /snap/core18/1705
loop8                   7:8    0  57.3M  1 loop /snap/discord/109
loop9                   7:9    0   956K  1 loop /snap/gnome-logs/81
loop10                  7:10   0  52.7M  1 loop /snap/john-the-ripper/297
loop11                  7:11   0   956K  1 loop /snap/gnome-logs/93
loop12                  7:12   0 142.8M  1 loop /snap/code/28
loop13                  7:13   0 156.7M  1 loop /snap/gnome-3-28-1804/110
loop14                  7:14   0 160.2M  1 loop /snap/gnome-3-28-1804/116
loop15                  7:15   0 140.7M  1 loop /snap/gnome-3-26-1604/98
loop16                  7:16   0 142.3M  1 loop /snap/slack/21
loop17                  7:17   0  93.8M  1 loop /snap/core/8935
loop18                  7:18   0  58.9M  1 loop /snap/discord/108
loop19                  7:19   0 142.7M  1 loop /snap/code/26
loop20                  7:20   0  54.7M  1 loop /snap/core18/1668
loop21                  7:21   0  48.3M  1 loop /snap/gtk-common-themes/1474
loop22                  7:22   0   4.2M  1 loop /snap/gnome-calculator/544
loop23                  7:23   0 142.2M  1 loop /snap/slack/22
loop24                  7:24   0  44.9M  1 loop /snap/gtk-common-themes/1440
sda                     8:0    0 119.2G  0 disk 
├─sda1                  8:1    0   512M  0 part /boot/efi
└─sda2                  8:2    0 118.8G  0 part 
  ├─ubuntu--vg-root   253:0    0 117.8G  0 lvm  /
  └─ubuntu--vg-swap_1 253:1    0   980M  0 lvm  [SWAP]
```

Curiously, this command fails to run in a WSL environment, since it does not expose block devices in /sys/dev/block.

### b) Program lsusb

***lsusb*** stands for "List USB devices". It gives information about different USB buses and devices connected to them.

| Column name | Description |
|-|-|
| Bus # | bus number a device is connected to
| Device # | device number; specific to bus
| ID # | device ID
| Name | name of the device

- Each bus may support multiple devices. Device numbers are specific to the bus it is connected to.
- Device 001 seems to be the root hub of each bus. I don't know the significance of this.
- Device ID is broken down into vendor ID : product ID. These numbers are defined by the USB Implementers Forum.

```
Bus 001 Device 004: ID 0408:a031 Quanta Computer, Inc. 
Bus 001 Device 003: ID 04ca:3015 Lite-On Technology Corp. 
Bus 001 Device 002: ID 0438:7900 Advanced Micro Devices, Inc. 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 003 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

<br/>

## 2. Storage Nomenclature

1. A ***Host Bus Adapter*** seems to refer to adapter cards which use PCIe (or another expansion standard) to allow a host computer to have additional buses, be them USB, SATA storage, or network cards. USB and SATA cards are used to give a computer additional storage or I/O points. Network cards allow for additional, or perhaps faster, network adapters. Other HBA types exist, like sound cards, but are not as frequently used.
2. ***SATA*** stands for Serial AT Aattachment (where AT is Advanced Technology, taken from IBM PC/AT back in the late 80's). This is a standardized bus that connects a host computer to storage devices, drives, etc. SATA is an evolution of the ATA standard, and SATA itself has seen several revisions over the years. Most computers today use some version of SATA for its storage bus.
3. ***Fiber Channel*** (*Fibre*?) is a formm of data transfer that usually runs over fiber optics, and is considered very fast today, achieving up to 128Gb/s. Several different protols are built on fiber channel, including (unsurprisingly) Fiber Channel Protocol (FBC). Fiber channel requires a dedicated connection between devices, and it not compatible with other protocols, such as IP.
4. ***iSCSi*** stands for Internet Small Computer Systems Interface. Wikipedia calls it an IP-based standard that allows block-level access to other devices over Local or Wide Area Networks. If I understand correctly, this means it effectively lets one device actively access, read, and write files onto another device on the same network. Compared to fiber channel, iSCSi is much more easier to implement.
5. A ***Storage Area Network*** (SAN) is a specialized network dedicated to storage servers. It effectively combines a larger array of storage nodes in such a way that any server accessing them sees the data as locally attached, by providing block-level access, through the use of an interconnect such as Fiber Channel or iSCSi. SANs are very scalable, but require their own dedicated network hardware, which makes them relatively expensive.
6. ***Network Attached Storage*** (NAS) is an alternative to SAN, typically implemented as a specialiized computer dedicated to nothing but data storage. NAS devices have extra space for storage devices and often use redundancy technology like RAID. They exist on a normal LAN instead of in their own dedicated nework, so are relatively easy to deploy when compared to SAN.