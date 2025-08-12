---
author: Sean Blanchfield
date: 2025-08-12 10:00:00
layout: post
link: https://seanblanchfield.com/irish-national-ai-championship-2025-keynote
slug: irish-national-ai-championship-2025-keynote
title: Irish National AI Championship 2025
image: /images/2025/08/irish-national-ai-championship-2025-keynote.jpg
---

I was invited to kick off the Irish national AI championship 2025, supported by Google and OpenAI, with 500 contestants from around Ireland on an intensive 2-week sprint to build innovative AI applications. In this keynote I focus on reflections from our journey so far in [Jentic](https://jentic.com), trying to build the AI-native way, and thoughts on what to build in a world where SaaS is dead, the app layer gets steamrolled, yet a world of opportunities exist.


<!-- more -->

More about [Jentic](https://jentic.com).

More about the [Irish National AI Challenge](https://techireland.org/).

Here's a video of the keynote, or feel free to scroll downfor a transcript.

<style>
.video-container {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%;
}
.video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}
</style>


<div class="video-container">
    <iframe class="video" src="https://www.youtube-nocookie.com/embed/dz7ORFUOSUA?si=kl0FrDM7I2XtKXCJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

# Transcript

Hello everyone. My name is Sean Blanchfield. I'm CEO and co-founder of Jentic, an Irish startup that is less than a year old, with €4 million in VC funding to build a platform for business AI agents to get work done using APIs and workflows. I previously cofounded a bunch of other companies, and I’m also honored to be a member of the government’s AI advisory council. Today, I’m delighted to be kicking off the **National AI Challenge 2025**.
![](/images/2025/08/slide_1.png)
**So This is exciting:** 2 weeks. 500 of Ireland’s brightest minds. There’s a technology revolution raging. You’re all here to do one thing: build something great with AI.

But, let’s be clear: If you think this is a coding competition, you're already losing. The winners here won’t be the ones who code the most or code the best. They’ll be the ones who barely code at all.

What this competition is really about is learning to build in a new way. 

I’m going to talk about two things:

![](/images/2025/08/slide_2.png)

**First**, my best effort at a playbook on how to work the AI-native way. That means using AI not as a tool, but as a *team of colleagues*. Your business planner, your researcher, your coder, your tester, your product manager. Maybe even your co-founder.

**Second**, what to build. Because not everything makes sense to build anymore. What you’re aiming for are applications that are only made possible with the arrival of AI.

If you build the AI-native way, then you’re not just going to be in with a chance to win. You’ll know how to build for the AI age — and frankly, that’s going to be your competitive edge from here on out.

## **II. Building the AI-Native Way**

---

1. ## Speed
![](/images/2025/08/slide_3.png)
The pace of AI is eyewatering, and every other day there is a major advancement. This is trickling down and speeding up all kinds of work. AI isn’t just automating coding, but it’s automating design, marketing, sales, finance \- everything \- one task or workflow at a time. You need to go fast too, or you might find the market you were aiming for has moved on by the time you get there. You need to find a way to quickly get into your market with a product and real engagement from users, and then keep on racing to stay there.

This need for speed has casualties. You can’t afford to build anything you can more quickly borrow. Use a database as a service instead of setting up your own, or use N8N to automate some business logic instead of coding it in Python. Use tools like loveable or its competitors to generate your UI. 

If you choose to build something you could have more quickly got off the shelf, it might end up being a very expensive mistake that knocks you out of the race. 

## 2\. Vibecoding
![](/images/2025/08/slide_4.png)
It’s a strange phrase, but it will do for now.  AI coding agents are already better than most human coders, and are accelerating rapidly. Maybe you're an amazing coder and can still solve harder bugs and write more beautiful code. But AI is much faster than you, knows literally everything , and you can summon an army of them at will.

So, if you catch yourself or a teammate actually typing code line by line, you need to stage an intervention immediately. 

But, it’s not just about speed. When you are building with AI coding agents, you have an opportunity to elevate yourself above the weeds, stay there, and start operating consistently at that level. When programming transitioned from assembly to high-level languages, programmers could move up a level, spend time thinking about abstract things like classes and object architecture, leaving many of the mechanical details of memory management behind. With this leap, code is the new assembly language, and we’re leaving it behind. Our unique human contribution isn’t producing code, but thinking about architecture, the product and the customer. 

You should expect this shift to be challenging. Just because you are a great coder, you might not initially be a great systems architect. Being great at that level requires an open mind, broad interests and a passion for solving problems for real people, not solving problems for their own sake. So, a bit of psychological distress as you make this transition is normal \- it just means you’re on the right track.

Practically speaking, there are phenomenal coding agents now. Cursor, Windsurf, Claude Code, OpenAI Codex, Gemini CLI, Cline, QWEN4 Coder. Some of them are IDEs with agents in them that you basically pair-program with, and the CLI ones are more like developers your delegate to. And they are all maturing rapidly.

## 3\. The new discipline of engineering
![](/images/2025/08/slide_5.png)
As you spend more time working with AI coders, you realise there’s a new discipline emerging here. They have flaws and they have superpowers. The new field is about figuring out how to deal with the flaws, leverage the superpowers, and scale up how many of them you can put to work simultaneously. If you look into the BMAD method you’ll see that people are merging agile software development with multi-agent architectures to do this. It’s an active area \- and if you jump in now, you will be on the bleeding edge. 

This often boils down to figuring out what we call “prompt chains”, where you don’t try to one-shot a big task in ChatGPT, but you break it down into phases and run each phase through the best AI for the job. You might even parallelize bits of it.  

For example, you could use a Custom GPT to write a research brief for a particular area, then get run that through 4 different deep research models to produce long-form research, which you then run through Gemini with its long context window to condense it into single report, which you then put into a thinking model to reason over to make a product requirements doc, which you then break down into user stories and an implementation and testing plan, then bring that into a coding model to implement. 

But you can do so much more than code this way. AI can write law as well as code. It can analyse leading companies’ design language to create a detailed branding and design guide, which a coding model can then follow to create a beautiful slide deck using [reveal.js](http://reveal.js). Coding with AI is a first step. You can use the same techniques for nearly anything. 

## 4\.  Clarity
![](/images/2025/08/slide_6.png)
The Gen AI revolution started off with a paper called “*attention is all you need*”. This seems to apply to us humans more than ever, not just AI transformer models.  You have limited time, limited people, and you’ve got to make every hour count. You need clarity and purpose and alignment. The enemy is anything that saps your attention or obscures your goal or confuses your internal communication. Without clarity and purpose, you may find yourself performing below the level of ChatGPT, which is a depressing place to be.

So spend some time in your team getting super clear about what your core goal is, and what you are **not going to do**. There’s still lots of unknowns and discovery ahead of you, but you all need to be pulling in the same direction. 

To maintain clarity you need to stay above the weeds  and avoid getting sucked down rabbit holes.  “Context engineering” is the new art of curating the diet of information you feed into your AI to keep its attention focused on what's important. There’s a lesson in that for all of us \- we must manage our own attention with at least as much diligence as we do with our AI’s.

**A warning:** be careful not to inadvertently use AI against each other. It is trivially easy to use AI to generate hundreds of pages of worthy analysis, but you should consider it a cardinal sin to ask anyone to spend more time reading something than it took you to create it. When you demand attention from your colleagues, it should be on actionable insights, **not** on 50 pages of freshly generated deep research. 

## 5\. Documentation
![](/images/2025/08/slide_7.png)
So where should all those long deep research papers go? They are often pure gold, and kilo-watt-hours might have been spent producing them. **But they aren’t for humans to read**; they are **fuel** for your AI. 

We’ve always produced documentation for our users, and often internal docs, and now we are producing **documentation for our AI**. In fact it’s probably the most important type, because if we can make sure our AI is well informed, then it can write the documentation for everyone else. In addition, we get a virtuous cycle, with a better informed AI producing better work, which it can then build on.

A good AI-friendly internal documentation strategy will be the hallmark of the AI-native company. Documentation is the core interface between the humans and the AI, and the core enabler for the quality of the AI’s work. We need to be able to expand on it, collaborate on it, hone it, and feed it back into the machine. In my experience so far, many of our traditional SaaS tools aren’t great for this. Standalone google docs get lost, Notion and other SaaS vendors lock data up behind their APIs. 

What is ideal from an AI’s point of view is a big folder of markdown files. The LLMs are all well trained on Markdown, and it’s a nice blend of something that both people and machines can read and write. You can put a whole folder in Git, version it, and collaborate on it there. You can drop the whole folder into a coding agent and ask it business questions, or you can upload it all to a CustomGPT or a NotebookLM, or curate it into a ChatGPT or Claude project and share that across the team. 

Similarly, if you have a lot of structured data \- e.g., you scrape or analyse a bunch of data \- I suggest putting it all into a postgres database \- self-hosted, NeonDB or whatever you like.  One big database. Over time, all structured data can go into that database instance, and any AI you have can be given access to it to answer your questions. 

## 6\. Collaboration
![](/images/2025/08/slide_8.png)
As you work together over 2 intense weeks using AI at every turn, be aware that AI is also screwing up collaboration. Collaboration is still vitally important, but the game has changed, and our tools haven’t caught up. For example, do you want to spend an hour commenting and suggesting edits on a document that was generated with AI?  Do you want to review thousands of lines of code in an AI-generated PR on github? It’s demeaning and wasteful to spend human time marking the machine’s homework. Human collaboration has to move upstream.  You can collaborate on a simple one-shot prompt in a google doc, but that doesn’t work for a prompt chain. I promise you that you will soon have two or more people on the team proudly showing off their competing AI-generated strategies, with no way to really evaluate them or compare them or tweak the information that went into the process and reliably reproduce it. 

I don’t have an answer to that one yet. I just want to say you’re not alone. We’re all figuring out at the moment, and we most likely the tools we need to be collaborating in haven’t been invented yet.

## 7\. Can I AI this?
![](/images/2025/08/slide_9.png)
The more experienced you are, the harder this is to remember to ask this question. It’s remarkable how many times the answer is “yes” and you save days of effort.

Any research work can be done by AI. Broadly speaking, anything you might hire a consultant or agency to do can be done with AI. 

For example: do a competitor analysis, monitor the market for pricing changes, make a shortlist of startup-friendly bookkeepers in Ireland, or find the top 20 VCs in London who have invested in my domain in the last 12 months along with contact details, or identify the top influencers to help market my product. Multi-modal models can literally see, which gives them the ability to analyse all kinds of images, photographs, webpages and videos, including making aesthetic judgements. You can generate music, podcasts and videos. 

## 8\. User Feedback
![](/images/2025/08/slide_10.png)
The Lean Startup Movement emphasised the importance of a fast feedback loop with user guiding the product towards market fit.  

With AI you can throw together functional minimum viable products in no time, and get those out in front of users. Users will always respond more meaningfully to something they can pick up and play with. 

Read **Running Lean**, or even better: ask your AI to summarize it for you. Then use AI to run the process and help you iterate. Generate a functional prototype and put it in front of someone. Do it on a video call and record it. Use AI to analyze the video and the transcript and work out where they fumbled.  Repeat many times. Get the AI to tell you the \#1 thing you need to fix. Basically, use AI everywhere possible to accelerate the product feedback loop. 

##  **III. What to Build (15 min)**

---

## SaaS is dead
![](/images/2025/08/slide_11.png)
SaaS had a good run, fueled by the emergence of cloud computing, and itself fuelling a massive growth in the VC industry and general digitization of business and our personal lives. Now Satya Nadella (CEO microsoft) and many others are saying SaaS is dead \- why? 

- Mainly, because **AI doesn’t need help using a database.** Most humans do. Most SaaS is just a database wrapper. If you believe that workflows currently performed by humans are going to be automated with agents, then the applications they use to do that work will disappear too. The first to go is any workflow that involves moving information between email, slack, spreadsheets and SaaS apps. Moving information from one form to another is all low hanging fruit for AI. That’s either a threat or an opportunity to you, depending on what you build.

- **Litmus test:** to think about how vulnerable a SaaS-type product is, is to imagine what it looks like if you rip off the user interface and expose the naked API underneath. Does the product make sense as a pure API (probably consumed by agents)?

- **Self-fulfilling prophecy.** VCs think on a 10 year horizon, and don’t see SaaS in that future. And they know that lots of SaaS companies mostly sell to other SaaS companies, so the end might be sudden. So they’re not funding it any more. **So it is dead**.

## Moats
![](/images/2025/08/slide_12.png)
In the age of vibecoding, all technology moats are evaporating. Network effects and marketplaces are vulnerable to user-side agents unbundling them. For example, a shopping agent can shop for you in amazon, temu, aliexpress, zalando, Etsy and a thousand shopify stores. So merchants don’t need to be on amazon any more.  There’s opportunity there for startups that hasn’t been there for a long time.

Data moats still exist, but good ones are rare. 

But it’s worth thinking hard about data, e.g.:

* Do you know where some data is locked up that you can get access to?  
* Do you have a product idea that generates data, which you can accumulate as a moat?

Either could be very valuable. Unfortunately, not all data is equally valuable. It needs to be useful, and you probably need tons of it. It needs to be special enough that competitors can’t easily synthesize similar data. 

If you do have some special data, you can monetize it by selling access to an agent that can answer questions using the dataset. You just have to be careful that competitors don’t try to exfiltrate the dataset through your agent. You don’t want your proprietary golden goose to be used to teach a competitor’s AI.

## API first
![](/images/2025/08/slide_13.png)
Whatever you build, you need to think AI-first. The world is on a path where your primary user is an AI agent, and the natural way for it to use you is over an API (it’s irrelevant if it’s REST or MCP or something else). For it to work well, you should have great APIs with multilayered design, allowing obvious goals to be accomplished in a single step via high-level calls, and allowing the AI to go under the hood and do granular operations where required. You should use OpenAPI to document your REST API in detail, and consider using Arazzo to document high-level API workflows.

You can use Jentic’s open-source “arazzo-runner” library to run the Arazzo workflows if you like. You can put MCP in front of all of this, or submit your APIs to Jentic, and test them using our open-source standard agent library. 

## Two Types of AI applications
![](/images/2025/08/slide_14.png)
There are two dominant patterns today. Software-calls-LLM, and LLM-calls software, 

**First**, software calls LLM. In other words, regular software or a hard-coded automation calls an LLM to complete some sub steps. You can do this with automation platforms like N8N or Zapier. AI gives these platforms wonderful new abilities to work with unstructured data like emails, sound and images. It’s easy to think about, and pretty safe and reliable. But it’s a bit of an incremental improvement, not a transformation, because you still need to design it like software.

**Second**, LLM calls software. The LLM is in the driving seat, and it’s in charge of deciding what the next step is. It can call regular software via APIs. This is the transformative meaning of **“agent”**. It will try to dynamically solve problems it wasn’t explicitly designed to solve, and has the potential to replace traditional software (and along with it, software engineers, and technical debt). The main problem is reliability, but that’s getting better, and is good enough in many cases.

Each has its place. Know which one you're building.

## Build what used to be impossible
![](/images/2025/08/slide_15.png)
So what should you build?  Try to build something that simply **wasn't possible** before AI —  that couldn’t have existed three years ago — and probably still doesn’t exist now.

It might be:

* An **autonomous agent** that performs a high-value business function end-to-end, replacing entire categories of SaaS.

* Something that **adapts to each user** in real time using LLM-driven UX and personalisation.

* A **data-native business**, where the product is just the mechanism for generating uniquely valuable data.

* A **fine-tuned model or specialist agent** trained on specialist knowledge in a professional niche others haven’t even looked at yet.

* A new kind of **tool or piece of infrastructure** for agents, to help them be faster, safer, or more reliable (like we’re doing at Jentic).

* **Here’s some free ideas**: solve the collaboration problem I mentioned with a new tool to help teams collaborate on prompt chains \- you could call if chaingang\! Or think about how the UX paradigm of agents \- adapting existing UX to agents is clunky and something built from the ground up to facilitate asynchronous collaboration might be great.

And here’s some tips about what **not** to build:

* Don’t build **thin wrappers** around ChatGPT or anything that your users can do in ChatGPT with a bit of effort. This kind of thing will get “steamrolled” **by general advances in AI**. If OpenAI or Google could crush it with a single feature or model release, it probably will.

* Don’t copy something you saw on Twitter or youtube unless you’re **going 10x deeper**.

* Don’t spend your time making UIs for work that agents are going to take over. 

### **Do what you know**
![](/images/2025/08/slide_16.png)
Many of the best businesses won’t come from people chasing Silicon Valley AI trends — they’ll come from people who already understand real-world problems, and now finally have tools powerful enough to solve them.

So: **look inward.**

* What’s a pain point from your previous career that’s ripe for automation?

* What  domain-specific knowledge do you already know, that you can teach an AI about?

* What customer do you know better than anyone else?

* Where have you recently seen people doing repetitive boring work?

**Do what you know**. This is your **unfair advantage**. Use AI to build the tools you wish you’d had.

## Monetisation
![](/images/2025/08/slide_17.png)
Let’s talk about money. Think about monetisation from the start.

**Payment models:**

* **Classic** recurring subscriptions via Stripe etc  
* **Usage-based:** metered billing tied to API calls, storage, or actions. Basically, charge for your north star metric.  
* **Agentic commerce:** autonomous agents initiating transactions (e.g., x402 protocol), crypto smart contracts, MCP wallets etc. 

Mostly, don’t wait until you “launch” to think about monetisation. Let it shape the product just as much as features do.

**Closing**

Let me leave you with this:

We’re at the beginning of a new era. All information technology since the printing press was about scaling distribution of information, but gen AI is the first technology that creates information. This is going to reshape software, work and all organisations. The traditional gatekeepers are gone. The incumbents are losing their competitive moats. You have equal access to the best cutting-edge technology in the world. In many cases, startups have all the advantages.  The time is now.

For the next two weeks, you’re not just competing in a hackathon. You’re exploring the frontier. You’re teaching yourself how to be an AI-native founder, architect, creator and 10x team. And if you do this right — if you build with speed, clarity, purpose — you won’t just win a prize. You’ll win your future career.

So, go build something extraordinary, and help shape the future.

Good luck. 🚀


![](/images/2025/08/slide_18.png)