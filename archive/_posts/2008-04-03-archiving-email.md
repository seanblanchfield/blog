---
author: admin
comments: true
date: 2008-04-03 21:02:34+00:00
excerpt: I still have every email I've ever sent or received, since 1996... I want
  to get them into some common format that I can come back to in 45 year's time and
  actually open and read.
layout: post
link: https://seanblanchfield.com/archiving-email/
slug: archiving-email
title: Archiving Email
wordpress_id: 760
tags:
- email
- python
---

I still have every email I've ever sent or received, since 1996. For me, it represents the best written account of my adult life, since I've never been much good at keeping a diary. I value it, and think it would be a great loss if I lost them all. By that I mean I would really regret the loss in later life. I'm thinking of a nostalgia-ridden me on my seventieth birthday.
<!-- more -->
There's a lot of email actually, over 100GB, and it's hard to manage. Worse, it's hard to browse and search, because it's in different formats. The really old ones were Eudora based, then Netscape Navigator, Outlook, then Thunderbird, then Gmail. I had managed to import all the preceding mails into Thunderbird some years ago, but still had a few different zipped up Thunderbird profiles containing the mail, as well as my Gmail account. What I wanted was to get them into some common format, along with attachment data, which would be future-proof, which I could browse, and which could be indexed by a desktop search system such as Google Desktop.

I don't really expect to spend a lot of time browsing the mail, and I don't want to have to maintain the file format that they are in by importing and exporting them from future mail client software. I want to get them into some common format that I can come back to in 45 year's time and actually open and read.

This definitely means that Outlook's PST format is out the window. I also think that 45 years is a long enough time that we can also expect Thunderbird to have moved on significantly. In fact, it is quite likely that no one but me and you will remember what email is.

I did a little bit of research, and decided that the best format is the most basic one. For email, this is the [email format](http://en.wikipedia.org/wiki/Electronic_mail#Format), unsurprisingly. This is familiar to us all from our mail clients: ASCII, a header section consisting of colon-delimited headers (To:, From:, Subject:, Date:, etc.), followed by an empty line, followed by the text body. It may also be MIME encoded, and contain attachment data in base64 encoding. The standard file extension is ".eml".

This format is ubiquitious. Although modern email clients try to buffer the user from it, it's there in the background. When you send an email to an SMTP server, what you send is one of these.

So, the bet I made was that future mail clients will probably support exporting to eml format so long as SMTP continues to be used. I only looks as far as Thunderbird, which does (at least with the appropriate extension installed).

So, step one was to get all my mail into eml formatted files. My preference is to arrange mail into folders for In/Out for each year.

1.  I copied my archived Thunderbird profiles into Thunderbird's application directory, and started up. I exported each Local Folder to eml (I already had the Thunderbird mail arranged into yearly In/Out boxes).
2.  I set Thunderbird up to grab some IMAP mail I had on a server. IMAP means that you download headers only at first, and email bodies only as necessary. Thankfully, the Thunderbird plugin I had to export to eml made that transparent (it just had to be left run overnight as it requested each mail one-by-one).
3.  I set Thunderbird up to grab my Gmail via POP (its in the gmail account options). I downloaded all of that, then exported again.

Now, I had a directory on my hard-drive containing all of my email, in eml format, arranged into yearly In/Out subdirectories. A desktop search system would now be able to index them, but they remained more or less impossible to browse.

\[caption id="" align="alignright" width="206" caption="Side navigation screenshot"\]![Side navigation screenshot](/wp-content/uploads/2009/02/sidenav.jpg "Side nav")\[/caption\]

I decided that I needed to write a script to parse through them all, generating a navigatable set of HTML pages that would hyperlink to each email by date, subject, to and from header fields. I never miss an opportunity to write some Python, so that's what I did.

The final program is quite short, and produces nice results. Each subdirectory get's its own EmailIndexN.html file, where N is a number. Each of these contains navigation elements to the parent directory and any subdirectories.

They each also contain a table listing of at most 100 emails, with links to the actual files on disk. At the bottom, there is navigation for previous and next pages, as well as direct links to each page.

\[caption id="" align="alignleft" width="373" caption="Bottom pagination"\]![Bottom pagination](/wp-content/uploads/2009/02/bottomnav.jpg "bottom pagination")\[/caption\]

And each page links to a style sheet of your choice.

Here's an example a typical page (in this case, directory navigation just contains a link to the parent directory):

\[caption id="" align="aligncenter" width="860" caption="Email list screenshot"\]![Email list screenshot](/wp-content/uploads/2009/02/full.jpg "Email list")\[/caption\]

You can grab it [here](http://drop.io/bcyhp4u) if you like. If that link has expired, please let me know with a comment.