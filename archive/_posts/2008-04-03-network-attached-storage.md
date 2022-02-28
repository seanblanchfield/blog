---
author: admin
comments: true
date: 2008-04-03 21:22:22+00:00
excerpt: I decided that the time had come to figure out a proper solution to the growing
  amount of media that I want to have accessible on my network.
layout: post
link: https://seanblanchfield.com/network-attached-storage/
slug: network-attached-storage
title: Network Attached Storage
wordpress_id: 762
tags:
- NAS
---

About a month ago, I decided that the time had come to figure out a proper solution to the growing amount of media that I want to have accessible on my network.

I suppose the main driver for this is actually my XBMC media center. Previously, to watch or listen to something on the media center, I'd connect the appropriate portable USB drive to my laptop, share out the appropriate directory, and navigate to it from XBMC.
<!-- more -->
That was fine and all, but kind of kludgy. Things I didn't like about it were:

*   Having to turn on my laptop and a portable HDD, as well as the Xbox and TV whenever I wanted to listen to some music or watch a movie.
*   The mess of cables perpetually attached to my laptop.
*   The risk of data loss from damaging the portable HDD.
*   The impending exhaustion of available space on the HDD.
*   The fact that despite all of this, I still needed to figure out a better backup strategy for my stuff.

So, having noticed that things purporting to be Network Attached Storage devices seemed to be on sale for as little as €50 in Maplin, I decided to come up with a better and permanent solution.

The criteria I ended up applying were:

*   must not require special drivers
*   supported disk size
*   speed
*   reliability
*   RAID support

The showstopper for most devices for me was that since I was going to be heavily accessing it via XBMC, it must not require the installation of any special drivers on the client. It turns out, bafflingly, that most of these home NAS devices do require special drivers, despite there being so many pre-existing standard protocols out there for accessing network filesystems.

Anyway, internet reviews eliminated a few other contenders as unreliable. I penultimately ended up debating three options with myself:

*   an ultra cheap system (low speed, no RAID) that wouldn't be a great loss if it didn't work out.
*   a good system such as the DLink DNS-323, but configured for lots of storage, and no RAID 1 (e.g. concatenate 2x big disks with JBOD)
*   a good system (DLink DNS-323) configured for reliability (i.e. 2x big disks in RAID 1)

Eventually, I convinced myself that I should splash out and get the reliable system configured with RAID 1, and furthermore get the biggest disks I could. My rationale was that I didn't want to have to worry about this thing. It should be invisible and just work.

For a long time. By using RAID 1, I would also have solved my backup problem and could consider the data safe. By getting big disks, it would last for several years before it required more space, at which point I could upgrade more easily. I basically considered the extra cost affordable when viewed as a multi-year investment that keeps my data safe and usable.

Eventually, I bought it on Komplett.ie for about €500, including two 1-Terabyte disks. Four days later, it had arrived, and I started to configure it.

I didn't realise when I was buying it that it supported mixed RAID 0, RAID 1 and JBOD. For example, I could have make 500GB RAID 1, then made the remainder JBOD, thus creating two logical volumes - one 500GB "reliable" volume, and one 1TB "unreliable" volume. Meanwhile, I was still tempted to just use JBOD and get 2 TBs available, because it sounds impressive. And the other option, to make it all RAID 1, getting 1TB available but reliable storage. I decided to take a day or two to think on it.

The reason I took a while to so carefully think about it surprised me a little at first too. Which ever path I chose to go down was going to be very hard to return from. The size of the disk is such that if I ever wanted to change from RAID 1 to JBOD for example at some point in the future, I'd be faced with moving potentially more than a terabyte of data around in the process. Basically, once it contained any significant amount of data, I would need another NAS if I ever wanted to reformat or upgrade my NAS, just to back the data onto. I realise that I'll still be faced with this problem in the future at some point, but I hope technology will bring new answers along with bigger disks.

Anyway, I came back from my couple of day's thinking having decided to make the whole lot RAID 1. That is, mirror all data between the 2 disks, halving available capacity, losing the filesystem performance benefits of RAID 0, but gaining full redundancy if/when one of the disks breaks.

I could have gone for the intermediate solution, with partial RAID 1 and partial JBOD, but this "best-of-both-worlds" solution just didn't work for me when I imagined my typical use-case. It would have required me to decide which volume each of my files should be placed on. Trivial enough maybe, but having to frequently make a decision about "whether I can lose this" would pose a step in the routine process of using a storage device that I would be likely to agonise over quite a bit. I decided that I wanted something simple to use, that required no thought besides "files I keep go here".

Another thing that caught me by surprise is that the fact that the DNS-323 is relatively fast is meaningless to me. You can only connect to the thing over the network, and my network is 100Mbps wired, and 54Mbps wireless. The network is the bottleneck, and I had failed to anticipate this.

I started off copying via the wireless network - I think it was my "My Documents" folder - expecting it to take maybe 30 minutes. After an hour or two I realised I'd got something seriously wrong. Naturally I first suspected the NAS, but eventually realised that it was the network that was the bottleneck. I was seeing just 1 megabyte per second being written to it. I couldn't understand that - I had a 54 Mbps connection, right? Well... 802.11 isn't great at throughput. I'm still looking into why and how to improve it, but this kind of throughput is in the right ballpark (back of envelope: 54Mbps = 6.7MBps. Network is half-duplex, so ~ 3 megabytes/sec raw data upstream. Now add headers).

Eventually, I just got all my data ready for copying on the laptop first, then dragged it over to the router, and connected with a real cable, and left it running overnight (or maybe over 2 nights, I can't remember). The throughput on 100Mbit ethernet was about 5 megabytes per sec (still surprisingly low).

Other folks out there on the web say that you can get about 15 megabytes/sec on gigabit ethernet, which would be much better. For the moment, the best internet connection I can hope to get in this country is about 8Mbps, so it all works out. Anything higher, and downloads would be bottlenecked by my WiFi!

Meanwhile, I thoroughly recommend the DNS-323. It just works, and you can even install your own stuff on it (it's linux-based).

So, lesson learned.