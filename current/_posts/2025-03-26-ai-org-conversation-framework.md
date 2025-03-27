---
layout: post
title: Having the "AI has arrived" conversation
date: 2025-03-26 12:00:00
author: Sean Blanchfield
slug: ai-org-conversation-framework
link: /ai-org-conversation-framework/
image: /images/2025/03/ai-conversation.png
draft: false
---

Since November 2024, software has become approximately free to create. 

The AI revolution isn't coming — it's here, upending our tacit assumptions about how organizations operate, what products should do, and who your customers will be tomorrow. If you're selling software on the premise that it's hard to build, you're already behind.

<!-- more -->

Most organizations have that one person — the budding AI champion, the unofficial Chief AI Officer in waiting — trying desperately to sound the alarm while facing skepticism, or resistance from colleagues who (rightly or wrongly) fear their roles will vanish. 

I've spent about a year having conversations about this. At Jentic's AI agent meetups (a shameless plug for my company — get on the [mailing list here](https://listmonk.jentic.com/subscription/form?l=Jentic+AI+Meetups)), at a certain secret founder gathering I run, through workshops, podcasts, fireside chats (on both sides), and mentoring sessions. I've distilled some patterns from this, a kind of framework for having the "AI is arriving" conversation.

This isn't about *whether* to adopt AI. AI has already arrived for many of us, and it is transformative. The tsunami is coming, and sooner or later it will hit every company, or its customers or suppliers.  The implications of AI will be uncomfortable for a lot of businesses (or for many people working in them) but there is time to respond and in many cases prosper. *It's time to have the AI conversation*. My small contribution is to suggest the following structure.

1. [How AI affects operations](#1-how-ai-affects-operations)
   - [Become AI-Native](#become-ai-native)
   - [Automation](#automation)
   - [Life after SaaS](#life-after-saas)
2. [How AI affects your product](#2-how-ai-affects-your-product)
   - [Table-stakes](#table-stakes)
   - [Fundamental Rethink](#fundamental-rethink)
3. [How AI affects your customers](#3-how-ai-affects-your-customers)
   - [Market Disruption Analysis](#market-disruption-analysis)
   - [The Changing Buyer](#the-changing-buyer)
4. [How to adapt](#how-to-adapt)
   - [Working with AI Today](#working-with-ai-today)
   - [Track your adoption blockers](#track-your-adoption-blockers)


---

## 1: How AI affects operations 

### Become AI-Native 

We're all trying to figure out what an AI Native organization looks like right now, but we know it's much faster and leaner and more productive.  Imagine AI-native law firms with 10x efficiency and big profit margins.  Don't be satisfied with open-ended explorations, pilots or initiatives; you need a map that shows you a path from where you are now to the organisation you would have been had you started in 2025. i.e., the kind of competitor you're going to be meeting in the market in a year or two. 

What does an AI-native organization look like? It's one where:
- AI isn't a department. It's how work gets done.
- Decision-making happens at AI speed, not meeting speed
- Competitive advantages come from proprietary data and AI customization, not human-hours

### Automation

**Software Development**: Your developers should be directing AI, not writing code. All software should be AI-generated with human oversight tapering as the tools get better. The productivity gap between AI-augmented developers and traditional coders incremental - it's probably orders of magnitude.

**Customer Support**: Intercom reports their AI agent Fin achieves a [52% resolution rate](https://community.intercom.com/fin-ai-agent-59/what-is-your-fin-success-rate-8841#:~:text=According%20to%20Intercom%2C%20Fin's%20average%20resolution%20rate%20is%2052%25.)—and that's just the beginning. L1 and L2 support tiers should be entirely AI-driven, with humans handling only the most complex edge cases (and even then, only handling them once).

**Administrative Tasks**: "Email jobs" are gone. If someone's primary value comes from moving information between windows on their laptop, AI will do it better, faster, 24/7 over APIs.

**Decision-making**: Management itself is being transformed. When AI can analyze every data point in your organization simultaneously, there'll be new challenges. How can you blend human intuition with AI's ability to overwhelm you with an evidence-based argument? How will you spot the hallucinations, while seizing the advantages? Is your leadership team already leaning into AI to learn how to co-work with it? (cheat code: start with a Deep Research model - OpenAI is currently very good).

### Life after SaaS

The multi-vendor SaaS stack will be a relic. Most SaaS is a UI to help people do CRUD on DBs (create-read-update-delete on databases) The cloud era and the corresponding SaaS boom has given us thousands of SaaS data silos tailored to the particular needs of different workers in different industries.  What happens when the human isn't doing that workflow any more?  AI doesn't need help using a database.

AI-native companies are building bespoke AI-generated super apps that can handle everything from CRM to project management to analytics in one self-hosted postgres database. They'll never need data lakes, because they are staring with data monoliths. Having all the data in one well-structured place, combined with AI coders ready to analyse and build, will unlock unexpected new capabilities for them.

In a way, generative AI's coding ability means that every small company can have it's own customised, free ERP system that adapts to their requirements instantly as they grow. 

---

## 2: How AI affects your product

### Table-stakes

Slapping a chatbot on your product isn't an AI strategy. But maybe it's the start of your AI product journey. 

Adding a conversational layer without reconsidering the underlying product signals you're aware of AI but unwilling to embrace its transformative potential. These surface-level integrations might buy you time, but they won't save you from the fundamental reckoning that's coming.

### Fundamental Rethink

The uncomfortable truth is your product wasn't designed for an AI-intermediated world. It was built for humans with human limitations, human interfaces, and human patience levels.

- *The naked API*. Here's a thought exercise worth doing: Imagine stripping the user interface off your product, leaving just raw APIs. This is how AI Agents will use your product. Imagining your product naked like this exposes its core value, or lack thereof. If you were only helping humans use a database, without adding some other value, you're in trouble. (if it helps, you're in great company... the perfect example of this is any CRM).

- *Does AI really need your API?* Even if your naked APIs add some value, you need to ask whether it's enough. In many cases, AI can just solve a problem internally, whether by generating some once-off code, or thinking through the logic of a problem, or doing an end-run around you and going direct to your source data (e.g,. using a agent to monitor multiple markets for price changes).

- *Where is your moat?* Competitive barriers or moats used to be so easy to understand: technical complexity, network effects, data. What's left? Technical complexity is gone. Network effects will likely be dismantled by user-side agents that can be in multiple marketplaces or social networks simultaneously. Data is good if it's truly proprietary and valuable and non-synthesizable, and monetizing it doesn't involve giving it away... but how often is that the case?  What's left is the leaky moats of regulatory barriers and maybe brand loyalty. But in nearly every case, that expensively-built competitive moat is about to be easily crossed by AI native competitors.

If you're sweating, that simply means you understand what's at stake.

---

## 3. How AI affects your customers

### Market Disruption Analysis

Some markets will explode with AI as a catalyst. Others will simply implode. Which category do your customers fall into?  I'm thinking of a certain SaaS conference in which hundreds of VC-backed SaaS companies meet to sell SaaS software to other SaaS companies, keeping the same VC dollars flowing along a Möbius strip of apparently increasing enterprise value. Sounds like something that could unwind kind of quickly.

Vulnerable customers might be those whose:
- Primary value proposition is providing or assisting human labor that can be automated
- Are gatekeepers or middlemen without moats

The opportunity lies not just in riding these waves but in identifying the second and third-order effects. When one industry transforms, what happens to its suppliers, customers, and adjacent markets?

### The Changing Buyer

What if your buyer's job is automated out of existence? Worse, what if your product plus AI means that you're the one doing it?

Many products are sold to roles that AI will eliminate first: analysts, administrative assistants, junior developers, content creators, customer support managers. When your buyer persona vanishes, who makes the purchasing decisions?

The answer is usually "someone higher up the chain". Executives who care less about feature checklists and more about strategic outcomes. Analysts want an analysis tool, but the executives want an analysis. 

1. Your sales pitch needs to elevate from tactical benefits to strategic imperatives
2. Your product needs to solve C-suite problems, not departmental ones
3. Your pricing model needs to reflect organizational value, not seat-based metrics

---
## 4: How to adapt

### Working with AI Today

#### What can you be doing right now?

Current AI capabilities are both more and less impressive than the hype suggests. Get as many people in the organisation (including the C-suite) using it on a day-to-day basis so they understand the strengths and limitations, and so you can have a real conversation about the meaning of the month-over-month advancements that are unlocking new applications. 

Set up peer groups interested in AI to compare notes, join meetups, discords and slacks, and identify mailing lists that help you keep track (I like [this smol one](https://buttondown.com/ainews)). Most importantly, constantly ask yourself "Should I still do this task this way, or should I AI it?".


### Track your adoption blockers

The AI and agentic field is still early, and strewn with obstacles to enterprise adoption. Here are some of the key challenges you'll need to navigate. Go through the list and rank them for your organisation. Then you'll have a list that you can monitor progress on, and gauge when the time is right to pull the trigger on full-scale adoption.

- **Reliability and consistency**: AI systems still produce inconsistent outputs and occasional hallucinations. Implementing robust evaluation frameworks and quality assurance processes is essential.

- **Authentication, permissions, and data governance**: This is what we're solving at [Jentic](https://jentic.com): ensuring AI systems access only the data they should, with appropriate permissions and auditability.

- **Security and prompt injection**: Your AI systems are only as secure as their prompts. Adversarial attacks can manipulate AI behavior through carefully crafted inputs.

- **Regulatory considerations**: From the EU AI Act to industry-specific regulations, compliance requirements are evolving rapidly (and [are a minefield](https://seanblanchfield.com/2025/03/eu-web-act)).

- **Copyright, training data provenance, and licensing**: The legal landscape around AI-generated content and training data remains deeply unsettled. 

- **Reputational risks**: From tone-deaf responses to toxic outputs or even AI systems that appear to deceive users — your brand could be on the line.

- **Data privacy concerns**: AI systems can inadvertently memorize and regurgitate sensitive information hidden in their latent space.

- **Fairness and bias**: Without careful design, AI systems perpetuate and amplify existing biases, including over-representing and under-representing certain groups or events. 

- **Explainability**: Black-box decision-making creates liability and erodes trust. Agentic approaches that provide reasoning and action traces offer a partial solution.

Addressing these challenges isn't just about risk mitigation—it's about creating sustainable competitive advantage through responsible AI adoption.

## Conclusion

The AI revolution demands more than incremental change—it requires fundamental reimagining of how your organization operates, what products you build, and how you go to market.

The organizations that thrive won't be those with the biggest AI budgets or the most data scientists. They'll be those that ask the hard questions early, make bold decisions quickly, and rebuild from first principles.

Start these conversations now:
- How would we design our organization if we were starting from scratch today?
- What would our product look like if designed primarily for AI consumption?
- Which parts of our value chain are most vulnerable to AI disruption?
- How can we turn AI from a threat into our greatest competitive advantage?

The answers won't be comfortable, but comfort is a luxury none of us can afford in this new world where software is approximately free and change happens at machine speed.

The future belongs to those who adapt fastest. Will that be you?

---

*Want to continue the conversation? Join our [AI agent meetups](https://listmonk.jentic.com/subscription/form?l=Jentic+AI+Meetups) or reach out [directly to us at Jentic](https://jentic.com/) discuss the challenges of deploying AI at organisation scale*
