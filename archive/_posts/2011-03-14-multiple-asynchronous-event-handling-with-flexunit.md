---
author: admin
comments: true
date: 2011-03-14 13:12:30+00:00
layout: post
link: https://seanblanchfield.com/multiple-asynchronous-event-handling-with-flexunit/
slug: multiple-asynchronous-event-handling-with-flexunit
title: Multiple asynchronous event handling with Flexunit
wordpress_id: 52
tags:
- Actionscript3
- Code
---

I had to write this down somewhere, now I've got it figured out. I've been banging my head against the screen for the last day and a half in work trying to figure out how to get a Actionscript unit test do what I want.
<!-- more -->
Here's the problem: The class is expected to fire a number of similar events, with slightly different payloads. Using flexunit you can tell the test to wait for these events to complete, and handle them with some additional test code. So far, so good. However, I was finding that the first event would fire _all_ the handlers, instead of just the first. When the second event fired, it wouldn't get handled (because its handler was "consumed" by the first event).

The asynchronous event handling mechanism in flexunit has a bit of a strange and badly documented behavior, which I've figured out through blind testing. In short, an event that fires during a test will be handled by every matching handler, in order, until it comes to a handler with a different event type. All the handlers it hits along the way will be consumed (I'm mentally picturing them getting shifted off the front of a FIFO queue, although I haven't actually checked the source code).

Consider the following example:
``` actionscript
public static const FIRE\_EVENTS\_TIMEOUT:int = 1000;
\[Test(async, timeout="1000")\]
public function fireEvents():void
{
    function eventHandler(event:Event, passThroughData:Object=null):void
    {
        trace('Received event\_number: ' + passThroughData.event\_number);
    }
    Async.handleEvent(this, this.instance.eventDispatcher,
                            MyEvent.EVENT\_NAME,
                            eventHandler,
                            MyTest.FIRE\_EVENTS\_TIMEOUT,
                            {'event\_number':0});
    Async.handleEvent(this, this.instance.eventDispatcher,
                            MyEvent.EVENT\_NAME,
                            eventHandler,
                            MyTest.FIRE\_EVENTS\_TIMEOUT,
                            {'event\_number':1});
    Async.handleEvent(this, this.instance.eventDispatcher,
                            MyEvent.EVENT\_NAME,
                            eventHandler,
                            MyTest.FIRE\_EVENTS\_TIMEOUT,
                            {'event\_number':2});
    // Fires 3 "MyEvent.EVENT\_NAME" events.
    this.instance.doAsyncEventFiringStuff();
    trace('FUNCTION EXITING... SHOULD WAIT FOR EVENTS...');
}
```

The `doAsyncEventFiringStuff()` function outputs a trace statement with every event fired. Running this test gives the following trace:

``` actionscript
FUNCTION EXITING... SHOULD WAIT FOR EVENTS...
Dispatching event number 0
Received event\_number: 0
Received event\_number: 1
Received event\_number: 2
Dispatching event number 1
Dispatching event number 2
```

As you can see, the eventHandler got called 3 times for the 1st event, and the next 2 events didn't get handled at all. What basically happened is that flexunit got the first event, looked in its FIFO queue of event handlers, and (starting at the front of the queue) called all of them that matched the event type. If we changed line 19 to reference a different event type, we would have got:

``` actionscript
FUNCTION EXITING... SHOULD WAIT FOR EVENTS...
Dispatching event number 0
eventHandler. event\_number: 0
eventHandler. event\_number: 1
Dispatching event number 1
Dispatching event number 2
```

(at which point the test would fail with a "Asynchronous Event Received out of Order" error).

The solution to this conundrum is to chain the event handler registration. That is, register the handler for event #2 in the handler for event #1, (similarly) register handler #3 in handler #2.

The code below shows this solution. Also note the lengths that it goes to avoiding the use of the `this` keyword inside the nested functions ("this" doesn't make it into nested function closures in Actionscript).

``` actionscript
public static const FIRE\_EVENTS\_TIMEOUT:int = 1000;
\[Test(async, timeout="1000")\]
public function fireEvents():void
{
    var event\_dispatcher:\* = this.instance.eventDispatcher;
    var test\_class:\* = this;
    function eventHandler0(event:Event, passThroughData:Object=null):void
    {
        trace('Received event\_number: ' + passThroughData.event\_number);
        // Register handler for next event
        Async.handleEvent(test\_class, event\_dispatcher,
                                    MyEvent.EVENT\_NAME,
                                    eventHandler1,
                                    MyTest.FIRE\_EVENTS\_TIMEOUT,
                                    {'event\_number':1});
    }
    function eventHandler1(event:Event, passThroughData:Object=null):void
    {
        trace('Received event\_number: ' + passThroughData.event\_number);
        // Register handler for next event
        Async.handleEvent(test\_class, event\_dispatcher,
                                    MyEvent.EVENT\_NAME,
                                    eventHandler2,
                                    MyTest.FIRE\_EVENTS\_TIMEOUT,
                                    {'event\_number':2});
    }
    function eventHandler2(event:Event, passThroughData:Object=null):void
    {
        // No more events expected.
        trace('Received event\_number: ' + passThroughData.event\_number);
    }
    Async.handleEvent(test\_class, event\_dispatcher,
                                MyEvent.EVENT\_NAME,
                                eventHandler1,
                                MyTest.FIRE\_EVENTS\_TIMEOUT,
                                {'event\_number':0});

    // Fires 3 "MyEvent.EVENT\_NAME" events.
    this.instance.doAsyncEventFiringStuff();
    trace('FUNCTION EXITING... SHOULD WAIT FOR EVENTS...');
}
```

This finally gives us the desired outcome, albeit at the expense of readability:

``` actionscript
FUNCTION EXITING... SHOULD WAIT FOR EVENTS...
Dispatching event number 0
Received event\_number: 0
Dispatching event number 1
Received event\_number: 1
Dispatching event number 2
Received event\_number: 2
```