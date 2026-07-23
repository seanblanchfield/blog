---
layout: post
title: "End of the SaaSpalooza"
date: 2026-04-28 00:00:00 +0100
categories: [ai, saas, strategy]
image: /images/2026/07/saaspocalypse/hero.png
---

In 2023, Satya Nadella declared "SaaS is dead." At the time it felt provocative. Two years later it feels like an understatement.

<!-- more -->

The story being told in most tech circles is that AI is killing SaaS. That's true, but it's incomplete. What actually happened is that two separate extinction events arrived almost simultaneously, and the second one finished what the first one started.

To understand why, you have to go back to where SaaS began.

## Three forces converge

Three moments made the SaaS era possible.

**1999:** Salesforce launched the first major Software as a Service product. The insight was simple but radical: software didn't have to be something you bought on a disc and installed. You could rent it over the internet, pay monthly, and someone else would handle the infrastructure. Capital expenditure became operating expenditure. Finance departments were delighted.

> **Where was Sean?** Just starting out in business. I co-founded [Phorest](https://www.phorest.com) in 2001 — one of the early vertical SaaS companies, and still going strong today.

**2006:** Amazon launched AWS. Suddenly the infrastructure itself followed the same model. You didn't need a server room or a data centre contract. You span up a virtual machine, paid by the hour, and span it down when you were done. Cloud computing turned infrastructure capex into opex too. Small teams could now build scalable software products without the upfront capital costs that had previously been a moat for large incumbents.

> **Where was Sean?** Living the pre-cloud version of this, scaling [Demonware](https://en.wikipedia.org/wiki/Demonware) to run the online infrastructure for Call of Duty across five data centres around the world — building our own cloud before the word existed. AWS would have changed everything for us.

**2008:** The financial crisis hit, interest rates crashed to zero, and stayed there for fourteen years. This is the bit people forget.

> **Where was Sean?** Back in SaaS, and by 2011 running a SaaS venture studio, seriously considering a move into VC. The money was flowing and the model felt unstoppable.

<figure>
<img src="/images/2026/07/saaspocalypse/slide-03.png" alt="Chart showing global VC funding, SaaS growth and cloud growth from 2005 to 2025, with ZIRP era highlighted" style="max-width:100%;border-radius:6px;">
<figcaption><em>Three trend lines, 2005-2025. Cloud kept climbing. SaaS coasted. VC went on a tear during ZIRP, then fell off a cliff.</em></figcaption>
</figure>

## ZIRP: the fuel nobody talks about

Zero Interest Rate Policy (ZIRP) meant that money was effectively free. Institutional investors who had previously been content with bonds and safe havens found themselves chasing yield anywhere they could find it. That money flowed into venture capital. The VC industry roughly tripled in size between 2008 and 2021.

And what was venture capital deploying all that free money into? Mainly SaaS. Because SaaS had something that investors in a low-yield world found irresistible: predictable, recurring revenue. Monthly subscriptions. Annual contracts. Churn rates you could model. Lifetime value you could calculate. Net Revenue Retention you could tout. The entire vocabulary of SaaS metrics was purpose-built to make these businesses legible to a financial system awash in cheap capital looking for somewhere to go.

The playbook was refined to a science: acquire users at any cost (because capital was free), lock them in with high switching costs and network effects, then harvest the recurring revenue indefinitely. Land and expand. Growth at all costs. The metrics looked beautiful in a spreadsheet. Valuations soared.

The SaaSpalooza was underway.

## The first death: ZIRP ends

In 2022, central banks started raising interest rates to fight inflation. ZIRP ended.

Almost immediately, the party stopped. VC funding fell off a cliff. The flood of cheap capital that had been inflating SaaS valuations and funding growth-at-all-costs strategies dried up. Public SaaS companies saw their valuations crushed. The multiple-on-revenue game was over. Suddenly investors wanted to see, of all things, profit.

The SaaSpalooza had been running on borrowed money, literally. When the borrowing got expensive, the music stopped.

This alone would have been a significant correction. A reckoning for overvalued businesses that had been optimising for growth metrics over economics. A lot of SaaS companies were not actually that good as businesses; they just looked good in a world where capital was free and the discount rate was essentially zero. Remove those conditions and the emperor had considerably fewer clothes.

But then the second thing happened.

## The second death: AI kills SaaS

In late 2022, just as the ZIRP era ended, generative AI arrived. The timing was coincidental but the effect was compounding: the financial conditions that had sustained the SaaSpalooza collapsed at the same moment as a new technology emerged that would undermine its entire premise. Generative AI turned out to be an existential threat to SaaS in its own right, for four distinct reasons.

### 1. Software IP has effectively disappeared

Building a successful SaaS product was never just about writing the code. The hard part was everything else: figuring out that there was a market, finding the right pricing, educating customers who didn't know they had the problem you were solving, iterating through the failures until the thing actually worked as a business. That process takes years and costs founders and early teams enormously in time, money and stress.

The reward for all that was supposed to be a defensible product. By the time you had product-market fit, you had a working system, accumulated knowledge, and a head start that competitors would struggle to close.

AI coding agents have largely eliminated that head start. A reasonably technical person with access to Claude Code or Cursor can now build a working version of most SaaS products in days. They don't need to go through your years of discovery — they can observe what you built, what works, what customers pay for, and replicate the implementation cheaply. The blood, sweat and tears of finding a working model are yours. The benefit of having found it is now everyone's.

Worse, it is not just competitors you need to worry about. Your own customers can copy you if they like. A business that pays you $500 a month for a workflow tool and has a technical employee with a coding agent can now ask themselves whether they want to keep paying, or spend a week building their own version, configured exactly how they want it. Many will keep paying — switching costs and inertia are real. But the calculus has shifted, and the trend is not in your favour.

### 2. Agents don't need a UI to use a database

Here is the short version: AI doesn't need help using a database. Most humans do. Most SaaS is just a database wrapper.

The user interface of a SaaS product exists for one reason: to make the underlying data and logic legible to a human. Strip it away and almost every SaaS product is a database with an API on top. Create, Read, Update, Delete. The beautiful UI, the polished UX, the carefully designed workflows — all of it is a translation layer between a human brain and a database.

<figure>
<img src="/images/2026/07/saaspocalypse/slide-06.png" alt="Diagram showing a SaaS UI stripped back to reveal REST APIs, which are themselves just database CRUD operations" style="max-width:100%;border-radius:6px;">
<figcaption><em>Rip off the UI, expose the API, and underneath almost every SaaS product is a database with Create, Read, Update, Delete operations. The UI exists to make that legible to a human. Agents don't need it.</em></figcaption>
</figure>

AI agents don't need that translation layer. When you have an agent working on your behalf, it doesn't open a browser, navigate to your CRM, click through a contact record and fill in a form. It calls the API directly. It doesn't care about your onboarding flow. It doesn't need a dashboard. Per-seat pricing becomes absurd when the "seat" is occupied by a software process that never sleeps, never needs training, and can operate dozens of instances simultaneously.

This is why the shift to outcome-based pricing is not just a trend: it is an inevitability. The per-seat SaaS model assumed a human on every seat. That assumption is no longer safe.

> **The litmus test.** How vulnerable is any given SaaS product to this? Imagine ripping off the user interface and exposing the naked API underneath. Does the product make sense as a pure API, consumed by agents rather than humans? If yes, it is at serious risk. If the value is genuinely in the network, the data, or something only a human can navigate — there may be more runway. Most products, if you're honest, pass the first test.

### 3. The moats are gone

Even if you accept the UI argument, you might think SaaS companies have other defences. They do, but they are weaker than they look.

**The technology moat** was always somewhat illusory — good engineers could always rebuild most products — but it was real enough when building took years and cost millions. AI coding agents have collapsed the time and cost dramatically.

**Network effects and marketplaces** were a stronger moat. If all your suppliers are on Platform X, leaving is genuinely painful. But AI agents are starting to unbundle these too. An agent that can negotiate directly, match buyer to seller, and execute transactions doesn't need a marketplace platform as an intermediary in the same way a human does. This one is slower-moving, but the direction is clear.

**Data moats** are the most frequently cited defence. Surely the accumulated data from thousands of customers makes incumbents impossible to displace? In practice, proprietary data moats are rarer and shallower than claimed. Most SaaS companies are sitting on usage data that is valuable but not irreplaceable. The companies with genuinely deep, hard-to-replicate data are the exceptions.

What's left? Brand, distribution, and regulatory compliance. These are real. But they are the advantages of incumbency, not of innovation — and they are advantages that startups by definition do not have.

### 4. A self-fulfilling prophecy

There is a more prosaic reason the SaaSpalooza is over, and it is the one that most directly affects founders and investors right now.

VCs think on a ten-year horizon. And on a ten-year horizon, most of them no longer see SaaS. If you believe that workflows currently performed by humans are going to be automated by agents — and the evidence is mounting that they will be — then the applications humans use to perform those workflows will disappear with them. The first to go is anything that involves moving information between email, Slack, spreadsheets and SaaS apps. That is the majority of office software. Low-hanging fruit for AI.

Once you accept that logic, you stop funding SaaS. And here is where it becomes self-fulfilling: a significant portion of SaaS companies' customers are other SaaS companies. They sell to each other. HR software, payroll, project management, CRM, finance tools — the customer base is disproportionately the tech industry itself. When investment dries up across the sector simultaneously, the cascade is faster than in industries with more diverse demand.

The exit market has closed as a result. SaaS as an asset class worked because there was a functioning exit pipeline: build a product, grow ARR, achieve a sale or IPO at a healthy multiple, return capital to investors. The multiples compressed when rates rose. The IPO window largely closed. Strategic acquirers got cautious. The pipeline clogged.

Without exits, venture capital cannot return money to its LPs. Without returns, LPs stop committing to new funds. Without new funds, VCs stop deploying. Without deployment, founders don't get funded. The machine runs in reverse.

This is not just a cyclical correction. The underlying conditions that made SaaS an exceptional vehicle for venture returns have structurally changed. They are not coming back in the same form.

SaaS solutions can still be successfully built — probably in hyper-vertical domains where the founder has deep domain expertise and an existing network. But those businesses are unlikely to attract VC backing or grow like the unicorns of the 2010s. They will be bootstrapped, profitable, and small by the standards of the last decade. That is not nothing. But it is not the SaaSpalooza.

## What comes next

<figure>
<img src="/images/2026/07/saaspocalypse/slide-09.png" alt="Graveyard illustration with headstones for SaaS, MRR, CAC, LTV, MAU/DAU, Churn and GTM motion" style="max-width:100%;border-radius:6px;">
<figcaption><em>"Dear SaaS, it's not you, it's us. – The Agents."</em></figcaption>
</figure>

None of this means software is dead, or that building products is dead, or that there is no money to be made. It means the specific conditions that made the SaaSpalooza possible — free capital, human-facing UIs as the only interface paradigm, high switching costs from network effects and integrations, recurring per-seat revenue as the universal business model — have changed.

The companies that will thrive are the ones that have genuinely useful knowledge or capability that an agent can leverage, not the ones that built a moat out of UI complexity and switching costs. The business model of the next decade is not "rent my software to your employees." It is "deliver outcomes into your agent fleet."

The SaaSpalooza lasted from 2008 to 2022 — fourteen years. It was a remarkable run, funded by historically anomalous conditions. It produced real value, real products, and real companies. It also produced a lot of overvalued businesses optimised for metrics rather than economics, and a venture ecosystem that confused "this grows well in a zero-interest-rate environment" with "this is a good business."

Both died in 2022: the financial conditions that sustained it, and the user paradigm it was built on. The timing was not a coincidence. The same technological shift that gave us generative AI also gave us the inflation that ended ZIRP. The world changed at both ends simultaneously.

SaaS is dead. The agents are already through the door.
