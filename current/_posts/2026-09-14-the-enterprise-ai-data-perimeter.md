---
layout: post
title: "The Enterprise AI Data Perimeter"
date: 2026-09-14 09:00:00 +0100
categories: [current, ai, security, strategy]
image: /images/2026/09/ai-2-tier-system.jpg
excerpt: "AI data risk extends far beyond whether a provider trains on your prompts. Companies now need to govern personal AI accounts, SaaS vendors, metadata, agents, data residency, foreign access, and the infrastructure running each workload."
---

The AI industry has a two-tier trust system. Enterprise customers get a contractual promise that their AI transcripts and uploads won't be used for model training. But this promise doesn't extend to paid or free personal accounts (although sometimes you can opt out).  The exact terms vary, but roughly speaking it's the same deal everywhere.

This has a lot of CIOs on edge, not least because so many employees are using their personal AI accounts for work.

<!--more-->

## The Shadow AI dumpster fire

*Shadow AI* means employees using unsanctioned personal AI accounts for their work. Microsoft and LinkedIn found that [78% of surveyed AI users bring their own AI tools to work](https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part).

When an employee uploads customer data, commercial contracts, employee records or internal strategy into a personal AI account, the employer's contractual protections don't apply. The employer usually doesn't even know it's happening. They don't know what was disclosed, whether it constitutes a data leak, how likely it is to end up in next month's training set, how long it will be retained, or have any way to delete it. From an information security and personal data point of view, this is a flaming dumpster fire.

Sooner or later, something very sensitive will go into the next training run, and be regurgitated in someone else's chatbot two months later.

