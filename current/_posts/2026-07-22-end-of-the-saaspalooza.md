---
layout: post
title: "End of the SaaSpalooza"
date: 2026-07-22 00:00:00 +0100
categories: [ai, saas, strategy]
image: /images/2026/07/saaspocalypse/hero.png
---

In 2023, Satya Nadella declared "SaaS is dead." At the time it felt provocative. Two years later it feels like an understatement.

<!-- more -->

The story being told in most tech circles is that AI is killing SaaS. That's true, but it's incomplete. What actually happened is that two separate extinction events arrived almost simultaneously, and the second one finished what the first one started.

To understand why, you have to go back to where SaaS began.

## The golden age that almost wasn't

Three moments made the SaaS era possible. I was there for all three, which is part of why I feel qualified to call time on them.

**1999:** Salesforce launched the first major Software as a Service product. The insight was simple but radical: software didn't have to be something you bought on a disc and installed. You could rent it over the internet, pay monthly, and someone else would handle the infrastructure. Capital expenditure became operating expenditure. Finance departments were delighted. I was just starting out in business around this time, and co-founded [Phorest](https://www.phorest.com) in 2001 — one of the early vertical SaaS companies, and still going strong today.

**2006:** Amazon launched AWS. Suddenly the infrastructure itself followed the same model. You didn't need a server room or a data centre contract. You span up a virtual machine, paid by the hour, and span it down when you were done. Cloud computing turned infrastructure capex into opex too. Small teams could now build scalable software products without the upfront capital costs that had previously been a moat for large incumbents. I was living the pre-cloud version of this at the time, scaling [Demonware](https://en.wikipedia.org/wiki/Demonware) to run the online infrastructure for Call of Duty across five data centres around the world — building our own cloud before the word existed. AWS would have changed everything for us.

**2009:** The financial crisis hit, interest rates crashed to zero, and stayed there for fourteen years. This is the bit people forget. I was back in SaaS by then, and by 2011 was running a SaaS venture studio and seriously considering a move into VC — the money was flowing and the model felt unstoppable.

<figure>
<img src="/images/2026/07/saaspocalypse/slide-03.png" alt="Chart showing global VC funding, SaaS growth and cloud growth from 2005 to 2025, with ZIRP era highlighted" style="max-width:100%;border-radius:6px;">
<figcaption><em>Three trend lines, 2005-2025. Cloud kept climbing. SaaS coasted. VC went on a tear during ZIRP, then fell off a cliff.</em></figcaption>
</figure>

## ZIRP: the fuel nobody talks about

Zero Interest Rate Policy (ZIRP) meant that money was effectively free. Institutional investors who had previously been content with bonds and safe havens found themselves chasing yield anywhere they could find it. That money flowed into venture capital. The VC industry roughly tripled in size between 2009 and 2021.

And what was venture capital deploying all that free money into? Mainly SaaS. Because SaaS had something that investors in a low-yield world found irresistible: predictable, recurring revenue. Monthly subscriptions. Annual contracts. Churn rates you could model. Lifetime value you could calculate. Net Revenue Retention you could tout. The entire vocabulary of SaaS metrics was purpose-built to make these businesses legible to a financial system awash in cheap capital looking for somewhere to go.

The playbook was refined to a science: acquire users at any cost (because capital was free), lock them in with high switching costs and network effects, then harvest the recurring revenue indefinitely. Land and expand. Growth at all costs. The metrics looked beautiful in a spreadsheet. Valuations soared.

The SaaSpalooza was underway.

## The first death: ZIRP ends

In 2022, central banks started raising interest rates to fight inflation. ZIRP ended.

Almost immediately, the party stopped. VC funding fell off a cliff. The flood of cheap capital that had been inflating SaaS valuations and funding growth-at-all-costs strategies dried up. Public SaaS companies saw their valuations crushed. The multiple-on-revenue game was over. Suddenly investors wanted to see, of all things, profit.

The SaaSpalooza had been running on borrowed money, literally. When the borrowing got expensive, the music stopped.

This alone would have been a significant correction. A reckoning for overvalued businesses that had been optimising for growth metrics over economics. A lot of SaaS companies were not actually that good as businesses; they just looked good in a world where capital was free and the discount rate was essentially zero. Remove those conditions and the emperor had considerably fewer clothes.

But then the second thing happened.

## The second death: agents don't need UIs

In late 2022, just as the ZIRP era ended, generative AI arrived. And it turned out to be an existential threat to SaaS for reasons that go deeper than most people have processed.

The core value proposition of a SaaS product is: we have done a difficult thing (built software that does X), and rather than you doing that difficult thing yourself, you can pay us a monthly fee to use ours. The moat is the difficulty. The cost of the UI, the engineering, the integrations, the reliability. You pay because building it yourself is harder than renting it.

AI coding agents have largely collapsed that moat. A reasonably technical person with access to Claude Code or Cursor can now build a working version of many SaaS products in days. Not a competitor product to sell to others; just a version that does the specific thing they need it to do, configured exactly the way they want, with no per-seat licensing fees. The "build vs buy" calculus has shifted dramatically.

