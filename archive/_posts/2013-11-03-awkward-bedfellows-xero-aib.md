---
author: admin
comments: false
date: 2013-11-03 20:21:03+00:00
layout: post
link: https://seanblanchfield.com/awkward-bedfellows-xero-aib/
slug: awkward-bedfellows-xero-aib
title: 'Awkward Bedfellows: Xero and AIB'
wordpress_id: 1037
tags:
- Code
- Enterprise
- Ireland
- Tech
- Javascript
---

In [PageFair](http://pagefair.com) I'm striving to automate as much admin as possible. This means figuring out for once and for all how best to handle startup accountancy in Ireland, stretching all the way from receipts and invoicing all the way up to on-demand management accounts and cashflow projections. After much searching I found [Xero](http://xero.com), a terrific cloud-based accountancy system. Getting it to play nice with AIB banking was another matter.
<!-- more -->
[Allied Irish Bank](http://aib.ie) is the bank we chose, and as our expectations of Irish banks go, we're largely happy. A big shout out to business centre staff, who have always worked hard to help us out.

![organgrinder](/images/2013/11/organgrinder.jpg)However, AIB's "Internet Business Banking" is a typically confusing online banking system, with theatrically obtuse security features that succeed at frustrating the user instead of the fraudster. At least it more or less works, unlike [Bank of Ireland](http://boi.ie)'s corresponding system (which I've never successfully used without having to telephone a helpdesk to decipher unhelpful error codes). I've heard that Ulster Bank's online banking system is great, but they suffer from a lack of branches - handy for those inevitable occasions you actually need to see someone.

When using Xero you can configure it to read from a bank feed so that it stays automatically up to date with your account. Whatever giant software megaconsultancy built AIB's online banking systems saw fit to equip _personal banking_ with this feature, but not the business banking system. Go figure.

Anyway, as a business client, you are left with the option to export transactions in CSV format. Unfortunately, AIB's business banking system grabs defeat from the jaws of victory, producing only a very broken attempt at CSV. The process of importing this into Xero therefore involves tedious and error-prone hand-fixing the file in Excel or a text editor.

**Thankfully, I found the people who could help**. After some detailed online research I found [ProfitPal](http://www.profitpal.ie), a [Irish Xero accountancy firm](http://profitpal.ie) who has been through all this before. ProfitPal has embraced the cloud. I had barely engaged with them before I was equipped with a new Xero account, a [ReceiptBank](http://receipt-bank.com) account, a cloud-based file drop, and was also the proud owner of an Excel macro that did a valiant job at fixing up the broken AIB CSV format. Last night, with my vestigial developer instincts tingling, I couldn't help tinkering with it a bit.

A few hours later, the result is now available to all at [AIB2Xero.com](http://AIB2Xero.com). It's a fully HTML5/Javascript based converter, meaning that you can use it to convert your broken AIB transaction histories into Xero-compatable files without any of your data leaving your computer. Best of all, you don't need to deal with Excel. If you want to prove this to yourself, download the [_index.html_](https://bitbucket.org/seanblanchfield/aib2xero/src/2b7818c7f658c7b7bcad079bec1cc49ad70dc228/index.html?at=default) file, open it and do the conversion locally with your network cable pulled.

You can use it online [here](http://AIB2Xero.com), or fork it on [bitbucket](https://bitbucket.org/seanblanchfield/aib2xero).