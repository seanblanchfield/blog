---
author: Sean Blanchfield
comments: true
date: 2011-06-20 20:51:14+00:00
layout: post
link: https://seanblanchfield.com/another-boxee-box-fail/
slug: another-boxee-box-fail
title: Another Boxee Box Fail
tags:
- Life
- Tech
- boxee dlink
---

Every software update that comes down to my Boxee box seems to be mainly about removing features, not adding them. Their last update hilariously [removed volume control]({% link archive/_posts/2011-05-13-boxee-box-fail.md %}) from the system, in the name of a consistent user experience. When the system downloaded and forced an update this evening, we had our jokes at the ready about what was going to be removed next.

<!-- more -->

Well, in our case, **it turned out to be support for video**. No kidding. It boots, shows a nice video, blinks once or twice, and then rejects the TV as a device it wants have an intimate relationship with. After a bit of research, it turns out that the Boxee's support for DVI TVs (via a standard converter) was an accidental oversight, and one they cheerily lopped in today's compulsory update. There are some irate threads running on their community support forums, which all consist of bewildered users vainly searching for words to communicate how it feels to have features routinely removed from your media center against your will, culminating in its actual ability to **play video**. Unbelievable.

I'm not sure what was to gain by removing support for DVI TV's. I hope it was good, because this could well nail the coffin shut in terms of the public's ability to trust the Boxee team to properly curate the project. As I mentioned in my last post when they removed a feature, long gone are the days you bought a gadget for its packaged features. Connected devices like Boxee are bought based on trust in the manufacturer, to maintain the service, add the right features, and to not be evil. Whatever about punters in shops, the boxee team are losing the trust of their early adopters.

If anyone from boxee is reading this, consider this question: Am I better off spending €500+ on a new TV to support your update, or perhaps using that money to buy a better system while flogging the boxee on ebay?

**How to fix** Should anyone be in the same boat, here's a detailed description and resolution:

After update 1.1.2.19250, the boxee reboots, and shows the opening animation. When that's done, the boxee logo on the box blinks once, and the TV loses its signal. The box remains on, but there is no video output.

This appears to be limited to those that are sending video through a HDMI-DVI converter. Apparently DVI support was never official, so we should have expected it to be arbitrarily removed at any time in a compulsory update without warning.

You can get things up and running by switching back to the previous version (performing a manual update) and preventing the compulsory update re-fubaring your system (by blocking access in your router's control panel).

**EDIT: As of 25th June 2011, update 1.1.3.19252 fixes this issue. See [this thread](http://forums.boxee.tv/showthread.php?t=37901) for information on how to install it. This seems to be a special-case fix until it can be rolled into the next official version, and to the Boxee team's credit, it took them just 5 days to make it available. I hope that this episode will lead them to improve both their testing and communications for the future. Like many of the early adopters among the Boxee userbase, I want to love this product. I want to recommend it to friends, and buy it for them at Christmas, because I believe in the Boxee project. But to do that, I need some re-assurance that these updates from hell will stop.**

Details are:

1.  You need to stop the Boxee from auto-updating. To do this, you need to get into your router's admin control panel, and block access to the following site: "app.boxee.tv/chkupd/dlink.dsm380".
2.  Download the previous firmware from [http://dl.boxee.tv/version/dlink.dsm380/1.1.1.19092/boxee.iso](
    http://dl.boxee.tv/version/dlink.dsm380/1.1.1.19092/boxee.iso)
3.  Stick it on a USB thumbdrive, put it in the Boxee. Turn it off, and then turn it back on by holding down the power button for 6-10 seconds. It will now boot into recovery.
4.  Choose to "upgrade" to the version on the USB thumbdrive.

Now, we wait to see how the Boxee team respond. You can also vote on this bug here: [http://jira.boxee.tv/browse/BOXEE-10224](http://jira.boxee.tv/browse/BOXEE-10224) (you'll need to create an account).

**Update - June 22 2011** According to this [thread](http://forums.boxee.tv/showthread.php?t=37520&page=17), the Boxee team have started work on "a fix that will be released soon". This is great news, but is unfortunately hearsay. I hope that it will be officially confirmed and that steps will be taken to improve communication in general.