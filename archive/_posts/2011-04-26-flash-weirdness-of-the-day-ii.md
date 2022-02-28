---
author: admin
comments: true
date: 2011-04-26 13:04:15+00:00
layout: post
link: https://seanblanchfield.com/flash-weirdness-of-the-day-ii/
slug: flash-weirdness-of-the-day-ii
title: Flash Weirdness of the Day II
wordpress_id: 134
tags:
- Actionscript3
- Code
- Tech
---

Hit a brand new FlashWoD today! This took me a while to track down, mainly because I couldn't actually believe that it could possibly be true. In Actionscript 3, an empty array created with object literal notation as shown below will evaluate as equal to an empty string. I had a part of a data structure that would be an empty string if uninitialized, and would be an array otherwise.
<!-- more -->
The code below will output "The world has gone mad!", and rightly so, I think. The theory is that the empty array is converted into a string for comparison.


    
    
    var obj:Object = {
        "array": []
    };
    if(obj.array == '')
    {
        trace('The world has gone mad!');
    }
    else
    {
        trace('The world may not be altogether mad.');
    }
    



Brian here did an experiment that showed that a literal array below would display the same behavior. Note that it must be assigned to a variable of type `Object`, otherwise the comparison won't compile (which is something, I guess):


    
    
    var obj:Object = [];
    
    if(array == '')
    {
        trace('The world has gone mad!');
    }
    else
    {
        trace('The world may not be altogether mad.');
    }
    
