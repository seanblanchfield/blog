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

This normally just required LXD bridge networking, but it turns out that Docker interferes with this. Fixing it took a bit of research and experiementation. Here are details on what worked for me.

<!-- more -->
---

### Option 1: macvlan - easy to configure, but containers and host cannot communicate.
``` bash
lxc profile device set default eth0 parent eno1
lxc profile device set default eth0 nictype macvlan
```

### Option 2: (preferred) Set up bridge networking.

I found this a bit trickier to do, because Docker inserts firewall rules that interfere with packet forwarding.

Here is a `iptables` rules inserted into the `DOCKER-USER` chain that permits forwarding of traffic through the bridge.

``` bash
sudo iptables -I DOCKER-USER -i br0 -o br0 -j ACCEPT
```

To make this persistent, I needed to create a script that runs after docker has started (i.e., after docker has created the `DOCKER-USER` iptables chain. 

Create a script at `/usr/local/bin/post-docker.sh`:

``` bash
#!/usr/bin/env bash

date > /var/log/post-docker-timestamp
iptables -I DOCKER-USER -i br0 -o br0 -j ACCEPT

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
