---
author: Sean Blanchfield
comments: true
date: 2011-07-30 11:48:00+00:00
layout: post
link: https://seanblanchfield.com/taking-software-seriously/
slug: taking-software-seriously
title: Taking Software Seriously
tags:
- Code
- Enterprise
---

I often find myself struggling to communicate to non-geeks just how complicated software engineering is, probably because there's no familiar lines of work that are any way comparable. There's a danger that I often end up looking like I have an even bigger head than previously imagined, going to such lengths to convince everyone that my field is more special that theirs, but I feel compelled to correct the attitudes of the multitude in business who think that programmers are glorified typists who should get back in line.

<!-- more -->

Three reasons you should read this post:

*   Bespoke software is mission critical to most modern businesses, but they haven't yet acknowledged it
*   Most modern businesses have zero understanding of the work of software engineers, and mismanage them terribly
*   I'm a bit of a geek and I love talking about computers

## Here's the Spiel

![The files are IN the computer??](/images/2011/07/zoolander_imac_1-300x188.jpg){: .captioned .right-half}


Software is innately incredibly complicated, and preventing it from getting too complicated is even more complicated. It's really really complicated. And worse, it's invisible. You can't see any of the moving parts: in software these are the operations that the processor performs on data in memory, and occur via electrical signals zipping about on an unimaginably small scale at an unbelievable speed. Unlike other engineers, programmers are unable to stand back from their invention, run it a little bit, and take in everything that's happening. To re-iterate:

*   it's invisible
*   it all happens millions of times faster than you can form a single thought
*   it's generally so complicated that you'd be unable to assimilate the whole system even if you could see it.

![Inside the mind of a programmer](/images/2011/07/inception13.jpg){: .captioned .right-half}

