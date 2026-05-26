---
layout: post
title: "Do Agents Dream of Electric Coworkers?"
date: 2026-05-26 12:00:00 +0100
author: Sean Blanchfield
slug: do-agents-dream-of-electric-coworkers
link: /do-agents-dream-of-electric-coworkers/
image: /images/2026/05/do-agents-dream-of-electric-coworkers.jpg
draft: false
categories: [ai, agents]
---

I've been running a single AI agent for everything. It handles my calendar, my email, my home automation, the infrastructure for a VPS, our CRM pipeline - all of it, one workspace, one context.

The multi-agent crowd would tell you this is naive. Their pitch, stripped down, is that you should map your AI system onto your human org chart like-for-like: an agent (or a multi-agent system) for every role, a team structure that mirrors the one you already have. Build your AI team the way you'd build a human team.

There's a kernel of truth in it. Isolation boundaries around different contexts *do* make sense in a company scenario - I'll get to that. But the like-for-like replacement thinking is where it goes off the rails.

I asked my agent what it thought:

> *"Most of that reasoning is borrowed from human team design," it said. "And it maps badly onto how I actually work."*

<!-- more -->


## The wrong mental model

The conventional case for multi-agent systems rests on familiar ideas: specialists outperform generalists, parallel tracks produce better outcomes, different perspectives improve decisions, and security benefits from separation of concerns.

These are all true of human teams. They're only *sometimes* true of LLM agents, and for completely different reasons.

The constraints that drive human specialisation are expertise limits, cognitive load, attention, time, and ego. An expert knows things a generalist doesn't. A focused person does better work. A team has more hours than a single person.

None of these apply to an LLM agent in the same way.

The agent doesn't get tired. It context-switches instantly. It already knows DevOps, CRM strategy, financial modelling, home automation, how to bake a cake - at roughly the same level, in the same session. There's no expertise gap a "specialist" agent fills. What a specialist agent actually has isn't deeper knowledge; it's a more focused workspace. But that's a narrower benefit than "specialists are better", and it comes with a real cost.

## The actual constraints

What genuinely limits an LLM agent isn't expertise or attention, but:

- **Context window and token budget.** Everything relevant to a decision needs to fit in active context. A 170GB email archive can't all be in the room at once. A CRM pipeline with thousands of contacts and years of interaction history competes for that space with whatever else you're discussing.

- **Workspace coherence.** The richer and more stable the accumulated context (e.g., memory files, learned conventions, domain-specific knowledge) the better the agent performs. An agent whose workspace is half email archive and half home automation configs is serving two masters.

- **Routing overhead.** Every boundary you create is a decision you have to make: which agent do I ask? That's cognitive load shifted from the agent back to you. It's real, and it compounds.

- **Isolation and blast radius.** This is the most important constraint in serious deployments. An agent with read access to your entire email archive and write access to production databases is a single prompt injection or hallucination away from a very bad day. The question isn't just *does this agent have too much context* - it's *does this agent have too much access*. Different domains carry different trust profiles. Your CRM agent probably shouldn't see your HR system. Your DevOps agent probably shouldn't read your personal email. These are the same authorisation boundaries that drives role-based access in human organisations, except agents might be ephemeral, and the stakes are different because agent are gullible and can destroy data and reputation at speed.

So "when should I use multiple agents?" collapses into: *what constraint am I actually solving?*


## Five tests before you split

My agent gave me a checklist. I'd want most of these to be true before spinning up a separate persistent agent.

1. **Autonomous continuous work exists.** Does this agent have a job to do between conversations, regardless of whether you've asked it anything? A CRM agent that ingests email, scores contacts, and monitors pipeline state has an autonomous lifecycle. A "calendar helper" that just answers questions doesn't.

2. **Context footprint is large and domain-specific.** Would this domain, if it lived in the main workspace, crowd out unrelated conversations? Email archives and contact graphs: yes. A recipe collection: no.

3. **The domain is stable and bounded.** Can the agent accumulate coherent memory over months? CRM: yes - contacts, interactions, pipeline are stable categories. "Research agent": no - the topic changes every time. A sub-agent handles that better.

4. **A different access profile is warranted.** Does this domain need tool access that increases the blast radius of a mistake? An agent with deep read access to years of email archives and write access to a database probably shouldn't also be controlling your home infrastructure.

5. **A clean shared data layer exists.** This one is easy to miss. The anti-pattern is agents passing context to each other in conversation. That's fragile and lossy. The right pattern: the CRM agent writes structured findings to a database; the main agent queries that database when it needs CRM context. The data *is* the handoff. No chatty coordination required.

If you can't tick most of these, you're probably solving a workspace hygiene problem... and you can solve that without a new agent.

## The pattern that actually works

The architecture I'm leaning towards isn't "persistent main agent plus three persistent siblings." It's orchestrator plus ephemeral sub-agents.

When a task benefits from focused context and a clean slate, spawn a sub-agent for it. It gets a specific brief, does the work, returns the result, and disappears. The main agent decides when to spawn and integrates the output. You never have to route anything.

This gets you the focus benefit without the coordination overhead, and it avoids the worst failure mode of multi-agent systems: information loss at handoff boundaries.

Humans think of "briefing the colleague" as a roughly lossless operation. It isn't, it's just our only option because we can't read each other's minds. Every handoff is a compression. Before long, whether human-to-human or agent-to-agent, it's a game of telephone with context loss compounding at every turn. But agents have a superpower that humans don't. They *can* read each another's minds. You can literally share memory from one to another, even if that just means mapping a folder of markdown files into multiple openclaw containers.  This isn't telepathy, it's a hive mind.

## In short

Split on isolation requirements. Not on functional domains.

The **right reasons** to run a separate persistent agent: different users who need true data isolation, genuinely autonomous long-running domains with heavy dedicated context, and real security concerns where blast radius reduction matters.

The **wrong reasons**: "I want a specialist," "different perspectives improve decisions," or anything that maps a human org chart onto a system that doesn't have human constraints.

Most of the multi-agent thinking imports the wrong mental model. Human teams are structured around human limitations. AI systems need to be structured around what actually limits an LLM.

Or as my agent put it: *"You're not adding expertise. You're managing context. Design for that."*

![Do Agents Dream of Electric Coworkers?](/images/2026/05/do-agents-dream-of-electric-coworkers.jpg)
