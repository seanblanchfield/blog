---
layout: post
title: "Five Shades of AI Sovereignty"
date: 2026-08-25
categories: [current, ai, strategy, policy]
excerpt: "AI sovereignty is being used to mean six different things simultaneously. But strip them back and they all reduce to the same question: what do you get to own?"
image: /images/2026/07/ai-sovereignty.png
---

The phrase "AI sovereignty" is everywhere right now. To a CISO it means means one thing. To a graphic designer in Galway asking whether her livelihood is safe it means something different again. To a government minister in Paris, watching Washington pull the plug on a frontier model overnight, it means something much bigger. But they are all asking the same basic question: *what part of this future do we get to own?*

<!-- more -->

In my role on the Irish government's AI Advisory Council, I took a special interest in AI sovereignty, and in my work as CEO of Jentic it is both a recurring conversation with our customers and a core value proposition of our company. AI sovereignty means different things to different people, with that one connective concern running through it all. The same conversation, at different scales. 


## The personal: meaning and dignity

If AI does the writing, the designing, the coding, the analysis, what is left? The Star Trek version is liberation from drudgery and freedom for more meaningful work. But we do not know yet, and the benefits will probably not be fairly distributed.

A small number of people are privatising intelligence itself (the one thing that has always been distributed roughly equally among humans) and building business models that rent it back to everyone else. When intelligence gets industrialised and the returns flow to whoever owns the infrastructure, the rest of us could be cut out. 

This might be the defining political question of the next decade. Will ordinary people get to participate in the upside of AI, or merely have it happen to them? It likely depends on decisions being made right now, or perhaps on the decisions that we are failing to make.

## The cultural: who writes the story?

Ireland is small but culturally rich, with a fragile minority language, and a long experience of its identity being flattened by a dominant anglophone culture. The cultural caricatures in movies like Far and Away, Darby O'Gill or Gangs of New York still irk. No one likes someone else telling their story badly.

AI accelerates this risk in ways that are easy to overlook.

