---
author: Sean Blanchfield
comments: false
date: 2013-11-03 20:21:03+00:00
layout: post
link: https://seanblanchfield.com/awkward-bedfellows-xero-aib/
slug: awkward-bedfellows-xero-aib
title: 'Awkward Bedfellows: Xero and AIB'
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

![organgrinder](/images/2013/11/organgrinder.jpg){: .right-half }

However, AIB's "Internet Business Banking" is a typically confusing online banking system, with theatrically obtuse security features that succeed at frustrating the user instead of the fraudster. At least it more or less works, unlike [Bank of Ireland](http://boi.ie)'s corresponding system (which I've never successfully used without having to telephone a helpdesk to decipher unhelpful error codes). I've heard that Ulster Bank's online banking system is great, but they suffer from a lack of branches - handy for those inevitable occasions you actually need to see someone.

When using Xero you can configure it to read from a bank feed so that it stays automatically up to date with your account. Whatever giant software megaconsultancy built AIB's online banking systems saw fit to equip _personal banking_ with this feature, but not the business banking system. Go figure.

Anyway, as a business client, you are left with the option to export transactions in CSV format. Unfortunately, AIB's business banking system grabs defeat from the jaws of victory, producing only a very broken attempt at CSV. The process of importing this into Xero therefore involves tedious and error-prone hand-fixing the file in Excel or a text editor.

**Thankfully, I found the people who could help**. After some detailed online research I found [ProfitPal](http://www.profitpal.ie), a [Irish Xero accountancy firm](http://profitpal.ie) who has been through all this before. ProfitPal has embraced the cloud. I had barely engaged with them before I was equipped with a new Xero account, a [ReceiptBank](http://receipt-bank.com) account, a cloud-based file drop, and was also the proud owner of an Excel macro that did a valiant job at fixing up the broken AIB CSV format. Last night, with my vestigial developer instincts tingling, I couldn't help tinkering with it a bit.

A few hours later, the result is now available to all at [AIB2Xero.com](http://AIB2Xero.com). It's a fully HTML5/Javascript based converter, meaning that you can use it to convert your broken AIB transaction histories into Xero-compatable files without any of your data leaving your computer. Best of all, you don't need to deal with Excel. If you want to prove this to yourself, download the [_index.html_](https://bitbucket.org/seanblanchfield/aib2xero/src/2b7818c7f658c7b7bcad079bec1cc49ad70dc228/index.html?at=default) file, open it and do the conversion locally with your network cable pulled.

You can use it online [here](http://AIB2Xero.com), or fork it on [bitbucket](https://bitbucket.org/seanblanchfield/aib2xero).

---
## Archived Comments

{: .archived-comment}
> **June 20, 2014 at 6:41 am, Eimear says:**
> Hi Sean, is it possible to feed personal AIB accounts to Xero? Can this be done online and if not, what’s the best department to speak to in AIB? Cheers
> 
> **June 20, 2014 at 9:17 am, Sean Blanchfield says:
> **
> Hi Eimear, I am told it’s possible but I haven’t tried it. Please leave a note here with instructions if you figure it out!
> 
> Sean

{: .archived-comment}
> **September 3, 2014 at 5:43 pm, Chris says:**
> Thanks for this information. Coming home to Ireland and using AIB business banking is like going back in time. The fact that i will be charged 65 euro a quarter to use this antiquated system is especially annoying. I phoned their helpline and was greeted by a sneering women who was talking to me like i was an idiot because i wanted my bank account to automatically reconcile with my accounting software. A concept that she obviously didn’t understand.
> 
> I will have to to download the .out file and use this helpful converting tool. Thanks again. At least someone understands these issues even if the bank itself doesn’t have an idea about business needs of a small business user.

{: .archived-comment}
> **September 11, 2014 at 4:40 pm, Rowena Kellt says:**
> Hi Sean, just wondering if you or anyone knows of a similar way to get Bank of Ireland to work with Xero? Am seriously thinking of leaving BOI because of their crap online business banking , but would like to not have to manually up load every transaction in the meanwhile. Cheers.

{: .archived-comment}
> **October 9, 2014 at 9:03 am, Ralph says:**
> Hi Rowena,
> 
> If you run a transaction detail report in BOI – Copy the transactions off the screen, Paste them into an excel sheet , delete the unnecessary columns you can import BOI into Xero but unfortunately it’s a little time consuming.
> 
> Feel free to drop me an email if you get stuck with it
> 
> Ralph

{: .archived-comment}
> **October 31, 2014 at 1:38 pm, Cormac says:**
> Hi Sean,
> I tried it but it wont upload a CSV file I created from a BOI excel statement. It says OUT file extensions only. Looking at the source code its obvious that your converter is specifically set for the “broken” AIB CSV. If I could see what format an AIB broken CSV comes in and make the BOI one the same then it should work.
> I continued searching for a fix for BOI. You can copy transaction reports and paste into excel and save as a CSV. This is not compatible with your converter as its obviously broken in a different way! I found a very useful webtool to convert CSV to QIF format (the preferred format at Xero) http://csvconverter.gginternational.net/ This has a few drop down menus for each column in your CSV so you can select the heading (like Date, Payee, Debit, Credit ..or if there is a pointless column like a second date column in the case of BOI, you can choose to ignore that.
> The saved QIF works on Microsoft Money and Xero. It took me less than 5 mins to convert as opposed to messing with macros and formats on excel for much longer.

{: .archived-comment}
> **January 10, 2015 at 9:18 pm, Sean O'Rourke says:**
> @Rowena For BOI (Bank of Ireland) Xero users the best way to get the data into Xero is to run the bank statement report for the period you want (say last month). It will open in a new window ready to print, instead of printing just drag the mouse over the data to highlight it, copy it and then open Excel. Then, rather than just normal paste, use Paste (Keep source formatting). The data is now in Excel and you can start deleting all columns except the Date, Description, & Amount. Save the file as a .csv and its ready to import to Xero. It sounds like a lot of work but it generally does not take more than 5 minutes to do the above for a months transactions.
> 
> PS Sean, great app, we use http://www.aib2xero.com all the time – sincere thanks!

{: .archived-comment}
> **February 27, 2015 at 7:19 pm, Simon Dempsey says:**
> 
> You legend Sean – serious time saver!!
> Hope you’re well.
> 
> -Simon.

{: .archived-comment}
> **June 5, 2015 at 5:30 pm, Lisa says:**
> 
> Hi Sean, I am very inexperienced and trying to fiddle around with Xero. I have managed to convert the .out file, but unsure how to then save and upload it into Xero as I cannot save it as .csv file. Any assistance would be gratefully received!

{: .archived-comment}
> **July 10, 2015 at 8:49 am, David Ahern says:**
> 
> Hi Sean,
> 
> Just wondering if you know of any XERO training day run by any proficient user/trainer?
> 
> Perhaps you deliver such training sessions?
> 
> Cheers!

{: .archived-comment}
> **August 4, 2015 at 3:43 pm, Catherine Surant says:**
> 
> Hi Sean, I am using the Xero accountancy software on a 30 days trial and will be purchasing at the end of the period. I have been trying to export the AIB Business on line transactions for July 2015 in the AIB-to-Xero Converter you have been showing on your webpage but nothing happens and I don’t know then how to import to Xero. Can you please help me? I am the bookkeeper for the Company I work for and not very savvy when it comes to computer related matters. A simple step by step would be gratefully appreciated. Kind Regards Catherine
> AIB-to-Xero Converter
> 
> Allied Irish Bank Internet Business Banking allows you to download a transaction history in CSV format. Unfortunately its CSV format is broken and incompatible with the the fantastic cloud-based accountancy system Xero. This simple converter turns the AIB CSV file into one compatable with Xero.
> 
> My transaction history is private. Is this secure?
> 
> This converter is implemented 100% in javascript, meaning that conversion happens in your browser, not on the server this page is hosted on. In fact, no data is sent to the server at all.
> 
> Drag & Drop or choose file file:

{: .archived-comment}
> **September 13, 2015 at 7:20 am, Sean O'Rourke says:**
> 
> Hi Rowena,
> 
> I know it’s a while since your post but glad to report that Bank of Ireland now allow small companies use Banking 365 (instead of Banking On Line). B365 links with Xero and has excellent smartphone/ iPad Apps. Many of our BOI clients have switched and found it excellent (it’s also free). Rgds,Sean

{: .archived-comment}
> **January 4, 2016 at 5:07 pm, James Delaney says:**
> 
> I just want to chime in and add that BOI is the same.. I have a Lloyds business account and guess what.. it works great with Xero…!
> Irish banks get your act together!!

{: .archived-comment}
> **June 7, 2016 at 11:32 am, Sarah says:**
> 
> THANK YOU SO MUCH!! Sean this post was SUPER helpful…..was getting so frustrated with AIB help desk

{: .archived-comment}
> **April 25, 2017 at 8:28 pm, Mark Ogilvie says:**
> 
> Hi Sean, I’d like to modify and use your AIB2Xero code on BitBucket as an open xero tool in my Irish Payroll add-on.
> I couldn’t find a license file, is it open source?
> Cheers.

{: .archived-comment}
> **February 4, 2018 at 10:28 pm, Teri Morris says:**
> 
> Does this still work? When I go to upload the CSV file I get a message saying “you may only upload files with the OUT extension”. I was hoping this tool would help but can’t get it to work.
> 