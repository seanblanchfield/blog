---
author: admin
comments: true
date: 2011-08-04 11:06:11+00:00
layout: post
link: https://seanblanchfield.com/fixing-the-boxee-box-remote/
slug: fixing-the-boxee-box-remote
title: Fixing the Boxee Box Remote
wordpress_id: 422
tags:
- Tech
- dlink boxee
---

Over the last week the remote for my [Boxee Box](http://www.dlink.com/boxee/) started going a bit weird. I thought that the battery was probably dying, so replaced it, but it still wasn't working right.

After some frustrated experimentation I discovered that I could make it work by pressing hard on the battery compartment cover while using it. It looks like I had the same issue as described on the Boxee issue tracker, [here](http://jira.boxee.tv/browse/BOXEE-8352). People on the Boxee forum [here](http://forums.boxee.tv/showthread.php?t=39121) also described it, among other things.
<!-- more -->
### Diagnosis

It looks like people are suffering from various issues with the remote, some of them software issues. The fix I describe below is only for people who seem to be suffering from the battery not making full contact with the terminals inside the battery compartment. You can normally tell by pressing hard on the battery compartment while trying to operate the remote. If this temporarily fixes things, then this post is for you.

It looks like the contacts inside the battery compartment can get bent out of position over time. Pushing on the battery cover re-establishes contact temporarily, but also probably just bends the contacts even further. I did some experimenting to try and fix this. First of all, I tried to jam some paper in the battery holder behind the battery to push it farther into the compartment when closed, unfortunately, this didn't work reliably for me. Eventually, what did work was to pull the battery contact back into the compartment so that it would make full contact with the battery again. Since so many people seem affected by this, I took pictures along the way.

### Tools required

One paperclip.

### The Operation

First of all, the disclaimer. There are crazy people in the world who attempt to hold bloggers responsible for bad advice. If you mess your remote up following the instructions below, it's your problem, not mine.

First of all, let's look at the 3v lithium battery. \[caption id="attachment\_423" align="alignnone" width="300" caption="The battery used in the boxee box. Note the positions of the contacts."\]![](/images/2011/08/battery-300x187.jpg "Lithium battery")\[/caption\]

The battery has its negative contact on its top, and its positive contact on the bottom and all around its sides. The Boxee remote makes contact with the top and the sides of the battery.

I made a little hook out of a paper clip to poke around inside the battery compartment with. \[caption id="attachment\_425" align="alignnone" width="600" caption="A paper clip, and trusty but battered needle-nosed pliers."\]![](/images/2011/08/hook.jpg "hook")\[/caption\]

Next, let's have a look inside the remote battery compartment. Remove your battery holder, and look into the empty compartment (you might need some bright lighting), you should see the following: \[caption id="attachment\_426" align="alignnone" width="600" caption="Inside the Boxee remote battery compartment"\]![Inside the Boxee remote battery compartment](/images/2011/08/boxee-remote-battery-compartment.jpg "boxee remote battery compartment")\[/caption\]

_Note:_ At the very rear of the compartment is a kind of hooked pin that makes contact with the (positive) sides of the battery. I originally imagined it was this terminal that was at fault, but I was wrong. I tried to bend it back towards me with my paperclip hook, but it made no difference.

**To fix your remote, gently pull the negative terminals out a bit.**

It's not very clear in the photo, but you should be able to see them clearly in your own remote. The negative terminal consists of 2 very small strips of metal on the bottom side of the compartment. You can easily hook your paperclip around these, and pull them back a little so that they protrude more into the compartment. This should help them make fuller contact with the battery when you re-insert it.

Please be careful, and don't pull them out too much, break them off, or otherwise damage your remote. Go slowly, testing the remote until it works again.