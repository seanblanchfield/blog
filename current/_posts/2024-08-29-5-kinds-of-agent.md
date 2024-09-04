---
author: Sean Blanchfield
date: 2024-08-29 21:00:00
layout: post
link: https://seanblanchfield.com/many-meanings-of-agent
slug: many-meanings-of-agent
title: Many Meanings of AI Agent
image: /images/2024/08/many-meanings-of-agent.png
---

I've been having back-to-back conversations about the AI agentic future for a few months now, and I've found people are throwing this new piece of "agent" jargon around a bit loosely, referring to pretty distinct things. Here's what I've classified so far:

<!-- more -->
# Many Meanings of "Agent"

Here's my list of the different things people might actually mean when they say "agent":

1. **Automation**: Any hardcoded script or automation of the usual variety (e.g. on Zapier, Workato, or other iPaaS or automation platform) that uses an LLM in one of the automation steps to summarise, categorise or extract data. A great step forward for automation, but one small step for AI.
1. **Agency**: An process that performs generative logic. At each step, the next step to be taken is decided by AI in the moment, and is not hardcoded into a prior script/automation. For example, the agent might prompt its LLM with a tree-of-thought prompt to form a plan of action to resolve a request, and then walk the tree performing associated tool calls until it succeeds. Perhaps this is how Apple Intelligence and Google Astra are coded.
1. **Async**: A long-lived process that runs in the background doing its own thing (e.g., reacting to external events or waking up on a timer), not just replying to human requests like a chatbot. From another perspective, a long-lived process has memory, while a chatbot doesn't exist when you aren't talking to it. 
1. **Chatbot**: A chat interface on top of a document store, using something like RAG and vector DBs to answer queries. These are read-only systems, so let's keep on calling them "chatbots", not "agents". 
1. **Multi-"agent"**: one part of a multi-agent system, which (if considered individually) might be just a chatbot or vector DB that wouldn't be called an "agent" outside of a multi-agent system.
1. **Anthropomorphic**: anything cute that encourages you to think of it as an assistant, docile colleague or helper. Siri, cortana etc. goes back to Clippy, and prody parrot if you go back that far.
1. **Self-driving**: A UI Large Action Model that uses a OS or application UIs, replacing human workers on a like-for-like basis. This is cool, but think it will be most useful for legacy applications, and will be a natural extension of RPA.

# Chatbots vs Actbots

The most simple of these definitions &mdash; automations &mdash; barely deserves new jargon, and I still think of them as automations or scripts.

The most useful definition of "agent" is based on agency and asynchronous long-lived processes that have state. These don't need humans to provide them with hardcoded logic in advance; they figure it out on the fly, constrained only by the tools and the job description they are given. This is transformative. In a personal context it is a useful assistant that lives on your device, but in a business context it means generative business logic. This definitely demands a new name.

An "agent" is like a chatbot that can do things. If the word "agent" seems to be getting your AI conversation in a tangle, I'll suggest you call them "actbots" instead.

These actbot agents - the type that have agency and don't need hardcoded logic - are the ones to watch. This is how human labour will be replaced by AI. Organisations will still have people at desks, but they will also have actbots hanging out on servers, doing work, talking among themselves and interrogating their chatbot cousins, and communicating with humans over email, slack or even voice. If we could start graphing the ratio of human labour to actbot labour over time, from now on it will go up and to the right.

