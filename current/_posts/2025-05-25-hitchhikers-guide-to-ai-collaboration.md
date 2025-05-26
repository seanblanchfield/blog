---
layout: post
title: "Hitchhiker’s Guide to AI Collaboration"
author: "Sean Blanchfield"
date: "2025-05-25"
slug: "hitchhikers-guide-to-ai-collaboration"
image: "/images/2025/05/hitchhikers_guide.png"
draft: false
---
> “The Answer to the Ultimate Question of Life, the Universe, and Everything is… 42.”
>
> *The Hitchhiker’s Guide to the Galaxy*

After  millions of years of computation, Deep Thought finally outputs "42" as the answer to "life, the universe and everything". But no one remembers what the question was. Douglas Adams was prescient as well as hilarious. It's a bit on-the-nose now that many of us (and I’ll admit to this) have taken to lobbing 40-page deep research memos into Slack or Discord without being clear about what we were trying to answer.

<!-- more -->

### The AI doc dump

Sending your colleague a long AI-generated hot-take  is anti-collaborative. [Doc dumping](https://en.wikipedia.org/wiki/Document_dump) is a dirty tactic from litigation, where legal teams bury each other in documents to overwhelm and confuse. Now we're doing it to our own side. Deep research AI agents  allow an insightful 30-page brief to be created in minutes instead of days. Reading it, however, still takes ages. If ten colleagues read a 30-page brief at two minutes per page, that’s 10 hours of company time burned, with none of the cost falling on the perpetrator. Previously, the work required to create such a doc provided its own friction, but now that guardrail is gone.

Even worse than time asymmetry is the lack of a clear question. It's suddenly more effort to articulate the question than to answer it, and often the author really never thought it through carefully in the first place. Now that we have magic  machines that can answer any question with a McKinsey-style report, we have a new responsibility to decide what questions matter, and how to ask them well. But our collaboration tools weren’t designed for that. They help us work on the *output*, not the *input*.

![](/images/2025/05/deep_thought_42.png)

### Collaborate where it matters

Historically, review happened after the work was done. Docs and code got polished collaboratively. That doesn’t work anymore. Reviewing an AI-generated artifact is slow, demoralising, and often pointless. You can’t meaningfully contribute to a prompt after the output exists. You need to be in at the start, when the question was shaped, the context assembled, the prompt designed.

### Some emerging etiquette

* Don’t ask someone to spend more time reading a doc than you spent generating it.
* A deep research memo should primarily be read by LLMs, not humans.
* Summarise it to a two-minute read that includes a thoughtful paragraph on what it's about, then share a link to a project where the underlying work can be interrogated interactively, if needed.

### Our tools are all wrong

Our collaboration stack is built around outputs. Take GitHub. Asking engineers to review AI-generated code after it’s been created is like inviting PRs on a minified JavaScript bundle. It's too late. The valuable intervention is to collaborate where the other humans are working, not to mark the machine's homework.

Meanwhile, engineers working with Cursor, Windsurf, or Claude are interacting with agents in ephemeral chat logs that vanish. Their colleagues can only review the artifact, stripped of the context window that shaped it.

The same failure applies to Google Docs. Document collaboration only begins after the AI has spoken.

### Collaboration moves upstream

Writing a good AI-generated doc or feature spec is no longer a single step. It involves prompt design, gathering and compacting context, chaining models, tuning parameters, and iterating.

Ironically, as software engineering has moved upstream to specs and product requirement docs, collaborating on documents is beginning to  resemble software engineering more than writing. Yet we have no tools that let teams collaborate on this process. No version control, no reviews, no visibility.

### The tool that doesn't exist (yet)

We need a collaborative workspace for prompt chains—something web-based, with tight integration to internal and external sources (Google Docs, Notion, CMS). Documents should be searchable, taggable, and organised by purpose. The tool should allow for prompt chain design, chaining models together with clear business intent, and viewing outputs side-by-side.

It should track all changes and rerun only what’s changed. Post-generation conversations should be logged and used to improve the prompt chain, allowing versioned evolution over time. Final artifacts should be queryable via API and accessible to agents. Evaluation tools should help teams track which chains deliver good results. In short, prompts should be treated like code: reviewed, tested, and improved with use.

If you know a tool like this, please let me know! Perhaps some of you have figured out an adequate workflow in a no-code agent builder platform like n8n. If so, please share!

### Ask better questions together

We must stop collaborating on the answer. The real leverage is in the question—its timing, its framing, its context. AI gives us speed, but speed without clarity is just noise. To get the full benefit, we need workflows and tools that help us think better together, not just generate faster alone.

![](/images/2025/05/dont_panic.png)