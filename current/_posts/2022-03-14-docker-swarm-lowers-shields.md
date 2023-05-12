---
author: Sean Blanchfield
date: 2022-03-14 21:00
layout: post
link: https://seanblanchfield.com/docker-swarm-lowers-shields/
slug: docker-swarm-lowers-shields
title: Docker Swarm Lowers the Shields
image: /images/2022/03/reliant.jpg
tags:
- Code
---

Today I learned that Docker automatically does extremely wreckless and dangerous things to the firewall on every node in a docker swarm, which leaves various swarm services wide open to the internet, and that Docker provides no way to turn off this behavior. I spent a lot of time today trying to understand what the hell was happening, and then a lot more time trying to find a solution to fix it. I think I found a better solution than suggested anywhere else, so here it is for anyone who stumbles here via a search engine. 

<!-- more -->

Docker automatically reconfigures `iptables` to set up its networking. If you have a service port of type `ingress`, you will see a few rules in your `iptables` corresponding to it, which take care of routing that traffic in the right direction. These rules allow traffic from any source to route to any service ports of type `ingress`. This is arguably helpful for the `tcp/80` and `tcp/443`. I wouldn't make that argument, but someone might. However, I have some ingress ports defined to make cluster-wide services such as logging and discovery internally available. I do not want these exposed to the internet, and I did not expected Docker to automatically reconfigure the filewall to make them available, but that's what happened. Even worse, I noticed that Docker had opened port `8080` on my test cluster, directly connecting to a  [docker-container-stats](https://github.com/virtualzone/docker-container-stats) instance, which does not even define an ingress port. I don't know why it did this - most other non-ingress service ports were still safely firewalled off, but this one was open. A mystery.

None of this behavior is visible if you try to find them with `ufw`. You need to go a level deeper, and look at the whole `iptables` config using a command like `iptables-save`.

This is all surprising and dangerous. External access into services should be by explicit configuration only. Docker uses `iptables` for internal networking, but most of us use it as our firewall. When docker adds a rule opening access to a service, it is opening it up to the World. 

{: .callout }
> I spent a long time today simply not believing my eyes, and then searching for an explanation as to how this could have been built this way. The only explanation I found was that maybe the engineers who wrote this didn't expect Docker Swarm to be run directly on the Internet. Maybe they thought that there would always be separate (non-swarm, maybe non-Docker) load balancer and firewall in front of docker swarm nodes (allowing them to throw caution to the wind and have fun with the node firewalls). For me, however, the point of having a cluster is to run all my infrastructure inside of it.

 Docker [documentation discusses](https://docs.docker.com/network/iptables/#prevent-docker-from-manipulating-iptables) an `iptables: false` option that can be supplied through the `/etc/docker/daemon.json` file. By "discuss", I should really say "warns you not to use it". Anyway, I tried using it, and discovered that it simply does not work at all (and [open issues related](https://github.com/docker/for-linux/issues/136) to this appear to be unattended for years).

One solution to this security nightmare is to put a non-swarm loadbalancer and firewall in front of docker swarm.  Another is to flush all docker firewall rules out of `iptables`, however doing this breaks inter-service connectivity in my testing. So I did some further testing.

When docker configures iptables for an ingress service port, it creates three rules, such as

``` txt
-A DOCKER-INGRESS -p tcp -m tcp --dport 8080 -j DNAT --to-destination 172.18.0.2:8080
-A DOCKER-INGRESS -p tcp -m tcp --dport 8080 -j ACCEPT
-A DOCKER-INGRESS -p tcp -m state --state RELATED,ESTABLISHED -m tcp --sport 8080 -j ACCEPT
```

In my cluster, an ingress port might be `80` or `443`, used for the load balancer (I am using *docker-flow-proxy* running with [letsencrypt-provisioner](https://github.com/seanblanchfield/docker-flow-proxy-letsencrypt-provisioner)). Or it might be an internal service, which I want to be available across every container in every stack in the cluster (e.g., logging). I achieve the latter by having logging clients connect to the `DOCKER_GW_BRIDGE` IP address. So, in the above example, I can connect to `172.18.0.1:8080` from any container and reach the service (i.e., `nc 172.18.0.1 8080` succeeds)

By removing any of the above rules, I would disable access both from the internet and from inside the cluster. However, after a bit of experimenting, I found that I could harden the rules by restricting the `ACCEPT` rule to only allow internal docker source IP addresses (i.e., `172.16.0.0/12`):

```
-A DOCKER-INGRESS -p tcp -m tcp -s 172.16.0.0/12 --dport 8080 -j ACCEPT
```

I found that I could automatically process `iptables` to make this change using `sed`:
``` bash
sudo iptables-save | sed -re "s/(-A DOCKER-INGRESS -p (udp|tcp) -m (udp|tcp) --dport .*)( -j ACCEPT)/\1 -s 172.16.0.0\/12 \4/" > /tmp/iptables-fixed.txt
sudo iptables-restore < /tmp/iptables-fixed.txt
```

At this point, internal communication was open between containers as normal, but internet access to ingress ports had been shut down. Obviously, I actually want to be able to serve web traffic, so to re-open web I needed to add a rule. Simply adding a new rule in `iptables` or `ufw` won't work, because the `DOCKER-INGRESS` `iptables` chain will be evaluated first. Docker provides the `DOCKER-USER` chain for this purpose. We can insert a new rule in there and it will get evaluated first.

To explicitly open access to a port to the Internet, you can use the `-I` option to insert a new rule at the top of the `DOCKER-USER` iptables chain, which is evaluated before the `DOCKER-INGRESS` chain:
``` bash
sudo iptables -I DOCKER-USER -p tcp -m tcp --dport 80 -j ACCEPT
```

Putting this altogether, here is a script that hardens Docker's lax iptables rules, and then explicitly opens up web.

``` bash
#! /usr/bin/bash

# Docker swarm automatically makes service ports available to the internet by creating new iptable rules.
# These firewall rules will not show up in ufw.
# This script is intended to be run as a `ExecStartPost` step in dockerd's systemd unit, and tightens up any
# iptable rules it finds left there by docker. In particular, it limits all traffic to service ports to 
# internal docker client IPs in the subnet 172.16.0.0\/12.
# In addition, it opens up the HTTP/HTTPS ports.

iptables-save | sed -re "s/(-A DOCKER-INGRESS -p (udp|tcp) -m (udp|tcp) --dport .*)( -j ACCEPT)/\1 -s 172.16.0.0\/12 \4/" > /tmp/iptables-fixed.txt
iptables-restore < /tmp/iptables-fixed.txt
rm /tmp/iptables-fixed.txt

# Open up HTTP/HTTPS ports. Avoid creating duplicate rules by checking with `iptables -C`
rule="DOCKER-USER -p tcp -m tcp --dport 80 -j ACCEPT"
if ! iptables -C $rule 2> /dev/null; then 
    iptables -I $rule
fi

rule="DOCKER-USER -p tcp -m tcp --dport 443 -j ACCEPT"
if ! iptables -C $rule 2> /dev/null; then 
    iptables -I $rule
fi

```

I then made sure this script is run automatically when docker starts by adding it to the `docker.service` systemd unit as a post execution hook.  On Ubuntu 20.04, this file resides at `/lib/systemd/system/docker.service`:
``` 
[Service]
# ...
# ExecStart=...
ExecStartPost=/usr/local/bin/fix-docker-iptables-rules.sh
```
Finally, for good measure I also invoke this script during the final build step during CI deployments.
