---
author: admin
comments: true
date: 2009-02-21 21:32:34+00:00
excerpt: Memoizing describes the programming pattern of caching results returned from
  a function, so that any subsequent calls to the function with the same parameters
  will return a cached value instead of re-computing it. Here's a Python implementation.
layout: post
link: https://seanblanchfield.com/python-memoize-with-expiry/
slug: python-memoize-with-expiry
title: Python Memoize with Expiry
wordpress_id: 29
tags:
- Code
- python
---

To any readers that may exist: sorry for my silence. I've been incredibly absorbed with Front Square (our new company), and the three major projects that have splashed and gone splat since November.
<!-- more -->
Anyway, so that I don't forget this blog exists, here's a tasty morsel of python for anyone who cares to use it.

In python, I have often found myself in creating a global dictionary along with a timestamp to stash relatively static database data into. In one case, for example, I cached configuration information stored in the database. This is a perfect example, since it nearly never changes, and failure to do this would result in many pointless DB hits. I generally timestamped the cache so that the application would eventually reload the data without the necessity of a restart (nice for live systems).

Memoizing describes the programming pattern of caching results returned from a function, so that any subsequent calls to the function with the same parameters will return a cached value instead of re-computing it. In python, its possible to create a function decorator/wrapper that will do this for you.

The version below is largely copied from [Django](http://www.djangoproject.com/)'s memoize (`django.utils.functional.memoize`), which is a function decorator. It adds to the implementation the ability to specify a cache timeout period, so that old entries in the cache will eventually be recomputed.

To use it, just decorate your function with it, and provide a cache object as a parameter. This object should be dictionary-like (i.e., be subscriptable). At the moment, I'm just using a global dictionary (so that in my webserver, a cache will be kept per server thread).

You can also specify a timeout in seconds (default is no timeout), and the number of parameters to key off when saving to the cache (default: all of them).

Use it as follows:

@memoize\_with\_expiry(mycache, 60, 2)
def my\_function(important\_param1, important\_param2, unimportant\_param):
  ....

Here's the implementation:

from time import time
class memoize\_with\_expiry(object):
   '''
   Modified from django.utils.functional.memoize to add cache expiry.

   Wrap a function so that results for any argument tuple are stored in
   'cache'. Note that the args to the function must be usable as dictionary
   keys. Only cache results younger than expiry\_time (seconds) will be returned.

   Only the first num\_args are considered when creating the key.
   '''
   def \_\_init\_\_(self, cache, expiry\_time=0, num\_args=None):
       self.cache = cache
       self.expiry\_time = expiry\_time
       self.num\_args = num\_args

   def \_\_call\_\_(self, func):
       def wrapped(\*args):
           # The \*args list will act as the cache key (at least the first part of it)
           # \[:None\] is equivalent to \[:\]
           mem\_args = args\[:self.num\_args\]
           # Check the cache
           if mem\_args in self.cache:
               result, timestamp = self.cache\[mem\_args\]
               # Check the age.
               age = time() - timestamp
               if not self.expiry\_time or age &lt; self.expiry\_time:
                   return result
           # Get a new result
           result = func(\*args)
           # Cache it
           self.cache\[mem\_args\] = (result, time())
           # and return it.
           return result
       return wrapped

### Update

Thanks to Villiros for pointing me to the python decorator module, which can improve things here. I've adapted one of their examples to achieve the same effect as the code above. To use it, you should make sure you have `python-setuptools` installed, and `easy_install decorator`.

The advantage of this code is that decorated functions have their docstrings and other metadata preserved.

\# This module requires decorator. Install with 'easy\_install decorator'.
from decorator import decorator
from time import time

def memoize\_with\_expiry(expiry\_time=0, \_cache=None, num\_args=None):
    def \_memoize\_with\_expiry(func, \*args, \*\*kw):
        # Determine what cache to use - the supplied one, or one we create inside the
        # wrapped function.
        if \_cache is None and not hasattr(func, '\_cache'):
            func.\_cache = {}
        cache = \_cache or func.\_cache
        
        mem\_args = args\[:num\_args\]
        # frozenset is used to ensure hashability
        if kw: 
            key = mem\_args, frozenset(kw.iteritems())
        else:
            key = mem\_args
        if key in cache:
            result, timestamp = cache\[key\]
            # Check the age.
            age = time() - timestamp
            if not expiry\_time or age &lt; expiry\_time:
                return result
        result = func(\*args, \*\*kw)
        cache\[key\] = (result, time())
        return result
    return decorator(\_memoize\_with\_expiry)