But the deeper issue is the UI itself.

<figure>
<img src="/images/2026/07/saaspocalypse/slide-06.png" alt="Diagram showing a SaaS UI stripped back to reveal REST APIs, which are themselves just database CRUD operations" style="max-width:100%;border-radius:6px;">
<figcaption><em>Rip off the UI, expose the API, and underneath almost every SaaS product is a database with Create, Read, Update, Delete operations. The UI exists to make that legible to a human. Agents don't need it.</em></figcaption>
</figure>

The user interface of a SaaS product exists for one reason: to make the underlying data and logic legible to a human. Strip it away and almost every SaaS product is a database with an API on top. Create, Read, Update, Delete. The beautiful UI, the polished UX, the carefully designed workflows — all of it is a translation layer between a human brain and a database.

AI agents don't need that translation layer.

When you have an agent working on your behalf, it doesn't open a browser, navigate to your CRM, click through a contact record and fill in a form. It calls the API directly. It reads and writes data in machine-readable formats. It doesn't care about your onboarding flow. It doesn't need a dashboard. Per-seat pricing becomes absurd when the "seat" is occupied by a software process that never sleeps, never needs training, and can operate dozens of instances simultaneously.

This is why the shift to outcome-based pricing is not just a trend: it is an inevitability. The per-seat SaaS model assumed a human on every seat. That assumption is no longer safe.

## The moats are draining

Even if you accept the UI argument, you might think SaaS companies have other defences. They do, but they are weaker than they look.

**The technology moat** was always somewhat illusory — good engineers could always rebuild most products — but it was real enough when building took years and cost millions. AI coding agents have collapsed the time and cost dramatically. The defensibility that came from engineering complexity is substantially diminished.

**Network effects and marketplaces** were a stronger moat. If all your suppliers are on Platform X and all your customers expect to find you there, leaving Platform X is genuinely painful regardless of what any agent can do. But AI agents are starting to unbundle these too. An agent that can negotiate directly, match buyer to seller, and execute transactions doesn't need a marketplace platform as an intermediary in the same way a human does. This one is slower-moving, but the direction is clear.

**Data moats** are the most frequently cited defence. Surely the accumulated data from thousands of customers makes incumbents impossible to displace? In practice, proprietary data moats are rarer and shallower than claimed. Most SaaS companies are sitting on usage data and operational data that is valuable but not irreplaceable. The companies with genuinely deep, proprietary, hard-to-replicate data are the exceptions, not the rule.

What's left? Brand, distribution, and regulatory compliance. These are real. But they are the advantages of incumbency, not of innovation. And critically, they are advantages that startups by definition do not have — which means the SaaS model as a vehicle for startup investment has lost much of its rationale.

## The third death: the exit market closed

There is a more prosaic reason the SaaSpalooza is over, and it is the one that most directly affects founders and investors right now.

The exit market has closed.

SaaS as an asset class worked because there was a functioning exit pipeline: build a product, grow ARR, achieve a sale or IPO at a healthy multiple, return capital to investors. The whole system depended on exits at the end. The multiples compressed when rates rose. The IPO window largely closed. Strategic acquirers got cautious. The pipeline clogged.

Without exits, venture capital cannot return money to its LPs. Without returns, LPs stop committing to new funds. Without new funds, VCs stop deploying. Without deployment, founders don't get funded. The machine runs in reverse.

This is not just a cyclical correction. The underlying conditions that made SaaS an exceptional vehicle for venture returns — free capital, expanding multiples, a functioning exit market, users who had no alternative to human-facing software — have structurally changed. They are not coming back in the same form.

## What comes next

<figure>
<img src="/images/2026/07/saaspocalypse/slide-09.png" alt="Graveyard illustration with headstones for SaaS, MRR, CAC, LTV, MAU/DAU, Churn and GTM motion" style="max-width:100%;border-radius:6px;">
<figcaption><em>"Dear SaaS, it's not you, it's us. – The Agents."</em></figcaption>
</figure>

None of this means software is dead, or that building products is dead, or that there is no money to be made. It means the specific conditions that made the SaaSpalooza possible — free capital, human-facing UIs as the only interface paradigm, high switching costs from network effects and integrations, recurring per-seat revenue as the universal business model — have changed.

The companies that will thrive are the ones that have genuinely useful knowledge or capability that an agent can leverage, not the ones that built a moat out of UI complexity and switching costs. The business model of the next decade is not "rent my software to your employees." It is "deliver outcomes into your agent fleet."

The SaaSpalooza lasted from 2009 to 2022 — fourteen years. It was a remarkable run, funded by historically anomalous conditions. It produced real value, real products, and real companies. It also produced a lot of overvalued businesses optimised for metrics rather than economics, and a venture ecosystem that confused "this grows well in a zero-interest-rate environment" with "this is a good business."

Both died in 2022: the financial conditions that sustained it, and the user paradigm it was built on. The timing was not a coincidence. The same technological shift that gave us generative AI also gave us the inflation that ended ZIRP. The world changed at both ends simultaneously.

SaaS is dead. The agents are already through the door.
