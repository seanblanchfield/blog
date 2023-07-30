---
author: Sean Blanchfield
date: 2023-07-30 22:00:00
layout: post
link: https://seanblanchfield.com/inner-problem-solving-jargon/
slug: inner-problem-solving-jargon
title: Some Inner Jargon of Problem Solving
image: /images/2023/07/hyperspace-axes.png
---

I keep notes on some odd things, and one of them is ways I have of thinking about things. For one reason or another I ended up trying to write out some of these notes properly this week, but decided not to use it. Here it is for posterity.

<!-- more -->

---
## 1. Wallow in the data

Soak up information on the topic and adjacent fields. Talk to people, read, watch videos, try to write it down as prose, bullets or diagrams. Get comfortable with the language and the concepts. Accept that it takes time.

## 2. Identify orthogonal axes
Notice when two things can be viewed as alternatives on a spectrum of many possibilities. Sort ideas this way, onto a number of axes. Each axis should be *orthogonal*, in the sense that it can (ideally) be considered separately from everything else. Take note of how many axes there are, and what is at the poles of each axis. The various axes and their poles provide a mental image of the space where the problem and possible solutions exist. 

## 3. Connect the dots
The leftovers from the orthogonal axes exercise will be all the exceptions where things on different axes are not actually independent. These exceptions are the real-life dependencies between different ideas, and are like a web of threads hanging between the axes.   

## 3. Find an angle

Try to visualize the axes and the web of dependencies interlinking them, and start rotating that model around, trying to find an angle that:
- isn't a tangle of dependencies, and is easy enough to reason and communicate about
- is likely to allow you to make good iterative progress

Grapple with it for a few minutes or days until you can see an angle that looks better than the others.

## 4. Decomposition

Notice whenever one axis seems pretty independent from the others, and try to solve it separately if possible. 

When working through densest webs of dependencies, seize any opportunity to tackle one trivial piece at a time. Like a jigsaw puzzle, every piece that is solved delivers the exponential benefit of reducing both the number of remaining pieces and the difficulty of each of those pieces. 

See [Problem Decomposition](https://en.wikipedia.org/wiki/Decomposition_(computer_science)).

## 5. Short-circuit evaluation
 
Notice opportunities to optimise the problem-solving journey. If something requires three other things to be true, try to disprove just one of them and move on. It's not necessary to fully explore the options when it is sufficient to eliminate just one of them. Therefore, arrange the work to tackle the most risky propositions first.
 
 See [short-circuit evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation). 
 
## 6. Binary search

 Some work can be arranged as a binary search: rather than investigating every possibility in a linear search, we can ask questions that eliminate about half the remaining possibilities each time. This is intuitive to anyone who played a lot of [*Guess Who?*](https://en.wikipedia.org/wiki/Guess_Who%3F) as a child, but we can sometimes forget to apply the lesson as adults. Given 24 possible options, an amateur *Guess Who* player will 
 require **24 &divide; 2 = 12** guesses, but a smart player will get there in **log(24) = 4.6** guesses.
