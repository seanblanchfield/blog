---
author: Sean Blanchfield
comments: true
date: 2011-04-08 11:09:44+00:00
layout: post
link: https://seanblanchfield.com/flash-weirdness-of-the-day-flashwod/
slug: flash-weirdness-of-the-day-flashwod
title: Flash Weirdness of the Day (FlashWoD)
tags:
- Actionscript3
- Code
- Tech
---

I spent some significant time trying to hunt down a bug (or maybe heisenbug), on and off for the last week. Thought I'd nailed it last night, but it was back again this morning.

<!-- more -->

This is in our pure actionscript 3 game that we're developing. It was a crash to do with a null being dereferenced, which was traceable back to a flashvar that is passed into the SWF randomly getting lower-cased by unknown forces. This flashvar is supposed to be a case-sensitive string ID, so when it got lowercased, the thing it was supposed to refer to didn't match it any more.

In the end, it all came down to firebug. If I hit refresh in Firefox normally, everything worked properly. However, if I opened firebug and then refreshed, the flashvar will be magically lowercased before being handed to the SWF. Putting a trace at the top of the main stage owner sprite like so:

``` actionscript
trace("Flash var: " + embedded_variables.assume_stage);
```

Would normally reveal:

```
**Flash var: MY_CASE_SENSITIVE_IDENTIFIER**
```

But opening firebug and refreshing again gives:
```
**Flash var: my_case_sensitive_identifier**
```

At all times, the flashvar in the DOM (as revealed by Firebug) was unchanged and correct.

So, I added a call in actionscript to explicitly uppercase that flashvar so that we don't crash with firebug.

Inexplicable. I don't really know what to blame here: firebug, flash or firefox. I'm tempted to blame Flash though, which seems to infect everything it touches with Adobe's personal brand of crazy.