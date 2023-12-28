---
author: Sean Blanchfield
date: 2023-05-12 15:00
layout: post
link: https://seanblanchfield.com/bridge-networking-in-lxd
slug: bridge-networking-in-lxd
title: How to Configure Bridge Networking in LXD
image: /images/2023/05/whale_v_firewall.jpeg

tags:
- Technology
- Web
- LXD
---

I am running Docker alongside LXD on my home server, and I want the various VMs and containers I am running to get their own IP addresses on my LAN and to be generally available for normal phones, laptops and other devices to connect to. 

This normally just requires LXD bridge networking (for which there are plenty of tutorials online), but it turns out that Docker interferes with it. Fixing it took a bit of research and experimentation. Here are details on what worked for me.

<!-- more -->
---

### Option 1: macvlan - easy to configure, but containers and host cannot communicate.
``` bash
lxc profile device set default eth0 parent eno1
lxc profile device set default eth0 nictype macvlan
```

### Option 2: (preferred) Set up bridge networking.

This has the benefit that not only do containers and VMs get their own real IP addesses on the LAN, but container-to-host networking also works. However, I found it a bit tricky to get working, because Docker inserts firewall rules that interfere with packet forwarding. 

First of all, you need to configure a bridge interface. Start off by installing `bridge-utils`:

``` bash
sudo apt-get install bridge-utils
```

In Debian and older versions of Ubuntu you need to add the details of your new bridge interface in the `/etc/network/interfaces` file (later versions of Ubuntu use `netplan` instead). There's plenty of [tutorials](https://medium.com/hackernoon/how-to-set-up-a-network-bridge-for-lxd-containers-98e3e7d1f273) on how to do this.

The modifications to `/etc/network/interfaces` include:
1. changing the mode of your normal interface to "manual", preventing it from starting automatically (in my case, `eno1`). 
1. Adding a new bridge interface (`br0` below). I chose to statically configure the IP address and gateway, but you could configure it with DHCP instead (as shown in most of the tutorials I saw).

Here's the modified `eno1` and new `br0` contents of my `/etc/network/interfaces`. 

``` text
# Bridge network interface for LXC/LXD
auto br0
iface br0 inet static
    address 10.0.0.2
    netmask 255.255.255.0
    gateway 10.0.0.1
    bridge-ifaces eno1
    bridge-ports eno1
    up ip link set eno1 up

# Set the original network interface to 'manual'
iface eno1 inet manual
```

Make this take effect by restarting networking. It's a good idea to make sure you can connect a monitor and keyboard to your box to fix things if you make a mistake and breaking networking.

``` bash
sudo /etc/init.d/networking restart
```

If successful, server traffic will now automatically route through the `br0` interface, which you can also configure containers and VMs with.  If you are not using Docker as well as LXD, you can probably proceed to configure LXD to use the new bridge interface. 

If you are also using docker, it modifies `iptables` in a way that prevents traffic being forwarded through the new bridge to LXD containers (see [this Github issue](https://github.com/docker/for-linux/issues/103) for more details). To fix this, I needed to add the following `iptables` rule to allow this traffic. It is inserted into the `DOCKER-USER` chain, so that it plays well with other Docker rules.

``` bash
sudo iptables -I DOCKER-USER -i br0 -o br0 -j ACCEPT
```

To make this survive reboots, I needed to create a script that runs after docker has started (i.e., after docker has created the `DOCKER-USER` iptables chain).

Create a script at `/usr/local/bin/post-docker.sh`:

``` bash
#!/usr/bin/env bash

date > /var/log/post-docker-timestamp
iptables -I DOCKER-USER -i br0 -o br0 -j ACCEPT
```

Make it executable:
``` bash
sudo chmod u+x /usr/local/bin/post-docker.sh
```

Create a `systemd` unit at `/etc/systemd/system/postdocker.service`:
```
[Unit]
Description=Post Docker
After=docker.service
BindsTo=docker.service
ReloadPropagatedFrom=docker.service
[Service]
Type=oneshot
ExecStart=/usr/local/bin/post-docker.sh
ExecReload=/usr/local/bin/post-docker.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Enable the new systemd unit:

``` bash
sudo systemctl enable postdocker.service
```

After a reboot, confirm that it ran successfully by inspecting the `/var/log/post-docker-timestamp` file and the output of `sudo iptables-save`.

> Note: These rules are adapted from rules discussed in this [github issue](https://github.com/docker/for-linux/issues/103).


Now set the bridge to be the default interface on containers.

``` bash
lxc profile device set default eth0 parent br0
lxc profile device set default eth0 nictype bridged
```

And change the interface on any existing containers to use it too:

``` bash
lxc config device remove <containername> eth0
lxc config device add <containername> eth0 nic nictype=bridged parent=br0 name=eth0
```

Start or restart affected containers and confirm they now get an IP address:
``` bash
lxc restart <containername> 
lxc info <containername> 
```

Confirm connectivity:

``` bash
lxc exec <containername>  bash
containername> ping 8.8.8.8
```
