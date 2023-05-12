---
author: Sean Blanchfield
comments: true
date: 2008-04-09 21:19:14+00:00
excerpt: My last post was all about how happy I was with my new DNS-323 NAS. Well,
  it's not uncommon for the little problems to only become apparent after a few week's
  of usage.
layout: post
link: https://seanblanchfield.com/network-attached-storage-problems/
slug: network-attached-storage-problems
title: Network Attached Storage Problems
tags:
- Tech
---

My last post was all about how happy I was with my new DNS-323 NAS. Well, it's not uncommon for the little problems to only become apparent after a few week's of usage.

In this case, I might have brought some of them on myself. I've been playing around with the tricks on the associated [hack wiki](http://wiki.dns323.info/), and have got telnet started on it, as well as a Debian etch chroot (this latter was particularly useful for extracting archived files of various kinds quickly, without having to send the data back and forth over the network).

<!-- more -->

Anyway, there are two things that are now annoying me:

1.  Apparently, RAID 1 isn't such a good idea with this thing. There's reports out there of partial and complete data loss when you have your disks set up this way. This undermines the reason that I went with RAID 1 in the first place. Now, reading more on RAID, I realise I should have known better. RAID 1 is designed for availability, and availability doesn't necessarily equate to backups. I don't want to lose my data, but I can tolerate not having access to it for a while. RAID 1 prioritises having 100% access to the data, and the safety of the data is definitely secondary. I shouldn't have used RAID 1.
2.  It's noisey. It wasn't noisey originally, but at some point I upgraded to the 1.04 firmware. Googling around, there are several possible causes: (a) a file in the print queue results in constant disk accesses \[known bug with solution\], (b) A bug in the samba config results in a regular syslog message to the effect that nothing has been happening recently, which prevents the unit entering standby, (c) 1.04 firmware plus RAID1 has a bug resulting in constant disk access. I believe I am afflicted by (c).

So, I'm in a position where, having just moved and organised hundreds of gigabytes onto the device, I need to move it off again and reconfigure the disks into something other than RAID1. I had hoped previously that it would be years before I would have to go through the pain of moving such large quantities of data around again.

Before I continue, let me tell you dear reader, if you are here having googled for "DNS-323", not to use RAID 1. It worked for me (I wasn't unlucky enough to lose any data, like some people), but it was noisey as hell. The unit has been thrashing its disks at full throttle for days now. I could hear it from the bedroom, and found myself turning up the volume on TV shows so I could hear over the din. And it's also annoying from an energy conservation point of view, and would negatively affect disk life too.

Instead, if you are looking for your data to be safe, follow these [instructions](http://forum.dsmg600.info/t1150-Tutorial%3A-Backup-Everything-from-once-night.html), to set up your system with two disks as two separate logical volumes, and automatically sync them together on a scheduled basis using cron and rsync. This has the added advantage that you can easily enough pop a drive out and put it into some other system without worrying about RAID controllers etc.

So, my next challenge (current challenge actually, as I write).

I need to get all the data off the RAID disks onto something else, then turn the RAID disks into plain-old disks, then put the data back on. The problem is that it's a lot of data, and I'd rather it not take several days.

I dismissed my first idea of copying via the network, based on the pain I went through to get all the data onto it in the first place.

I then attempted to (from the Debian chroot), mount a USB external drive, and copy from the mounted RAID filesystem to the mounted USB storage system. I left that running over night. At around 5am I checked on it and it was having problems.

I was using "cp -r", and it was giving me an error that the target disk was out of space, which simply wasn't true. It is a FAT32 disk, which isn't the most efficient or anything, but there was 300GB free on it, and it was still writable from the command line and from windows. It was just cp that was barfing on it. So, that's an unsolved mystery. I just went back to bed and left it for the morning.

So, in the morning, I saw that I'd got about 70 GB into it, and had about 230GB to go. Over USB I measured a tranfser rate of about 8MB/sec, so that would take about 8 hours. I decided to restart the copying, but this time using rsync rather than copy. Rsync should be better - at least it modestly claims to be "extraordinarily versatile" in its own man page. This time though, I was only seeing about 2.5 MB/sec transfer.

I left that get through another 7GB before I gave up in search of a faster way. It occured to me that since the system has two disks in RAID1, I should be able to take one out and still have a working system. Then, surely I should be able to put in the disk from the external drive directly, and mount it. Then copying should be faster, because its going straight over the system bus.

It turns out that I was mostly right. You can take a disk out. It is a little confused (the web admin page doesn't work), but everything else is okay. You can also put in another disk. Once I figured out which /dev entry it was, it mounted ok.

mkdir /mnt/LHS mount -t vfat /dev/sdb1 /mnt/LHS

Then I restarted the copying. It's still going right now, and is in the "B"'s in my music collection. I'll try to estimate the speed now (but it doesn't look stellar :- ).

Okay, results are in, it's about 4 MB/sec. It could be that its affected significantly by number of files as opposed to amount of data (directory access, seeking etc.). I previously got my 8MB/sec copying a 700MB file.

Well, hopefully this doesn't take too much longer. In the meantime, it's still, surprisingly, usable.