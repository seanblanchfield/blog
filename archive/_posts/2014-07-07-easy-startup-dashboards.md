---
author: Sean Blanchfield
comments: false
date: 2014-07-07 18:09:08+00:00
layout: post
link: https://seanblanchfield.com/easy-startup-dashboards/
slug: easy-startup-dashboards
title: Easy Startup Dashboards
image: /images/2014/07/Screen-Shot-2014-07-07-at-19.05.34.png
tags:
- Code
- Enterprise
- Ireland
- Tech
---

At [PageFair](http://pagefair.com) we’ve repurposed all our spare monitors as cheap real-time business dashboards. Here's how you can do the same ([especially if you’re in Dublin](https://mloccy.github.io/Beaglebone-Black-Dashboards/)).

<!-- more -->

> _"That which is measured improves"_

It's one of those business truisms that escapes attribution, but some brief research says it was probably Peter Drucker or Karl Pearson. Whoever it was figured it out decades before "_Lean_" came into vogue for the rest of us. It crept into my phrasebook sometime in 2010 when we were working on a Lean Manufacturing gamification startup. That was the year I learned to think of companies as systems built on feedback loops, plus several other important facts:

1.  Feedback is useless if it’s tucked 5 clicks away on a password protected admin screen or spreadsheet. **Feedback must be on the wall**.
2.  What metrics you want today will not be so relevant tomorrow. You need real-time wall-based dashboards that are easy to reconfigure.

Since the launch of the [_Raspberry Pi_](http://www.raspberrypi.org/) I’ve been convinced that the components exist to cheaply repurpose every spare screen into a useful wall-based dashboard. Sadly, they’re not yet consumer-ready.

![etsy_dashboards](/images/2014/07/etsy_dashboards.jpg)

I was jealous after visiting [Etsy](http://etsy.com) in Brooklyn and being impressed with staff being able to order in their own 40 inch Apple TV-powered dashboards for nearby walls (more on their dashboards [here](http://vimeo.com/25807922)). I want to achieve the same in [PageFair](http://pagefair.com). Our first attempt was to repurpose spare machines around the office to keep various webpages open on an auto refresh. That began to change our behavior for the better, but the tech wasn’t small, easy or cheap.

Our next attempt was to order a bunch of system-on-a-HDMI-stick Android media players, flash them with Linux, and set them up to drive all our spare monitors. It nearly worked, but the hardware wasn’t quite there yet. The mean time to failure was about three days, after which each of the sticks would need to be re-flashed and re-configured. We (and you) have no time for that.

**The good news is that attempt number 3 worked, and I want to share it with you today**. 

![The Beaglebone Black](/images/2014/07/Screen-Shot-2014-07-07-at-19.06.20.png){: .captioned .right-half }

In 2011 we gave a spare office to the entrepreneurs from Computer Science in Trinity College Dublin known as [Tophat](http://tophat.ie). From that terrific collaboration, various great things have come. Most recently, [Colm Vize](https://mloccy.github.io/Beaglebone-Black-Dashboards/) has come to our aid and sorted out our dashboard situation. The answer was a particular cocktail of cheap components that, when taped to the back of a spare monitor, turn it into solid and flexible wall-mounted live dashboard.

The units Colm created consisted of a [Beaglebone Black](http://beagleboard.org/Products/BeagleBone+Black) (essentially a souped-up Raspberry Pi) with a wifi dongle, attached to a spare monitor, and configured to auto-start a browser in full-screen, login to a given URL, zoom into a part of the resulting web page and auto-refresh ad infinitum. Should they be hit by a cosmic ray, we just pull the plug and restart them. _Solid_.

Here’s what he's got configured for us right now:

1.  _Build monitor._ We use Jenkins for continuous integration tests, and it has a great built-in dashboard. It gives us all warm fuzzies to see it all code continuously re-testing passing, and makes it immediately apparent when someone has committed the ultimate faux pas of faulty code.
2.  _Scrum dashboard._ We’ve switched to [Pivotal Tracker](http://pivotaltracker.com), and have configured the plugin product [in-sight.io](http://in-sight.io) to get their beautiful scrum dashboard, including burndown, recent stories, sprint velocity and more.
3.  _Google Analytics Dashboard._ We have configured a GA dashboard with some juicy tidbits, such as real-time visitors to pagefair.com. More than once this has allowed us to opportunistically maximize the visitor surges delivered from unexpected stories on us.
4.  _New signups._ We have our own proprietary dashboards to measure what we currently see as important. We keep a screen on the wall with recent signups. This allows us to (a) quickly see when we’ve netted a whale and respond accordingly and (b) bond over how cool it is to have traction.

![Build Monitor and Scrumboard](/images/2014/07/Screen-Shot-2014-07-07-at-19.05.34.png){: .captioned}

The best news is that we now have a formula for getting more dashboards on-demand. For only a few hundred bucks, we can quickly and affordably get a new dashboard on the wall to display whatever we feel we need to be measuring ourselves against this month. We’re running the company the way we always aspired to: _data first_.

If you are a tech startup, let me recommend that you immediately re-purpose those old 21” monitors and either:

1.  implement Colm’s [detailed instructions](https://mloccy.github.io/Beaglebone-Black-Dashboards/), or
2.  (if you're in Dublin) Email Colm at [vizec@tcd.ie](vizec@tcd.ie) and offer to pay him to do it for you.