Because of this, the key skill in programming is an overdeveloped aptitude for [spatial-temporal reasoning](http://en.wikipedia.org/wiki/Spatial-temporal_reasoning "Spatial-Temporal Reasoning"). A programmer has in his/her head a mental model of all the components of the system, and how they interact with each other. To program effectively, you've got to be able to experiment with that mental model and play out the consequences. It can take a while to build up this mental model, and get it ready for use. For me, the experience is easiest to compare to walking around a familiar city. You know where the streets are, you've got an idea of where to find different kinds of things you might need. But it takes a bit of effort to actually navigate to your destination. Distractions don't help. It's like trying to get your Christmas gift shopping all done in one day: you've got 30 shops to visit, not enough time, and you've got to plow through the human crush to get from one to the other.

So much for this Inception-esque mental city of your most recent software project. How about actually getting into the city in the first place? To me, it's like the city maps for whatever software projects I'm working on are in storage somewhere. At the start of the day, I need to get the relevant map out, re-familiarize myself, and kind of load it all into RAM. This is why a distraction, like [an impromptu meeting or phone call]({% link archive/_posts/2011-07-13-the-energon-methodology.md %}), is so negatively received by programmers: it completely blows their concentration, and everything needs to be reloaded back into memory afterwards ([a process that takes 15-25 minutes](http://www.amazon.com/Peopleware-Productive-Projects-Teams-Second/dp/0932633439)).

## Is it really that complicated?

You might be saying, yeah, yeah, so it's invisible mental work that takes concentration, but is the problem itself really so complicated? For example, writing well is also a pure mental activity that takes a lot of concentration. Well, in fact, writing well is really hard, and writers command my complete respect. But software is different. A text, when it is written, is linear, goes in one direction, and doesn't branch out, loop around, or have bugs that cause it to crash. While it certainly takes an enormous amount of imagination and heavy mental lifting to write a novel, what is eventually produced is static, not a live system. Software _is_ a live system, and when running, can have more outcomes than a game of chess (i.e., [more than there are atoms in the universe](http://en.wikipedia.org/wiki/Shannon_number)). For software to be this bad, it is probably either intentionally running a simulation (such as [Conway's Game of Life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life)), or is badly written or maintained, such as legacy software run amok (typical in banks, for instance).

The reason for this complexity is that software does cool things by reacting to input. It may decide to repeat an operation a number of times, or it may decide to jump to a different kind of operation altogether. The actual number of paths that software may take when its running is normally very large, and may in fact not have an upper bound.

Software engineering is mainly about trying to get this situation under control: it's about controlling complexity. To help us, we employ all kinds of concepts. [Cyclomatic Complexity](http://en.wikipedia.org/wiki/Cyclomatic_complexity) measures the number of independent execution paths of software, and we even have our very own [cute versions of the thermodynamics laws](http://www.artima.com/forums/flat.jsp?forum=106&thread=8248):

*   Zeroth Law. Change is Unavoidable
*   First Law. Complexity will be Conserved
*   Second Law. Software Complexity tends to Maximum Entropy

The question of the number of possible paths through running software is analogous to the question of how many games of chess might exist, and is nice to think about. But it focuses on intentional behavior, and fails to grasp some crucial gotchas that are the source of unexpected software behavior and bugs. I prefer to wonder: _how many potential interactions are there between parts of my program?_ Roughly speaking, this is the **number of ways that things can go wrong**. Maybe one component directly affects 5 others, or maybe 10 components all interact with one shared common component, and therefore all indirectly interact with each other (99 possible interactions right there).

Realistically, it would be a daunting challenge to map out all the possible interactions inside anything but the most trivial program, but we can make some generalizations. Without constant care, attention and discipline, a software project will grow into a monolith, without any sensible modularization. This is typical in companies that don't consider software to be a core competency (I'm looking at you, banks). In this kind of software, every piece of functionality may have a side-effect on any other piece of functionality. Consider a piece of legacy software maintained in a finance organization who doesn't take their software seriously. It has been worked on continuously since 1991, with bits added willy nilly in various languages du jour, by staff and contractors who have come and gone. No one understands how it actually works, and everyone is afraid to touch it, in case one of its appendages in another continent blows up. It's been growing in size at a constant rate, it has not been properly managed, and therefore has become exponentially complicated: 

![Monolithic Software Complexity vs Time](/images/2011/07/chart_1-2.png){: .captioned}


To produce this chart, I assumed that 60K lines of code were added each year, and that (on average) every 200 lines constituted a component that might interact with another component. This would be typical of a fairly modest team working constantly on the software, with few consistent software engineering practices in place. By year twenty, there are 50 million potential interactions within the codebase - no wonder the team is scared to muck with it!

This scary example considers every 200 lines of code as an indivisible unit, but the reality is much scarier. A single line of code can contain a large number of bugs, and within any such chunk of code there may be a large number of potential execution paths, thanks to loops and if-statements, and other conditional logic. There's enough at this level to keep the average programmer very busy, leaving no time to consider the larger issues of project complexity.

So how complicated is this in real terms? I'm not sure, but I'd hazard to guess that it's possibly on a par with a decent sized space station: 


![Sean's estimate: about 50 million possible component interactions, about the same as your bank's payroll software.](/images/2011/07/iss_0.jpg){: .captioned}

A more modest project, one that's younger, or perhaps better managed, will presumably have far fewer interacting pieces. My unscientific quess is that the typical young or well-managed software project is about as complicated as a helicoper packing a lot of onboard gadgets, such as Airwolf.

![Airwolf: about 1m interacting parts. About the same as your web app.](/images/2011/07/airwolf.jpg){: .captioned}

It's worth noting that not only are the programmers trying to invent and build a helicopter from scratch, but they are expected to ensure it flies first time.

## Managing Complexity

The real challenge of software engineering isn't getting those 200-line components working. That's difficult and skilled work, but there's only so many new features you cram into a product before before you hit a wall of [technical debt](http://en.wikipedia.org/wiki/Technical_debt). The bigger challenge is to arrange the project and future development in a way that limits the potential unwanted interaction between subsystems. This is where software becomes art, and mental visualization of complex architectures combine with gut instinct and intuition. To extend the metaphor, consider it like city planning: will it be good or bad to split the city up this way, or that? What will happen if you build a certain thoroughfare, and what back alleys, side streets and unexpected activities will spring up as a consequence? These are questions we try to approach scientifically, but which are too complicated to answer purely analytically. The best programmers spend their time thinking about these things, and don't append features to a product until they've granted themselves planning permission.

The bad news is for the banks and other organisations that have accidentally built space stations. The task of refactoring large legacy systems to try and reduce their complexity is basically beyond human ability. The only choice seems to be to rebuild the systems from the ground up, but this too is such a large task that by the time its done, it would be outdated. These mission-critical software systems that no single person understands are major risks to these businesses. They cannot stop to rebuild them, nor can they continue to extend them to match the functionality of smarter competitors.

The lesson is to not let your own company fall into that trap. Chances are that your company primarily processes information. This is true of nearly every company on the web, all banks, all insurance companies and all media companies. Software should now be a core competency, because it speaks directly to your ability to operate your business. The software engineers that work on your software systems have an incredibly important and challenging job to do. Failure to recognize this, hire good people, or to allow them to do their jobs correctly, means that in a few years, your business systems will crash into a wall of technical debt, and your business will hit the wall.

![Hit the Wall](/images/2011/07/car_in_wall.jpg){: .full-width}
