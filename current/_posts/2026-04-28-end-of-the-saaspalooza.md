---
layout: post
title: "End of the SaaSpalooza"
date: 2026-04-28 00:00:00 +0100
categories: [ai, saas, strategy]
image: /images/2026/07/saaspocalypse/hero.png
---

In late 2024, Satya Nadella declared "SaaS is dead." I'm semi-proud getting there first, preaching it from the stage in Dogpatch Labs in Dublin at every opportunity during the first half of the year. But now it feels like an understatement.

<!-- more -->

It's true, but it's incomplete. What is actually happening is two separate extinction events arriving at the same time.

Let's put it in context and go back to where SaaS began... and I'm just old enough to have been there at the time.

## Three forces converge

### 1999

Salesforce launched the first major Software as a Service product. Software didn't have to be something that came on a disc. You could rent it over the internet, pay monthly, and someone else would handle the infrastructure and upgrades. CapEx became OpEx and CFOs were delighted.

> **Where was Sean?** Just starting out in business. I co-founded [Phorest](https://www.phorest.com) in 2001 — one of the early vertical SaaS companies, and still going strong today.

### 2006

Amazon launched AWS. Suddenly the infrastructure itself followed the same model. You didn't need a server room or a data center colo. Virtualized servers were available on-demand, paid by the hour. Cloud computing turned infrastructure capex into opex too. Now small teams could follow in Salesforce's footsteps without any serious upfront capital.

> **Where was Sean?** We were already running the backend for Call of Duty in [Demonware](https://en.wikipedia.org/wiki/Demonware), scaling our own cloud up to thousands of servers in five sites around the world. AWS would have been handy!

### 2008 
The financial crisis hit, the start of Zero Interest Rate Policy to stimulate recovery, which stayed in place for fourteen years. This is the bit most people don't connect the dots to.

> **Where was Sean?** Back at SaaS, and by 2011 running a SaaS venture studio, seriously considering a move into VC. The money was flowing and the model felt unstoppable.

<figure>
<img src="/images/2026/07/saaspocalypse/slide-03.png" alt="Chart showing global VC funding, SaaS growth and cloud growth from 2005 to 2025, with ZIRP era highlighted" style="max-width:100%;border-radius:6px;">
<figcaption><em>Three trend lines, 2005-2025. Cloud kept climbing. SaaS coasted. VC went on a tear during ZIRP, then hit a wall.</em></figcaption>
</figure>

## ZIRP: the fuel nobody talks about

Thanks to Zero Interest Rate Policy (ZIRP), institutional investors who had previously been content with bonds started reallocating capital to wherever they could find some yield. A lot of it flowed into venture capital. The VC industry roughly tripled in size between 2008 and 2021.

And VC suddenly had a great story to tell. SaaS had something that investors in a low-yield world found irresistible: capital-efficient, predictable, recurring revenue. Monthly subscriptions. Churn rates you could model. Lifetime value you could calculate. Net Revenue Retention you could tout. The entire vocabulary of SaaS metrics was purpose-built to make these businesses legible to a financial system awash in cheap capital looking for somewhere to go.

The playbook was refined to a celebrated science: acquire users at any cost (because capital was free), lock them in with high switching costs and network effects, then harvest the recurring revenue indefinitely. Land and expand. The metrics looked beautiful in a spreadsheet. Valuations grew.  An industry of startups, accelerators and VCs started to harmonize, and the SaaSpalooza was underway.

## The first death: ZIRP ends

By 2022 the party was at fever pitch, and central banks started raising interest rates to fight inflation. The music was rudely stopped, and tech valuations crashed. 

It was a double whammy for VCs. First, they massive holes were blown through their portfolios as previous investments in unicorns and decacorns were sharply written down. Then, nursing that hangover, they found they couldn't raise their next funds, as capital flowed back to bonds. 

But then...

## The second death: AI kills SaaS

In late 2022, just after tech crashed, generative AI arrived. The timing was coincidental but brutal: the financial conditions that had sustained the SaaSpalooza collapsed at the same moment as a new technology emerged that would undermine its entire premise. Generative AI turned out to be an existential threat to SaaS in its own right, for the following four reasons.

### 1. Software IP is defunct

Building a successful SaaS product was never about the code. The hard part was everything else: figuring out that there was a market, finding the right pricing, educating customers who didn't know they had the problem you were solving, iterating through the failures until the thing actually worked as a business. The search for a repeatable business model cost serious time, stress and money. The reward for all that was supposed to be a head start that competitors would struggle to close.

AI coding agents have basically eliminated that head start advantage. The first mover spills blood, sweat and tears on finding a working business model. Once publicly demonstarted, AI can build a faithful copy in a day or two (sometimes an hour or two). 

Worse, it is not just commoditization you need to worry about. Your own customers have AI too! A business that pays you $500 a month for a subscription just needs to spend a day rolling their own version, this time tailored precisely to them. 

Even a patent portfolio won't save you here. A company that builds an internal replica of your product, and never resells it, is essentially unreachable. You'd have no way to know it happened, no way to prove it, and in the US and EU you have no damages to claim even if you could. The patent was always a weapon against competitors who wanted to sell something competing with yours. It was never a defense against your own customers rolling their own. 



### 2. Agents don't need a UI to use a database

Most SaaS products exist to help humans perform a workflow on top of a database. Strip the UI away to expose the naked REST API endpoints, and you'll often find its pretty simple: Create, Read, Update, Delete. 

Most people can't write SQL, and need a good UI instead. But AI speaks SQL fluently. In fact, it's much more reliable and efficient with machine interfaces than with user interfaces. Beautiful UX only gets in its way. 

<figure>
<img src="/images/2026/07/saaspocalypse/slide-06.png" alt="Diagram showing a SaaS UI stripped back to reveal REST APIs, which are themselves just database CRUD operations" style="max-width:100%;border-radius:6px;">
<figcaption><em>Rip off the UI, expose the API, and underneath almost every SaaS product is a database with Create, Read, Update, Delete operations. The UI exists to make that usable for normal people. Agents prefer to skip it.</em></figcaption>
</figure>

> **The litmus test.** How vulnerable is any given SaaS product to this? Imagine ripping off the user interface and exposing the naked API underneath. Does the product still have a right to exist as a pure API, or does it seem like a trivial database wrapper? 

### 3. The moats are gone

**The technology moat** was always a bit mushy (good engineers could always rebuild most products) but it was real enough when building took years and cost millions. AI coding agents have collapsed the time and cost to near zero.

**Network effects and marketplaces** were a stronger moat. But AI agents can unbundle this. A personal agent can hang out in all the social networks and funnel interesting messages back to you directly. Suddenly, you don't need to go to LinkedIn any more, and you don't need to be on the same platform as your friends. And when you go shopping, your agent can tirelessly scour Amazon, AliExpress, Temu, Shein, Shopify, classified, and everywhere else... and merchants can choose to sell wherever they like knowing that their customers will find them there.
This one is slower-moving, but the direction is clear.

**Data moats** are great if you got one, but good ones are hard to find. In practice, most data is not truly special, and comparable data can be found from other sources. Given just a small sample, more can be synthesized. And even when you have truly proprietary data, it's a challenge to monetize it while simultaneously keeping it secret. Even LLM training data is now routinely extracted through distillation attacks. So "build a data moat" is a not a plan, but if you've somehow got one, cherish it.

What's left? Brand, distribution, and regulatory capture. These are real. But they are the advantages for the incumbents, not the disruptors.

### 4. A self-fulfilling prophecy

VCs think on a ten-year horizon, and most of them no longer see SaaS in that future. So they have stopped funding SaaS, and arguably have rotated away from software in general. So even if SaaS isn't dead yet, the funding is.

And this might be leading to a kind of colony collapse. SaaS companies are each other's best customers. VCs love them to sell to each other, to keep the capital circulating, creating $10 of revenue for every $1 of capital. When SaaS companies cut spending, the rate of collapse might take everyone by surprise.

SaaS solutions can still be successfully built, probably in hyper-vertical domains where the founder has deep domain expertise and an existing network. But those businesses are unlikely to fit the venture capital funding path, or to grow like the unicorns of the 2010s. They will be bootstrapped, might make the founders rich, but be small by the standards of the last decade. 

## What comes next


The SaaSpalooza lasted from 2008 to 2022 for fourteen years. That's a long enough time that lots of people have only known that bull market during their careers, and can't figure out what the hell is happening right now. During that period, a huge system of playbooks, startup culture, founder lore, metrics, state supports and interventions was established about how to build a technology business. 

Those playbooks now need to be thrown out the window. What made sense during SaaSpalooza won't work now that gravity has been turned back on, investors expect profit, and AI is turning all conventional wisdom upside down. It's time to write some new playbooks!


<figure>
<img src="/images/2026/07/saaspocalypse/slide-09.png" alt="Graveyard illustration with headstones for SaaS, MRR, CAC, LTV, MAU/DAU, Churn and GTM motion" style="max-width:100%;border-radius:6px;">
</figure>