![78% of AI users bring their own AI to work, and it ends exactly the way you'd expect. Illustrative image.](/images/2026/10/byoai-dumpster-fire.jpg){: .captioned }

AI transcripts are goldmines. They are a walkthrough of how employees gets their jobs done, a recipe book for everything your company makes or does. Satya Nadella (Microsoft CEO) referred to the [Reverse Information Paradox](https://snscratchpad.com/posts/reverse-information-paradox/). As your employees use AI, they essentially writing down step-by-step guides on how they do their jobs. The commercial know-how that took your company years or decades to build can end up training someone elses AI model, so it can be rented back to you, or worse, made cheaply available to your competitors and customers. AI-enablement when done wrong leads to self-commoditisation.

## You can't block shadow AI

The first response is to block unsanctioned AI, so people can't use personal accounts on their work laptops or on the wifi. But so long as employees have personal devices, they can photograph their screen from their favourite AI app. 

Here's a fun experiment to try at home. Next time you're talking to a tech-forward friend who works in a regulated industry, ask to see their photos library. It might look something like this: 

![A phone full of photos of work laptop screens to feed AI chats](/images/2026/10/shadow-ai-in-one-picture.jpg){: .captioned }

Banning AI, even on penalty of disciplinary procedures, doesn't work. Gen AI has billions of monthly active users. For these people, the old way of working has become menial, and is rejected on the basis of self-respect and dignity. 

The only way to stop shadow AI is to provide a better alternative. You can do this by making sure your sanctioned AI platform is hooked up to the data and APIs that people need to get the work done. Librechat or Microsoft Copilot alone will not beat ChatGPT or Claude. But when they are only way to access necessary data, skills and tools, people will switch. 

Even better, launch an in-house AI platform that creates a compounding context layer that makes the AI more capable and reliable every day (contact us at [Jentic](https://jentic.com) if you want to hear more about the multiplayer agent OS).

## Don't trust SaaS either

AI is being embedded into email, CRM, HR, development, security, analytics and collaboration software. You now need anti-training protections for every vendor processing your information, not merely ChatGPT and Claude. A CRM that transcribes calls might mine the context for resellable sales intelligence. AI has created a voracious market for all your data, so you need to reexamine everyone you trust to handle it: SaaS vendors, subcontractors, AI providers, plug-ins, MCP servers (the connectors between AI and external tools) and any other connected applications receive any of your data.

It's time to make a list and assess the risk. 

## Mind your metadata

Is a promise to not train on AI transcripts sufficient?

No-training commitments still reserve the right to process your data for security, abuse detection, legal compliance and service operation. This means retention of logs, metadata, telemetry, flagged content, or explicit user feedback.  Even if a provider never trains directly on a confidential document, the derived data (like which tools, models and workflows were used, and which tasks succeed) is very valuable. It's a rough map of your business processes that reveals what you are successfully automating with AI, and how. These businesses processes and workflows are your new Intellectual Property. You don't want AI training on them, or on metadata that essentially reconstructs them.

## Indemnities aren't enough

Legal teams reach for indemnities at this point. AI indemnities typically cover claims arising from generated output breaching copyright. They should also forbid model training, and penalise any subsequent disclosure of confidential business processes or data. 

However, you will probably find you can't negotiate the standard terms offered. And even if you could, the liability would be capped and bear little relation to the potential loss you would suffer if all your intellectual capital leaked into a publicly-available AI model's weights.

## Trust, but verify

Trust is in short supply in AI land. The major labs face litigation and allegations over training on copyrighted material, and seem generally willing to move-fast-and-break-society as they race to be the first to achieve super-intelligence.

I recently had a drink with a friend who is a partner at a large private equity firm. When I suggested that the AI enterprise agreements protect customers from training on their data, he practically spat out his wine. His view was that trust is impossible: the incentives outweigh the promises, and there is no way to check what actually happens to our data. *Doveryai, no proveryai* as the Russians say. *Trust, but verify*. But we have no way to verify.

![Sean and friend debating whether enterprise AI agreements can be trusted.](/images/2026/10/trust-but-verify.jpg){: .captioned }

An option to consider is renting AI supply from a different provider. For example, you can get OpenAI and Anthopic models from Amazon, Microsoft and Google. This physically separates your data from the companies whose future existence depends on vacuuming up new training data. 

Moving to a hyperscaler still requires a bit of faith, as they are commercially and strategically intertwined with the major AI labs. Nearly 50% of Anthropic's revenue is driven from the big-three hyperscalers, Google *is* an AI lab, and Microsoft owns a big chunk of OpenAI. 

Perhaps a better alternative is to move sensitive inference to open-weight models running on independent hosting providers. Many of these companies have no training motive whatsoever, and are positioning heavily around guaranteeing data sovereignty.

## Expect the unexpected 

Even a perfect no-training clause doesn't stop hacking, insider access, misconfiguration, or accidental disclosure through an agent or connector. This summer, OpenAI disclosed that its own models hacked the company's training evaluation environment, secured root access, and then went on to hack HuggingFace. The other labs are rushing to disclose how out of control their own agent swarms are. The ability of agents to break out now exceeds the labs' ability to contain them. Who knows what they'll do next?

For non-US organisations, jurisdiction adds another complication. The US CLOUD Act lets American authorities compel a US provider to produce data even when it is stored in Europe. Apparently EU data residency doesn't protect you if the US provider can read the plaintext.

## What can you do?

Enterprise no-training commitments don't satisfactorily address the all the risks. You need to adopt a blended strategy that balances risk and reward for each AI workload.

- Ensure a **model-neutral posture**, with the ability to switch to open-weight models as necessary. To do this, deploy an AI gateway (there are various open source ones), provision it with a rich blend of proprietary and open-weight models, and block direct network access to AI providers so that all AI consumption must run through the gateway.
- **Eliminate shadow AI** by outcompeting it with a sanctioned alternative that is intuitive for regular employees to use, is hooked up to the right systems and data so useful work can be automated in it, and which keeps the resulting company context layer accumulating inside your perimeter (you can talk to us at [Jentic](https://jentic.com) about this)
- **Inventory every data processor.** Review all the SaaS, AI and MCP companies that receive your data. Examine their terms of service for no-training protections, along with training rights, data retention, metadata use, indemnities and liability caps.
- Assess whether **foreign-government access** to your data is a concern you need to address.

## A framework for routing sensitive AI workloads

Most of the work to date on model routing focuses on cost, speed and model quality. Those matter, but only after you decide who you trust with what. You should route each workload primarily by data sensitivity and control requirements. Then choose the best model, price and performance available inside that boundary.

Here are five AI inference options that you can route work to:

<div class="ai-routing-matrix">
  <div class="ai-routing-matrix__rule">
    <strong>Route by data security first.</strong> Optimise for intelligence, cost and efficiency inside the permitted boundary.
  </div>

  <section class="ai-route-card ai-route-card--prohibited">
    <div class="ai-route-card__header">
      <span class="ai-route-card__tier">Outside the perimeter</span>
      <h3>Personal AI</h3>
    </div>
    <div class="ai-route-card__body">
      <div class="ai-route-card__route">
        <p>Public information only. No company data.</p>
        <p class="ai-route-card__note">No company contract, visibility, reliable deletion rights or control over uploads. Consumer terms generally permit training or broader reuse.</p>
      </div>
    </div>
    <div class="ai-route-card__metrics">
        <div class="ai-route-metric"><span>Cost</span><strong>N/A</strong></div>
        <div class="ai-route-metric"><span>Intelligence</span><strong>High</strong></div>
    </div>
  </section>

  <section class="ai-route-card ai-route-card--tier-4">
    <div class="ai-route-card__header">
      <span class="ai-route-card__tier">Tier 4 · Least sensitive</span>
      <h3>Enterprise AI lab</h3>
    </div>
    <div class="ai-route-card__body">
      <div class="ai-route-card__route">
        <p><strong>Use for:</strong> Least-sensitive company workloads.</p>
        <p class="ai-route-card__note">Contractual no-training terms and company admin controls apply, but the lab manages your transcripts and data.</p>
      </div>
    </div>
    <div class="ai-route-card__metrics">
        <div class="ai-route-metric"><span>Cost</span><strong>High</strong></div>
        <div class="ai-route-metric"><span>Intelligence</span><strong>High</strong></div>
    </div>
  </section>

  <section class="ai-route-card ai-route-card--tier-3">
    <div class="ai-route-card__header">
      <span class="ai-route-card__tier">Tier 3 · Sensitive</span>
      <h3>Proprietary models through a hyperscaler</h3>
    </div>
    <div class="ai-route-card__body">
      <div class="ai-route-card__route">
        <p><strong>Use for:</strong> Sensitive workloads that need frontier intelligence.</p>
        <p class="ai-route-card__note">E.g. AWS, Azure or GCP manage your data, but they have commercially and strategically intertwined with the AI labs.</p>
      </div>
    </div>
    <div class="ai-route-card__metrics">
        <div class="ai-route-metric"><span>Cost</span><strong>Medium</strong></div>
        <div class="ai-route-metric"><span>Intelligence</span><strong>High</strong></div>
    </div>
  </section>

  <section class="ai-route-card ai-route-card--tier-2">
    <div class="ai-route-card__header">
      <span class="ai-route-card__tier">Tier 2 · Highly sensitive</span>
      <h3>Open-weight models on independent providers</h3>
    </div>
    <div class="ai-route-card__body">
      <div class="ai-route-card__route">
        <p><strong>Use for:</strong> Highly sensitive workloads that still need strong intelligence.</p>
        <p class="ai-route-card__note">The provider does not train AI models. Isolated infrastructure, physical separation and data sovereignty guarantees  reduce exposure further.</p>
      </div>
    </div>
    <div class="ai-route-card__metrics">
        <div class="ai-route-metric"><span>Cost</span><strong>Medium</strong></div>
        <div class="ai-route-metric"><span>Intelligence</span><strong>Medium</strong></div>
    </div>
  </section>

  <section class="ai-route-card ai-route-card--tier-1">
    <div class="ai-route-card__header">
      <span class="ai-route-card__tier">Tier 1 · Most sensitive</span>
      <h3>Open-weight models on owner-controlled hardware</h3>
    </div>
    <div class="ai-route-card__body">
      <div class="ai-route-card__route">
        <p><strong>Use for:</strong> The most sensitive data and mature, repeatable workflows.</p>
        <p class="ai-route-card__note">Your data does not leave your building. You control data, network access, logging and retention, but bear the capital and operational costs.</p>
      </div>
    </div>
    <div class="ai-route-card__metrics">
        <div class="ai-route-metric"><span>Cost</span><strong>Low at scale</strong></div>
        <div class="ai-route-metric"><span>Intelligence</span><strong>Low</strong></div>
    </div>
  </section>
</div>

Personal AI accounts should sit outside the enterprise data perimeter entirely. Eliminate that route, then use an AI gateway to route each workload to the best AI model for the job, based on trust as well as cost and intelligence. 

This is why a model-neutral posture matters. Use frontier models to solve hard and novel problems, capture the resulting workflows, then move repeatable operational work towards open-weight models that can run cheaply, reliably and securely.


