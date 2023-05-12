---
author: Sean Blanchfield
comments: true
date: 2011-04-24 12:07:09+00:00
layout: post
link: https://seanblanchfield.com/logging-unhandled-exceptions-in-actionscript/
slug: logging-unhandled-exceptions-in-actionscript
title: Logging Unhandled Exceptions in Actionscript
tags:
- Actionscript3
- Code
- Tech
---

When an error occurs in your flash application, and is not handled, the Flash runtime will cross its fingers, ignore it, and try to struggle on. Unfortunately, an unhandled error will probably leave your client in an unstable state, and ultimately compromise the user experience in a way that may be very difficult to diagnose.

<!-- more -->

What you really want to do is have a default handler that will receive any such exceptions, that then logs them along with useful info (such as a stack trace) to your server for later analysis. Unfortunately, the ability to register a default handler like this is only supported in the 10.1 runtime and later, which only about [85% of clients have as of this writing](http://www.adobe.com/products/player_census/flashplayer/version_penetration.html). Nonetheless, 85% of unhandled errors caught is better than none, so its worth doing.

The main difficulty implementing this is that the relevant API ([LoaderInfo.uncaughtErrorEvents](http://help.adobe.com/en_US/FlashPlatform/beta/reference/actionscript/3/flash/events/UncaughtErrorEvent.html)) is only available when you are targeting your build at the 10.1 runtime, but you probably want to target 10.0 to benefit from its higher penetration. The trick to avoiding compiler errors is to only access `uncaughtErrorEvents` _dynamically_.

There are two kinds of errors to be aware of: those of type `Error` (which would be known as an `Exception` in most other languages) and those of type `ErrorEvent`. You can think of an `ErrorEvent` as an asynchronous replacement for an exception. `Error`s are only useful for reporting errors that synchronously occur during function execution. If your function does something asynchronous (such as access a network resource), you can't use an exception to report errors that happen after the initial function call. Therefore, when accessing an API with asynchronous functionality, you will probably use try...catch blocks to handle `Error`s that occur synchronously, and register a handler for any `ErrorEvent`s that occur asynchronously.

The code below is the best I could do. It dynamically inspects the runtime to see if the appropriate API is there (which it will be on 85% of clients running Flash 10.1+). It compiles with the 10.0 runtime, but only does its work if the `uncaughtErrorEvents` object is available, which indicates the client is on Flash 10.1 or later.

``` actionscript
protected function recordUncaughtErrors(logger:Function):void
{
    // Define the handler.
    function uncaughtErrorHandler(event:ErrorEvent):void
    {
        // Prevent the default error handling behavior for unhandled errors (e.g., ugly stack trace).
        event.preventDefault();
        var type_name:String = ObjectUtil.getClassInfo(event['error']).name;
        // Figure out if it is an Error, ErrorEvent or randomly thrown Object.
        if(event.hasOwnProperty('error'))
        {
            if(event['error'] is Error)
            {
                var error:Error = event['error'];
                logger("Uncaught Error", error.name, error.toString(), error.getStackTrace());
            }
            else if(event['error'] is ErrorEvent)
            {
                var error_event:ErrorEvent = event['error'];
                logger("Uncaught ErrorEvent", type_name, error_event.type);
            }
            else
            {
                logger("Thrown Object", type_name, "");
            }
        }
    }
    // Register for uncaught errors.
    if(this.contextView.root.loaderInfo.hasOwnProperty('uncaughtErrorEvents'))
    {
        // Get an instance of the uncaughtErrorEvents object. We do this in a way that will compile in runtimes < 10.1.
        var uncaughtErrorEvents:IEventDispatcher = IEventDispatcher(this.contextView.root.loaderInfo["uncaughtErrorEvents"]);
        // Have to register for the literal string name of the event, because we cannot import
        // UncaughtErrorEvent to access its UNCAUGHT_ERROR property.
        uncaughtErrorEvents.addEventListener("uncaughtError", uncaughtErrorHandler);
    }
}
```

Note that this code logs three different kinds of things:

*   thrown `Error`s (exceptions that are synchronously raised during function calls, which make it all the way up the stack without being handled). A stack trace is logged for these.
*   thrown `Object`s that are not `Error`s. These are logged, but without a stack trace, which is not available. You really shouldn't be throwing objects!
*   dispatched `ErrorEvent`s, which are dispatched after an asynchronous function call completes. Only those `ErrorEvent`s that no handlers have been registered for will be caught here, however `ErrorEvent`s dispatched through custom dispatchers won't be caught at all. This is because the `LoaderInfo.uncaughtErrorHandler` has no idea of their existence.