**Minority languages are at risk of degradation**. Research confirms that LLMs degrade low-resource languages not just through absence of training data but through poor quality training data: literal translations, beginner-level text, early machine translation output that encodes errors as norms. What gets baked into the model becomes the baseline. Generations of Irish speakers could end up learning from an AI that speaks a subtly wrong version of their own language. Adding insult to injury, AI also process non-English languages inefficiently: [one major study](https://proceedings.nips.cc/paper_files/paper/2023/file/74bb24dca8334adce292883b4b651eda-Paper-Conference.pdf) found that the same passage used up more than twice as many LLM tokens in Irish as in English. Because providers charge and limit their systems by the token, using an LLM in Irish can cost twice as much for an already inferior service. [Údarás na Gaeltachta](https://en.wikipedia.org/wiki/%C3%9Adar%C3%A1s_na_Gaeltachta) (roughly, the Irish state agency tasked with the defense of Irish language, regions and culture) takes this seriously, launching Ireland's first AI language benchmark leaderboard and a €1.2m initiative with TG4 to fund Irish-language digital media development. More than most low-resource language countries have managed, but unlikely to be enough.

**Then consider cultural archives**. Ireland has fifty years of video in the RTÉ archives, painstakingly digitized in an epic project at great taxpayer expense. It is an underused asset of enormous cultural value in the custody of a distressed semi-state. If it gets licensed to a foreign AI company for a one-time fee (the typical deal) it would become a perpetual source of "Irish" content under non-Irish control that pays no further dividends to Ireland.  While I was on the Irish government's AI Advisory Council we [flagged this in published recommendations](https://assets.gov.ie/static/documents/Irelands_AI_Advisory_Council_Recommendations_-_Helping_to_Shape_Irelands_AI_Future.pdf), calling for publicly-funded data to be treated as a protected national asset rather than a one-time licensing opportunity.

**One response is to treat national data as a strategic asset**. The [UK’s 2025 AI Action Plan](https://www.gov.uk/government/publications/ai-opportunities-action-plan/ai-opportunities-action-plan#secure-future) gives partner companies preferred access to valuable national datasets. Its new [Sovereign AI fund](https://www.sovereignai.gov.uk/) offers British AI startups compute, capital and access to curated national data, while its [Life Sciences AI plan](https://www.gov.uk/government/publications/ai-champions-ai-adoption-plans/ai-adoption-plan-life-sciences) proposes secure access to NHS data. In contrast, the EU’s [Open Data Directive](https://digital-strategy.ec.europa.eu/en/policies/legislation-open-data), in effect since July 2021, requires national data within its scope to be made generally available, usually for free, and prohibits exclusive arrangements. Once data is opened for commercial reuse, foreign AI companies are free to also exploit it without restriction. Europe’s new [Data Union Strategy](https://digital-strategy.ec.europa.eu/en/policies/data-union) points towards more controlled data policy, but has not yet resolved the tension between open access and using European data to attract FDI or build indigenous strategic capability.

These challenges go beyond Ireland. Every minority culture and language faces the risk of a hegemony of AI-generated media regressing it to the mean of the training data, with the costs falling on the culture being erased.

## The corporate: your business is their training data

Satya Nadella (Microsoft CEO) called it the [Reverse Information Paradox](https://snscratchpad.com/posts/reverse-information-paradox/). To make effective use of an LLM you need to tell it your proprietary context, workflows, institutional knowledge, and continuous human corrections. The byproduct is valuable "intelligence exhaust." Every prompt, every tool call, every correction subtly trains and refines the vendor's LLM. The enterprise pays for the service twice: first with money, and second with the proprietary know-how that forms its competitive moat.

Alex Karp (Palantir's CEO) [went on a tirade on CNBC in July 2026](https://www.cnbc.com/video/2026/07/01/palantir-ceo-alex-karp-says-something-has-gone-completely-wrong-with-how-ai-is-sold.html), speaking on behalf of the CEOs of companies using AI:

> *"These people are stealing the weights and alpha of my business, and they're creating a wealth tax that does not help the poor, it just punishes."*

Security researchers at [OriginHQ demonstrated](https://www.originhq.com/research/how-much-alpha-lives-in-your-ai-traces) that AI models can even reconstruct unwritten internal policies purely from the AI exhaust left behind by employees using AI over just a few weeks. The way you do business is visble to the LLM, by reading between the lines of the prompts.

Imagine an insurance company that automates its underwriting and claims processing using rented AI. The AI learns the risk models, the edge cases, the pricing logic, the fraud patterns. At what point does the AI vendor have everything it needs to open its own insurance company? At what point does the customer's continued subscription amount to funding the development of their own competitor? It's worth noting that Sequoia [identified insurance as their #1 target sector](https://sequoiacap.com/article/services-the-new-software/) for AI disruption.

**This is called [platform envelopment](https://www.hbs.edu/faculty/Pages/item.aspx?num=38631)**. A platform watches its partners and customers prove specific business cases, then ships a native competing version and eliminates them. Microsoft did it to Netscape. Apple does it to App Store developers. The third party funds the R&D; the platform holds the option.

I've experienced platform envelopment personally. In Demonware, we built multiplayer for Xbox and PlayStation. When PlayStation Network launched, game studios had a free (if inferior) alternative built into the platform. Every feature we shipped from that point was effectively R&D for Microsoft and Sony. We knew any sufficiently valuable breakthrough would be duplicated. That weighed on us, and it factored into our decision to sell to Activision when we did (where Demonware continues to run the *Call of Duty* online platform).

Likewise, Salesforce launched [Agentforce for Financial Services](https://www.salesforce.com/news/stories/agentforce-for-financial-services-announcement/) in 2025, absorbing workflows that fintech companies had built on top of its own CRM platform. Alex Karp called out Anthropic, which has already launched Claude Design, Claude Code, Claude Legal Plugin, Claude for Financial Services and Claude for Life Sciences.  OpenAI has moved into Healthcare. The major AI labs are under enormous pressure to justify their valuations, AI erodes the technical moats of companies that build upon their LLMs, and they can easily deploy agent skills at scale. Platform envelopment is no longer opportunistic, it's the intentional strategy. Lucrative verticals like insurance should be watching their back.

## The national and continental: the kill switch

On 12 June 2026, the Trump administration issued an immediate export control directive restricting use of Anthropic's Fable and Mythos frontier AI models by non-US citizens. Anthropic disabled them globally for all customers within hours.

The models were eventually restored on 30 June after Anthropic agreed to a new pre-release government evaluation framework. Meanwhile OpenAI has offered to [sell a 5% stake to the US government](https://www.theguardian.com/technology/2026/jul/02/openai-stake-us-government-ai-sam-altman) if Anthropic, Google and Meta would do the same. The US government now appears to have asserted de facto approval rights over commercial AI, may be on a path to partially nationalising its AI industry, and either way has demonstrated a willingness to abruptly terminate foreign access.

The [reaction was not calm](https://www.euronews.com/2026/06/13/wake-up-call-europe-reacts-to-anthropic-halting-access-to-its-fable-5-and-mythos-5-ai-mode). For example, Bruno Retailleau, a senior French political figure said:
> *"In the race for artificial intelligence, a nation that depends on others for its technology is a nation that can be unplugged overnight."*

The majority of the EU's AI policy effort is led from regulation lens, with its vast machinery focused on implementing the EU AI Act, which has nothing to say about protecting access to AI infrastructure or developing our own. Regulating something we don't control can create an illusion of safety. In Ireland's AI Advisory Council we had already identified this exposure in our [published recommendations](https://assets.gov.ie/static/documents/Irelands_AI_Advisory_Council_Recommendations_-_Helping_to_Shape_Irelands_AI_Future.pdf), explicitly flagging "*vulnerability to geopolitical risks, such as trade restrictions on US-based AI technologies*" as an economic sovereignty concern. This risk was clearly telegraphed, but I think everyone was surprised by how quick the US was to demonstrate its power.

The scale of Europe's economic dependency is massive. The [Draghi report](https://commission.europa.eu/topics/eu-competitiveness/draghi-report_en) discusses how Europe  failed to effectively embrace innovation during the last major disruption:

> "Europe largely missed out on the digital revolution led by the internet and the productivity gains it brought: in fact, the productivity gap between the EU and the US is largely explained by the tech sector...there is no EU company with a market capitalisation over EUR 100 billion that has been set up from scratch in the last fifty years, while all six US companies with a valuation above EUR 1 trillion have been created in this period."

![30 years of US vs EU GDP, 1995–2025](/images/2026/07/us-eu-gdp-1960-2025.png){: .captioned }
(*Source: [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?end=2025&locations=EU-US&start=1960&view=chart)*)

Whatever European successes did emerge were quickly acquired by those US companies (for example, Deepmind is one of the top three global AI labs, and was founded and runs in the UK but was acquired by Google). As a result, Europe now substantially imports its digital infrastructure from US companies. The economic analysis firm Asterès [published a report](https://www.cigref.fr/from-technological-dependency-to-economic-capture-the-cost-of-cloud-software-services-inflation-to-europe) that calculates that Europe spends €330 billion on US cloud and software providers each year. This may soar as AI embeds itself in business across the continent.

Infrastructure is something you should build, not rent. Europe needs to find a way to redirect this spending into its own innovation, digital and AI infrastructure.

Europe has domestic AI companies that are leaning into sovereignty. Mistral AI has reached a $23 billion valuation and $400 million in Annual Recurring Revenue on the pitch "[you don't want anyone to turn off your systems](https://www.startupriders.com/p/mistral-growth-playbook)" and a [clearly stated mission of AI sovereignty](https://europe.mistral.ai/). Germany's Aleph Alpha [was acquired](https://cohere.com/blog/cohere-alephalpha-join-forces) by Canada's Cohere with funding from the Schwarz Group (owners of *Lidl*) who will provide cloud infrastructure to the combined entity, with the goal of providing sovereign alternatives to US AI. This deal happened months after the announcement of the [Canada-Germany joint AI declaration and launch of their sovereign technology alliance](https://www.canada.ca/en/innovation-science-economic-development/news/2026/02/canada-and-germany-sign-ai-joint-declaration-and-launch-sovereign-technology-alliance.html), with the view that "*advanced technologies are central to economic security, competitiveness and democratic resilience*".

*The other force to be considered is China*. Mark Zuckerberg originally open-sourced the Llama LLM so that Meta wouldn't become a tenant on someone else's AI platform, openly citing tough lessons learned while building Facebook in Apple's app ecosystem. Meta couldn't win the AI race, so he changed the game so no one could win, ensuring "[power isn't concentrated in the hands of a small number of companies](https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/)" (thanks Zuck!). Now, Chinese companies are carrying the torch, collectively continuing to pull the rug out from under proprietary AI with their open source models (most notably DeepSeek, Qwen, Kimi and Z.ai's GLM). These have now nearly closed the capability gap with proprietary AI, often with much better energy and cost efficiency. For now, this is a gift to the rest of the world.

However, there are strategic downsides to becoming dependent on continued gifts from China. Broad adoption of Chinese open-source LLMs has been described as "[infrastructure colonisation](https://www.cigionline.org/articles/chinese-ai-models-and-the-high-stakes-fight-for-ai-neutrality/)": distributing free AI that carries the ideological alignment with the Chinese Communist Party. An [Australian Strategic Policy Institute report](https://www.aspi.org.au/report/the-partys-ai-how-chinas-new-ai-systems-are-reshaping-human-rights/) found that Chinese AI "*strengthen the CCP's ability to shape information, behaviour and economic outcomes at home and overseas*." An LLM, it turns out, is an excellent way to package political censorship and propaganda for mass distribution. There are probably even more subtle ways that AI could be trained to produce specific output or tool calls in response to specific triggers - an LLM equivalent of "The Manchurian Candidate".

Even if you accept or mitigate the risks in the training of the Chinese models, it would be foolish to expect continued access to the best of China's R&D for free. [Reuters reported](https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/) that in early July the CCP called in its major AI labs to discuss placing tough export controls on advanced Chinese AI, due to angst about advanced AI like Anthropic's Mythos being used as a strategic cyberweapon against China, and the need for China to develop its own countermeasures in response. In a future where the most intelligent AI is restricted due to its offensive capabilities, then all counties that don't have their own are doubly disadvantaged: they remain strategically vulnerable to cyberattack from both sides, and structurally unable to even rent access the level of intelligence that will drive the future of the world's innovation across all sciences and engineering.

The rest of the world, in short, could be cut out.

---

## The economic: who owns the supply chain?
Karl Marx argued that those who own the means of production control the economy. In an AI era, those who own the intelligence control both the economy and all future innovation. If AI replaces human knowledge work, power inevitably shifts to AI infrastructure. Wealth redistribution through middle-class wages slows down, more capital aggregates to the AI shareholders, and wealth inequality worsens.

Even Sam Altman acknowledges the danger. In 2025, he warned that "[*the balance of power between capital and labor could easily get messed up*](https://blog.samaltman.com/three-observations)." He has suggested giving all humans a personal compute budget, floated partially nationalising OpenAI, and [previously proposed](https://moores.samaltman.com/) an American public wealth fund to share the proceeds among US citizens.

The problem is that if the companies that own the AI aren't based in your economy, then you can't even tax them. The automation is purely extractive, replacing wealth redistribution through wages *within* your economy with AI fees that flow *straight out* of your economy. Unlike previous automation waves, AI primarily threatens well-paid professional workers. An [Anthropic study](https://www.anthropic.com/research/labor-market-impacts) found that workers in the most exposed occupations earn 47% more than those in unexposed jobs and are substantially more educated. The most lucrative tax payers are the first to be displaced. They might be able to upskill, or they might find that they can't outrun the pace that AI is improving at.

Governments could face a double blow: declining tax income from the highest-paid earners, at precisely the moment that job displacement drives demand for welfare, retraining and other public support.

In 2025, Eric Schmidt (former CEO/chairman of Google) answered a Stanford student's question about what most countries should do. His answer ([clip on YouTube](https://youtu.be/bnRfQNqP37s?si=w0epntBMW4tf2ZM8&t=2429)):
>  "They'll have to face the fact that this is a rich country's game. Huge capital, lots of technically strong people, strong government support, right? There are two examples [USA and China]. There are lots of other countries that have all sorts of problems. They don't have those resources. They'll have to find a partner. They'll have to join with somebody else."

Every country will have a unique set of mitigation strategies they can employ, but the time to start is now. For example, in Ireland:

- **Hosting AI.** Ireland already hosts the European operations of major cloud companies, has a supply chain capable of building and running data centers, with extensive transatlantic data connectivity.
- **Renewables.** Ireland has abundant potential for cheap renewable wind energy. AI is energy intensive, and AI data centers will be developed where cheap and abundant energy is available.
- **Climate.** Ireland's cool stable climate reduces cooling requirements in data centers.
- **Regulation.** Ireland sits within the EU regulatory framework, providing access to 450 million EU citizens, while remaining culturally and commercially close to the US, with traditionally commercially pragmatic approaches to regulatory enforcement.

**Ireland's key challenge is developing its energy**. Already, data centers consumed [23% of metered electricity in 2025](https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2025/keyfindings/), and Amazon abandoned a [€300M AI facility](https://www.irishtimes.com/ireland/2025/07/25/amazon-scraps-plan-for-dublin-plant-and-hundreds-of-jobs-over-failure-to-secure-power-supply/) adjacent to the M50 in north-west Dublin that same year for lack of power supply. When planning decisions comes down to a choice between homes or data centers, homes should always win. But a better answer is to develop the underlying energy infrastructure on all fronts, seizing the unprecedented commercial opportunity to drive investment in renewable infrastructure, and secure a fundamental part of the AI supply chain within our economy (and to tax it!).

Physical hosting is the foundation, not the ceiling. Ireland needs to climb the stack into the parts of the supply chain that generate real margin and keep skilled jobs in the economy: cloud operations, model deployment, security and compliance, grid optimisation, enterprise AI services.

---

## Participation not protectionism

Any instinct to protect by closing it off is the same mistake Ireland made for thirty years before TK Whitaker broke it.

For decades, Ireland was one of the poorest countries in Europe, drained (as Whitaker diagnosed) by protectionism.  His remedy was not to insulate further but to figure out what Ireland was good at, find the right partners, and participate on its own terms. His 1958 economic blueprint pivoted Ireland towards internationalism and participation, eventually driving its modern prosperity. That pragmatism is exactly what's needed now. 

AI is has become an arms race between giants. Europe is not yet at the table in any meaningful way. Most of the hard sovereignty problems (infrastructure dependency, data flows, regulatory leverage, strategic autonomy) can only be addressed at scale. The EU is where a serious plan needs to be made.

Ireland has a particular role to play. We sit at the intersection of interests as a common-law, high-tech, English-speaking EU member with deep ties to America. We can be more than a data center host, but build influence as a pragmatic broker that cares about the outcomes for both sides and can help shape the terms.

The question for every country, every company, every person is the same: are you drifting into this, or are you making choices? Dependency isn't inevitable. It's just what happens when you don't decide.

---

*I served on the Irish Government's AI Advisory Council. The Council's published recommendations, [Helping to Shape Ireland's AI Future](https://assets.gov.ie/static/documents/Irelands_AI_Advisory_Council_Recommendations_-_Helping_to_Shape_Irelands_AI_Future.pdf), are cited in this article. Several arguments here - particularly on data sovereignty, the RTÉ archive, and the EU Open Data Directive - draw on a working draft I co-authored that informed the Council's AI sovereignty section. That paper was never independently published; its more specific policy recommendations ran into the political constraints described above. The views expressed in this article are my own.*
