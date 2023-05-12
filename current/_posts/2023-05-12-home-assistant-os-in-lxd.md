---
author: Sean Blanchfield
date: 2023-05-12 15:00
layout: post
link: https://seanblanchfield.com/home-assistant-os-in-lxd
slug: home-assistant-os-in-lxd
title: How to Run Home Assistant OS under LXD
image: /images/2023/05/home-assistant-os-in-lxd.jpeg

tags:
- Technology
- Web
- Home Assistant
---

I recently set up an Intel NUC as new home server, ended up hosting a wide range of services on it in containers or VMs. I initially tried using Proxmox to achieve this, but have found LXD running on top of Debian to be vastly preferable.

Getting Home Assistant OS running inside LXD wasn't well documented, so here's how I did it.

<!-- more -->
---

Acknowledgements to:
 - [Daniel on the HA forums](https://community.home-assistant.io/t/running-hassos-as-an-lxd-lxc-virtual-machine/227643/17)
 - [xiki and stgraber on the LXD forums](https://discuss.linuxcontainers.org/t/vm-from-disk-image/11473/19)

 Prerequisites:
 - Have bridge networking set up so that you can access your LXD containers and VMs directly over your network.

## Instructions to run Home Assistant OS under LXD
``` bash
# make a directory to work from
mkdir haos
cd haos/
# download the KVM image
wget https://github.com/home-assistant/operating-system/releases/download/10.1/haos_ova-10.1.qcow2.xz
# extract it
xz -d haos_ova-10.1.qcow2.xz
# make a `metadata.yaml` file and compress it
cat << EOF > metadata.yaml 
architecture: x86_64
creation_date: 1624888256
properties:
  description: Home Assistant image
  os: Debian
  release: buster 10.10
EOF
tar -cvzf metadata.tar.gz metadata.yaml
# import both the KVM image and the metadata file as a new image called "haos"
lxc image import metadata.tar.gz haos_ova-10.1.qcow2 --alias haos
# launch it as a VM
lxc launch haos ha --vm -c security.secureboot=false -d root,size=32GiB
# Set VM limits per advice at https://www.home-assistant.io/installation/linux
lxc stop ha
lxc config set ha limits.cpu=2 limits.memory=2GiB
lxc start ha
```

At this point, Home Assistant started up normally. 

![New VM in the LXDWare Dashboard](/images/2023/05/HA_in_LXDWare_dashboard.png){: .captioned}

![Home Assistant's startup screen](/images/2023/05/HA_in_LXD.png){: .captioned}


## USB devices

I haven't yet tried to pass any USB devices through to HA. I believe the tutorial on the [LXD forums here](https://discuss.linuxcontainers.org/t/usb-passthrough-on-ubuntu-based-vms/12170
) will be a good starting point for that.  With luck a command like the following will be all that is required:

``` bash
# Find `vendorid` and `productid` with `lsusb` on the host.
lxc config device add ha myusbdevice usb vendorid=058f productid=6387

```


## Background Setup

My NUC is running Debian 11 (Bulleye), and has Docker and LXD installed. This allows me to run Docker containers, LXC containers as well as virtual machines. There is nothing else to speak of running on the host machine.

To make life easier, I have Portainer running in Docker, which I can use to easily manage other Docker containers. 

After reviewing various web UIs for LXD, I selected [LXD Dashboard](https://lxdware.com/). I have it running as a Docker container, configured from inside of Portainer with a `docker-compose.yaml` as follows:

```yaml
version: '3'
services:
  LXD-Dashboard:
    privileged: true
    restart: on-failure

    image: lxdware/dashboard:latest
    ports:
      - "8080:80"
    volumes:
      - "/configs/lxddashboard/lxdware:/var/lxdware:rw"
```

This allows me to easily manage containers and VMs running in LXD. 

## Server overview (LXD and Docker)
Right now, here is everything that is being hosted:
* Docker
  * Portainer (for managing docker containers)
  * LXD Dashboard (for managing LXD containers/VMs)
  * Frigate
  * Nginx (a local Nginx serving a static page with links to all local services)
* LXD VMs
  * Windows 10 (on demand, and available over remote desktop)
  * Home Assistant OS (as a backup to my Home Assistant Blue)
* LXD/LXC containers
  * NAS (SMB server on top of Debian, which is also configured to perform backups)
  * PiHole (local DNS server on top of Debian)
  * Wireguard (VPN server on top of Debian)
  * Zabbix (system monitoring server on top of Debian)
