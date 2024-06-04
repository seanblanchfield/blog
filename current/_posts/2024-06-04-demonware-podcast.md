---
author: Sean Blanchfield
date: 2024-06-04 12:00:00
layout: post
link: https://seanblanchfield.com/demonware-podcast
slug: demonware-podcast
title: The Demonware podcast
image: /images/2024/06/demonware_sean_and_dylan.jpg
---

[Dylan Collins](https://dylancollins.com/) and I recorded a podcast on the early days of [Demonware](https://www.demonware.net/), a video games middleware company we co-founded in 2003. Demonware developed multiplayer technology for video games studios on Xbox and Playstation, just as online gaming was going mainstream. Demonware's splashscreen will be familiar to many gamers from the countless titles that have incorporated its technology, including major online franchises like Call of Duty and Guitar Hero. Demonware was acquired by Activision Blizzard in 2007, where it continues to operate as the central online technology platform for Activision games.

Here's some links where you can get the podcast, plus a full transcript.

<!-- more -->

# Podcast

Get it on [Spotify](https://podcasters.spotify.com/pod/show/middleware-files/episodes/Demonware-and-multiplayer-gaming-e2kfrbh),  [Apple](https://podcasts.apple.com/us/podcast/the-middleware-files/id1750258813) or [Google](https://studio.youtube.com/playlist/PL6V7H7cEJ65xRmQUJWMif9zO3chvXz4yd/videos).

<div class="audio-container">
    <iframe src="https://podcasters.spotify.com/pod/show/middleware-files/embed" frameborder="0" scrolling="no" ></iframe>
</div>

<style>
.audio-container iframe {
  width: 100%;
  border-radius: 12px;
}
</style>

# Transcript

**Dylan:**   Hi, I'm Dylan Collins, and you're about to hear a conversation with Sean Blanchfield about the history of Demonware, one of the original video game middleware pioneers that he and I founded in the early 2000s.

This episode was originally inspired by Mitch Lasky and Blake Robbins' [GameCraft podcast](https://gamecraftpod.com/) on gaming, which, by the way, you should check out, and specifically by our view that they skipped an important episode on the role of middleware companies in the growth of the sector. So if you're curious about the origins of online gaming or just want to hear some unvarnished startup war stories about what building companies in a pre cloud era was like, I think you might enjoy this.

---
**Dylan:** I gotta get like a pic of this just to kick things off. There's some history being made right here.

**Dylan:** Let's see if we can assemble the oral history of Demonware, or Demonware up until the Activision acquisition. The bits of the early bits of Demonware we remember. 

**Sean:** And then opinions. 

**Dylan:** Yeah, 

**Sean:** very 

**Dylan:** much. About what happened after. 

**Sean:** Yeah, 

**Dylan:** I think so. So, okay, right, let's begin. What were you doing in 2003? That was the official start date of Demonware. 

**Sean:** July 13th. 2003. 

**Dylan:** Oh, you remember the date. Wow. 

**Sean:** So prior to that, I was a PhD student and a part time CTO in Phorest. 

**Dylan:** Oh, Phorest. That's Phorest with a &quot;ph&quot;. 

**Sean:** Yeah. Our first venture. We started as undergrads. 

**Dylan:** Now, now run by Ronan Perceval. That's a whole other story. Shout out, shout out to Ronan. 

**Sean:** Yeah. Ronan has done amazing with that company. Built it up the honest hard way. 

**Dylan:** Yes. You were doing a PhD...

**Sean:** Basically trying to anonymize file sharing. I think I'd made it onto Metallica's Napster list and that had inspired me to do an undergrad dissertation in anonymizing file sharing so that no one would get caught again. And then I parlayed that into a PhD, and it was basically like TOR. So I was kind of doing darknet, in retrospect before we had darknet, but then TOR came out, and it was better. And at the same time, we were trying to do a new company and spin it out of Phorest. 

**Dylan:** I can't remember exactly how we got onto this visual metaphor breakthrough, but essentially we were postulating that, &quot;Hey, gaming at the time was all client-server, surely it would make sense to have some sort of peer-to-peer distributed model&quot;, do you remember that?

**Sean:** Yeah, I do. I think I remember the conversation. Because you and I and Ronan were running Phorest. I think you guys were full time. I was part time. We did our management meetings on a Saturday in Ronan's apartment, Wintergarden, which was our official headquarters because he had the poshest sounding address. I think you had done your undergrad dissertation on the games industry. And you had looked a lot at *Havok*, which was a Trinity College spin out at the time. And Steve was one of my former lecturers and their staff were people correcting my lab assignments as an undergrad.

**Sean:** At the end of one of those sessions, you asked a question: &quot;Sean, the kind of stuff you're doing in your PhD. Is there anything kind of networky that we could do something kind of like Havok with?&quot;

**Dylan:** So with that extremely technical question, a middleware company was born. 

**Sean:** I remember a question like that and a long pregnant pause and I was like. &quot;There might be something there&quot;. I was thinking about peer-to-peer file sharing networks like Kazaa at the time, which were federated peer-to-peer. Instead of everyone connected to everyone trying to share their Metallica songs or MP3s or whatever, there were super nodes and it was more scalable.

**Sean:** We played Quake a lot and Soldier of Fortune and stuff like that back then in the computer labs, LAN games is what existed then, and they were client-server architecture. We also knew, I think of EverQuest. So massively multiplayer games existed back then as well. Just one or two.

**Sean:** EverQuest was the big one at the time. That's where we started thinking maybe we could take this file sharing style technology and get rid of these servers. 

**Dylan:** Probably worth stating that at the time, our plan was to build what we ended up calling a network state propagation engine. That's what we thought we were going to build. A distributed network engine that would allow for multiplayer games to not require a dedicated client-server set up. So in theory, 

**Sean:** In particular, in our business plan, we were saying this multiplayer thing is probably going to take off and no one's there yet. Then we thought, well, the hardest problems are going to have to be solved. And the hardest one we can find is massively multiplayer and those servers are very expensive. So we're going to use peer-to-peer technology to eliminate those servers, so that massively multiplayer games can run in this peer-to-peer network, without there being servers. That was version one of what was in the business plan. 

**Dylan:** That was the dream. At the time, this was all, to a large degree, like pre-cloud. 

**Sean:** Oh yeah. 

**Dylan:** Right, I mean, there was no ...

**Sean:** This whole *story* is pre-cloud.

**Dylan:** Yeah. But I guess for the benefit of people listening today, there was no abstracted infrastructure. There was no AWS, there was no Google cloud platform. There was no Azure. 

**Sean:** Absolutely. The internet was there, it was smaller, but it existed. And if you wanted to put something on it, you had to get a server, and that meant a physical box and you had to connect it into something, maybe go to a data center and have a direct relationship and put the server in your car, drive it over, or whatever. 

**Dylan:** Yeah. It's hard to believe that is only 20 years ago, which both sort of a long time and not very much time at all.

**Sean:** Yeah, there's definitely a barrier to entry there, right? 

**Dylan:** It really was. And I think as we were looking at gaming at the time and we were beginning to think about where this might go, like EverQuest at the time, which had about, about a quarter of a million subscribers, a month. And that was seen as peak online gaming. Like, this was absolutely, this was incredible. It was almost unbelievable, literally. This is clearly as big as online gaming is going to be. But it wasn't so much that we thought games were going to be bigger, but we thought that there were going to be more EverQuests. Or more things like EverQuest. I think was one of the hypotheses that we had. 

**Sean:** Yeah, we thought it was cool. And we wanted to be in the middle of that. And massively multiplayer is like a hard problem. We thought in order to be worthy of success, we have to do something difficult. That's not actually how the world works, it turns out, but we were trying to find the hardest problem to solve. I think we spent most of 2002 and 2003 trying to raise money. 

**Dylan:** It took us a full year to raise money. 

**Sean:** And there wasn't many people in Ireland you could raise money from at that point. I remember we were turning up to Dermot Desmond's office, pitching massively multiplayer network middleware, but we got money. We got half a million from *DBIC* at the time

**Dylan:** *DBIC*... Dublin Business Innovation Centre

**Sean:** *Enterprise Ireland* and a couple of angels,

**Dylan:** a few angels. Yeah. 

**Sean:** Possibly the only company in Ireland in that year that raised anything. 

**Dylan:** Yeah, it was a time, it was a tough time, wasn't it? That was, it was post-, post- kind of 2001 

**Sean:** Post-bubble. Post-crash. And that was summer of 2003. I was there in my PhD saying, &quot;gee, I didn't think we were gonna succeed at that, but now what do I do?&quot; I, went to my supervisor, and said &quot;we've raised money, we're going, bye&quot; . They all said, &quot;yeah, we're sure you'll come back someday&quot;. That didn't happen. We got an office in middle Abbey street, which was the former worker's party headquarters. As Ian Kehoe described it, &quot;a shabby place&quot;. That summer we moved in and we rewired it ourselves, no, sorry, I should edit that out, we definitely didn't rewire that building ourselves. 

**Dylan:** No, enough time has passed. 20 years. I mean, we absolutely rewired that building. I mean, *you* rewired that building. 

**Sean:** You nearly cut your leg off. 

**Dylan:** You nearly electrocuted yourself. 

**Sean:** Several times. Yeah. We installed CAT5 up and down it. It's surprising how much CAT5 you can put in a building. 

**Dylan:** You know the big problem, we actually, when you say we installed it up and down, we made the mistake of installing it up rather than installing it down, instead of using gravity to our advantage.

**Sean:** Yeah, yeah, that does sound like us. Yeah, so, first couple of weeks was everyone pitching in, refurbishing the building and wiring it up. Laying carpets, building computers. So actually our workstations are built from scratch because we were frugal and we bought components and we assembled them in the meeting room. Everyone's workstation was a tower PC we built ourselves with a decent graphics card. Initial team, we didn't talk about initial team, but it was a whip around my research lab, plus John Kirk, who'd recently been in a round of layoffs from Havok and Steve Collins tapped us on the shoulder 

**Dylan:** and said ... 

**Sean:** ... if you need anyone, get this guy, he's the best.
He was in the last and first out layoffs from Havok due to their post dotcom bubble woes. He was the only experienced engineer on the team. And still probably the best programmer I've ever worked with. He professionalized a lot of us and we started building.

**Dylan:** Mmm. 

**Sean:** Version one was what was in the business plan - a peer-to-peer network that could run a massively multiplayer game. That was a frenetic time as we learned to work with each other, learned how to code for real, we were smart students, but we hadn't coded professionally, learned what source control was. All this stuff was new. John was basically teaching us. 

You were applying intense and very necessary pressure from the other room to get something that we can take on the road 

**Dylan:** We went building some demos and hypothesizing our way into the difficult thing we thought that we wanted to solve for people and went to talk to some game studios, and I remember like we would lug around like big chunky laptops. Do you remember that? To demonstrate that we had like a product that was doing networking.

**Sean:** I remember the run up to that was that demo, was paper airplanes flying around the world. 

**Dylan:** The paper airplane demo, yeah, yeah. 

**Sean:** Three of the laptops were supernodes and the other laptops were all clients and the paper airplane could fly across zones in the world, the zones being managed by different supernodes, and the transition was smooth was the point. Mostly smooth, when it didn't crash, but the paper airplane could fly from one server to another and that was handled dynamically. We were very proud of that and it was hard work to build that much. It was a hard summer. It was great. We bonded as a team. Yeah. As an engineering team. You were basically, running around in a frenzy saying, &quot;where's my demo? Where's my demo? We've got to get on the road&quot;.

**Dylan:** That, that sounds like something I would have been saying. 

**Sean:** We needed to. If you weren't doing that, we would have just as engineers just meandered around trying to build, build, build, build something huge, and, as it turns out in the next stage of the story, completely wrong. 

**Dylan:** I think we realized very early on, because we had been inspired so much by Havok, who built the physics middleware layer. The advantage of that was that because it was in the graphics stack you could demonstrably see it, whereas the challenge with the networking piece was obviously that you can't. That was something that we had hilariously underestimated, I think. 

**Sean:** Yeah. It was quite hard to describe, quite hard to show. 

**Sean:** I think that roadshow we went on, the process of getting onto it, I think was interesting because *LinkedIn* didn't exist, right? We had to try and set up meetings in an industry we really had no background in. 

**Dylan:** I remember it was literally cold emailing studio after studio after studio.

**Sean:** You had copies of *Edge* magazine, highlighting the names of people at studios. In the previous company, we had a bit of a pedigree in spam. 

**Dylan:** That's, that's harsh. It was opt-in communication. Well, was it opt-in back then? Actually, maybe it wasn't opt-in communication. 

**Sean:** The very first product was SMSing people promotions about *Smirnoff Ice*, which is an alco-pop, without their permission. That was our scrappy start in that company. In a similar vein, from knowing people's names, heads of studios that we collected from Edge magazine, we started guessing what their email addresses probably were, made a long list of guesses of email addresses and basically spammed the whole bunch with things like. &quot;Hey, just so happens we're going to be in Madison, Wisconsin on Tuesday.&quot; 

**Dylan:** We are passing through entirely coincidentally. We're going to be in your small town. 

**Sean:** Yeah. You successfully booked us I think a two or three week trip zigzagging up and down across the US. The map was like, crisscross, crisscross of the whole country for three weeks. 

**Dylan:** An absolute disregard for the realities of American geography. 

**Sean:** That was an intense trip, and we were lugging Alienware laptops with us, like, huge things. 

**Dylan:** Somewhere along the line, we realized that, actually, there's very, very few companies building MMOs, because they're so expensive, and they're going to take years. But why don't we look at these other game companies that are doing smaller things? Where they might have to think about multiplayer. 

**Sean:** I kind of remember learning that lesson on *that* trip. 

**Dylan:** It might've been that, we learned a lot of lessons on that trip. 

**Sean:** When I think about that trip, I specifically remember, Madison Wisconsin, one of the most unlikely places to randomly be, but they were like, okay, you happen to be here. We got into *Raven*, which had made *Soldier of Fortune* at that point. They said, yeah, come in over lunch, pitch the team. So we were in the canteen and the entire engineering team and CTO filed out around us for the demo. And we were demoing our paper airplanes game. 

Thankfully we weren't being judged too much on the graphics. And it might have crashed once or twice. But I think they got it. Like, see this airplane now? It's in this zone. It's going to fly over there. Now that airplane just flew from this laptop to that laptop. They just switched servers. I think I remember them going, oh, that's cool. So at least they recognized it. But then ... this could be *Zombie* in Seattle saying this either. They said, &quot;this is cool, but it's not what anyone needs right now&quot;.

**Dylan:** Yeah, yeah, yeah. 

**Sean:** &quot;Massively multiplayer is cool, but can we get four players in a session. That's what we need to do. We've got a single player game, we need a multiplayer mode.&quot; A massively multiplayer game is a totally different business proposition. I think lesson one was that first trip we were taught, we were told you gotta do session based games. And then we went back to the drawing board, we did session based games. And then there was a GDC the following March and we went back to the GDC, we were saying, &quot;yeah, we've got session based games, like client-server, basically&quot;. Basically a reimplementation of the quake networking model, Quake 2 , which Carmac had open-sourced, and we turned into basically a middleware that ran along the same lines with all the same tricks, and we were demoing it at GDC, in our little Enterprise Ireland booth. Right? 

**Dylan:** That must've been in 2000... GDC 2004, right?

**Sean:** Start of 2004. People we're like, &quot;that's cool if we were doing a PC game, but we're doing a Xbox game&quot;. 

Incidentally around that time, our business model prediction that this multiplayer thing was going to turn out to be big was on the money, and we were in the right place at the right time, because Microsoft had just dropped a billion or 2 billion into *Xbox Live* and created the space and said, from now on, every game is going to be a multiplayer game. It's got to have this checkbox on the back. So these meetings were setting up themselves at GDC. And we were saying, we're a networking middleware that helps you take your single player experience and put multiplayer into it. 

But they were like, &quot; this is a console game, which one's the server?&quot; If it's Quake or something, and someone's really invested in their computer, it makes sense that there's a server. But they're like, &quot;these are simple session based games. Can you just do a straight peer- to- peer model?&quot; Like in a racing game or something. You just want all of the players just blipping their coordinates to each other four times a second. That's all they wanted. So back from GDC that time, back to the dev team, the news I was bringing is &quot;we over engineered again&quot;. We got to go even simpler, and do straight peer-to-peer. So that was version three, from an engineering perspective, because we tried to do massively multiplayer, then we tried to do client-server, and then we're like, okay, we got to do peer-to-peer. Incidentally, peer-to-peer had its own challenges in terms of *Network Address Translation*. Trying to get people to connect to each other, which was hard to solve. 

**Dylan:** But also at the time, like, the general state of the internet right? Do you remember that being a factor? Maybe it was so early that it actually didn't matter in a sense, but it was definitely, I mean, irrespective of people's home setups. 

**Sean:** People had shitty internet connections. Network Address Translation is basically the same now as it used to be. Back then, to solve it, you had to solve it yourself. These days, you can get a library or, it's done for you. But, I'm sitting at home here and I've got a 500 megabit connection. It's not expensive. Back then our company was running on a 10 megabit connection or something. 

**Dylan:** Was it even that? 

**Sean:** Maybe not even. And the typical home connection was... two megabits was loads, it was a lot. Games like Quake were designed to run on a modem, a 56K modem. We had that in mind as that's what we're aiming for, that we use tiny amounts of RAM, like a 200K in RAM and it'll run on a modem. So. There was a lot of engineering challenge in trying to make sure that if when used correctly your racing game would perform well or your shooter game would perform well even if the player was on a dial-up modem, and it was possible, but that was a challenge. 

**Dylan:** This is a sort of flash forward / backward kind of question: when you think about the challenges that you and the dev team had then versus the kinds of challenges that a software startup today will see, are they harder? Were they harder then? Is that sort of an apples to apples question or comparison you can make? 

**Sean:** Yeah, it was harder because you had to build it yourself. These days, a lot of these problems are just solved. Examples are we needed to encrypt communication. We had to figure out a library. You don't want to write your own. We had to use [libtomcrypt](https://www.libtom.net/). We got Tom [St Denis] from Ontario to fly over to Dublin and we talked to him and you know, it was a bit more full-contact figuring out that stuff.

The Network Address Translation, so that you can get two people behind two home routers to talk to each other. We had to research this significantly ourselves and build up a system from scratch, and you'd get that off the shelf now. When it came to scaling the servers ...we haven't really got to that stage of the story... It was running on Linux, but it was before the 2.4 kernel that had this thing called *Epoll*, which allowed you to scale. But before that, it was very unscalable and it was very hard to have more than a thousand connections open to a server, or at least performance would rapidly decline after that. 

We were at that level where we're writing in C code, performant server networking code, and we were thinking about what kernel we're running on, things you just really would not think about today. There's any number of libraries that'll just solve it for you. The problem wouldn't come up because if you're running on, say NGINX or, any number of the Python web servers or any of the other languages, they all just have it built in. You wouldn't hit the problem. It's all pre-solved for you. Of course, the internet was there, but *Stack Overflow* wasn't, and the resources you have today, the kind of documentation. You could Google something and the answer you get might be an academic paper that you'd need to take a day or two out to properly understand.

**Dylan:** It's interesting, right? Cause when I think back to where the games industry was in general around that time, around sort of 2003, 2004, like it was going through a step change in complexity, right? I think it's fair to say, 'cause, it wasn't just multiplayer that was opening because you had, presumably as a function of Moore's Law, with Xbox being rolled out, and PS (what would it have been then... PS3 on the horizon?) so much more graphical sophistication, and you had all of these other middleware companies that were almost being formed in response to that. We talked about Havok earlier. We should probably do a separate section on middleware companies just in general. But you had *Havok*, you had *RenderWare* and *MathEngine*, *NaturalMotion* might or might not have been born around then. All of these different companies were there providing complexity shortcuts for the industry as it, it strained to figure out how to build with these, with these new lack of constraints, I suppose, fundamentally. It was almost like a kind of a Cambrian technical explosion. 

**Sean:** You know, in a gold rush, you make money by selling picks and shovels? And it was like a gold rush of people trying to sell picks and shovels to the other gold rush of people trying to make the games.

**Dylan:** And everyone underpricing. 

**Sean:** We should, get back to where, the answer to the *GameSpy* bit came in, though. Which is online services for games.

**Dylan:** It must have been post-2004, post-GDC 2004, that's where we first encountered GameSpy. Because it was in those same conversations where people started to say, I think it might've been an English studio that said it to us first, but it's like, &quot;Hey, we are going to build like four player sort of, PVP type thing. Maybe we've built one thing before, by the way, could you build us a lobby system?&quot; And I remember you and I looking at each other in probably near panic, me, probably naturally confidently going, &quot;absolutely no problem. We're thinking about lobby systems!&quot;, mentally going, &quot;*what is a lobby system?*&quot;

**Sean:** It's then that I remember every meeting, same feedback saying &quot;that's cool, but where's the lobby system? Do you expect us to use GameSpy?&quot; And we were like, &quot;Maybe? We're doing the hard problem here. GameSpy is in this other part of the market. You can keep on using them.&quot; And the feedback we were getting was: &quot;have you guys tried to use them?&quot; 

**Dylan:** Yeah. That actually does start to sound familiar.

**Sean:** We probably started hearing it in the first trip and we were bluffing our way through saying, yeah, lobby systems, GameSpy, yeah, yeah, of course. I think I remember thinking it was weird that you'd say there's a system for that. The lobby is just a screen with people's screen names on it, right? I mean, how do you need a system for that? 

**Dylan:** Yeah, it didn't seem difficult. And also GameSpy, like, it's funny, I mean, I'm sure there's like, someone's done the history of GameSpy, but if they haven't, they should. It was interesting that it didn't seem like a hard problem and I remember a moment where you had estimated that it was gonna take about two months. Two to three. At which point I probably just announced it! 

**Sean:** Yeah, it was about three years in the end.

---

**Sean:** Was it in response to our first customer? I think we had made the peer-to-peer stuff, right? It was like engineering version 3 of the product. Middleware for a peer-to-peer game. Was it Starship Troopers or was it Stacked?

**Dylan:** (The poker game)

**Sean:** Which one was of those was first? Around the same time.

**Dylan:** I think Stacked was the first customer. I think Starship Troopers was the first one that shipped.

![Early press](/images/2024/06/sunday_business_post1.jpg){: .captioned }

**Sean:** Yeah, I think we sold the client-server stuff to the English company that was making Starship Troopers for PC.

**Dylan:** Yeah

**Sean:** That was our first customer. That was a little bit of validation, and then around the same timeline (and I think it must have been 2004) that was when we got on to MTV Stacked, which was the two English guys in Reno, Nevada. Tim and Ian? Yeah, we started working with them. They needed some networking because they had the license to the MTV Stacked brand, which was a poker tournament, like, Texas Holden tournament. They were going to ship on Xbox. They had the scion on of the 52nd wealthiest man in the U.S. or something, investing a constant amount of cash as his pet project. So it was a project that wouldn't die, and wouldn't ship, it just kept on getting more investment, but they needed the networking bit.


**Dylan:** Myelin media.

**Sean:** Myelin media.

**Dylan:** Actually, backed by a very famous corporate raider, Carl Ican.

**Sean:** Yeah

**Dylan:** Carl Icon's son.

**Sean:** And he just kept on putting more and more money in. Right, so that was kind of like customer one or two. They had a background in slot machines, I think, the *other* kind of gaming. That's why they were in Nevada, and they were doing computer games, and it was poker. But anyway, they needed the networking bit, and they were like, well, we also need the other bit, which is we need to arrange these tournaments. So that led us into the online services bit. Yeah, "we'll do that too, we need a customer".

**Dylan:** Yeah. Yeah.

**Sean:** Us competing with GameSpy came in,  because we learned it wasn't enough for us to say "you can just go to GameSpy and they'll sell you that bit". That wasn't flying, even with these guys. So that's what we really heard: "Have you guys tried to use GameSpy? It's unusable. It's a cobbled together collection of stuff." When you read it as code, there was no coding standard. It looked like it'd be written by different interns in different years.

**Dylan:** To your point, I think it was originally just Quake server code.

**Sean:** I think it was a standalone PC application to try to find other Quake servers. That's where it came from. And then it just had other bits added in - a bit of voice, a bit of leaderboards, all kind of working in a non-cohesive of kind of way. And around this time... when did it Xbox Live launch? Around... 2003?

**Dylan:** It was announced around about then, yeah.

**Sean:** Xbox Live had launched, and it was excellent. Microsoft really knocked it out of the park in the design of this. It was a beautiful API, very well considered, compared to GameSpy, I mean. It was a very cohesive, and we looked at it and thought, from an engineering point of view, we wouldn't really change anything here. This is a really nice API. And we thought, gee, people, you know, they've got this on Xbox, they're going to need something on PlayStation. So we thought: let's make something that's exactly the same.

**Dylan:** Yeah, right. I remember this...

**Sean:**  function for function, like API call for API call, we copied it, just with a different naming standard. But if there was a function that did something that had a certain signature, like you pass a certain set of parameters in on Xbox and get a certain kind of result, then we had the same thing, which made it possible to build your multiplayer for Xbox and all of your screens and all of your UI, and then just swap Demonware in on Playstation. That was *Matchmaking+*, that's what we called that.

**Dylan:** How ... how...

**Sean:** That was Matchmaking+. That was around that era.

**Dylan:** Hold on. How long did that take to get to? We were in 2004, so that means we probably announced that coming up to GDC 2005.

![Demonware team with first customer, 5000ft, at GDC 2005](/images/2024/06/gdc_2005_first_customer.jpg){: .captioned }

**Sean:** Yeah, you said how long would take? I said, "that's just a bit of database programming - three months." Yeah, but... It was a long journey, and we were developing this PlayStation version of Xbox Live. At the same time, we had the poker game going, and we were building a custom service to manage Texas Hold'em Tournament, as a kind of plug-in for our own framework.

**Dylan:** Right.

**Sean:** For me, the memories that flood back, is sitting in our apartment in Santa Monica, which we'd rented adjacent to Activision, which kind of dates it as well, because it took longer than three months because it must have been to 2005 if I'm sitting in an apartment in Santa Monica trying to code this thing. Because, we were writing the server in C++, which was a mistake.

**Dylan:** When you think back to that, to Matchmaking+, to that lobby service, what was the hardest bit to build? It was doing matchmaking, it was doing leaderboards. It was essentially like, like, proto-community stuff. Do you remember what was surprising? I mean, other than database. What was surprising at the start?

**Sean:** The hard thing was that we made... I made... poor technical decisions. We tried to implement the server in C++, all of it, all of the business logic in C++. It's not something you should do. We did that because we thought it would be nice to just have one language that we're working on in the company. That was fragile, it crashed a lot. Starship troopers launched on this thing, and if more than 89 players connected, the servers went down.

**Dylan:** Was it 89? it was something that was predictable!

**Sean:** Because they launched on the C++ version. Yeah, apart from just that flakiness because we shouldn't have been writing our business logic in C++, individually... it was stuff like matchmaking means you have a function say that says create a session,  one of the PlayStations calls "create session", it puts a row in the database saying there's a new session and it's at this IP address and here's the name of it or whatever. And then other players would say "find sessions", and have parameters like "have less than certain number of players" or "close to me geographically" or "in my country" or whatever. Like these things aren't hard in and of themselves. These days they'd just be web services.

**Dylan:** And these were all Matchmaking services for players on the same platform. Was there any cross-platform back then?

**Sean:** We really wanted to do it. I mean, later on, we were completely capable of doing cross-platform.

**Dylan:** It was a business issue, right?

**Sean:** Yeah, it was a business issue. It would have been pretty cool. I remember... like, we get acquired by Activision later in the story. You know post-that, we were, I think even in the lab, you know, we were playing Xbox against PlayStation.

**Dylan:** Right. Yeah. Yeah.

**Sean:** Um, but it wasn't allowed to ship that way. Rewinding back a bit, writing the C++ was hard. We made, we decided to try to make it work really well on modems again. We were still married to having really high performance, so we were, we were bit-packing the requests. Um, you just obviously, today it would just be HTTP requests. And you'd send JSON or something over the wire, but we were bit-packing the requests so that they were the minimum amount of bytes on the line. So we would run well on a modem, which possibly wasn't necessary even at that time. As we moved on, some things were legitimately hard, like leaderboards. We shipped for a while with leaderboards that were bad. Xbox ones were kind of the same. Players would shoot each other, the scores would get recorded, but the rankings wouldn't update in real time. And then every night there'd be a big job that would go through and sort like the million rows and try and re-rank them. Or maybe every hour. And studios were a bit pissed off at that. Solving that was difficult, at the time. It took quite a while to figure out an algorithm that could basically have millions of players simultaneously writing data to it and be sorted in real time, so it was ranked in real time, as people's scores changed. So there were hard problems in there, like really high concurrency problems like that. I would say that most of my memories of the difficulty of it was hitting every scaling problem under the sun. This stuff wasn't documented online very well. I mentioned Starship Troopers would fall over reliably at 89 players or something, but thankfully they very rarely had more than 89 players! I think when we had a game that had more than 1,000 players, we hit a system limit of how many connections you can open to the servers. So we had to learn how to do a bit more system administration and have more TCP connections. Then it was, I think, an Ubisoft game... kind of skipping ahead here in terms of progress in sales.... (there were more games) we hit one, I think Splinter Cell had around 10,000 players. We had to figure it out, rearchitect and scale pass that. We hit  another at like 50,000 players. Then maybe it was Call of Duty 3: Big Red One, the "Call of Duty: the shitty version", that we hit another one maybe at about 100,000 players.  And we just kept... my memory of it is like you're running through a field full of rakes. Every time you take a step, you get hit in the face. But we got to ultimately, we scaled really high, to millions of concurrent connections into the system performing really well (as in, million of players), that was Call of Duty 4, suddenly like "oh crap this number just keeps on going up", and that was very hard to get to, and we had to solve these problems ourselves. It wasn't something you could Google.

**Dylan:** Yeah, but did you have a sense when we were scaling through... through those numbers, because in the beginning you know when when Starship Troopers shipped or the poker game shipped or whatever or almost anything was shipped,  the number of people using multiplayer at any one time was just hilariously comically small. I guess I'm asking you did you have a sense of history in terms of ... in that window where this huge giant industry that exists today was starting to emerge and was getting bigger and just wasn't stopping and it was going to be bigger than just the realm of Everquest players fundamentally. Did you feel it?

**Sean:** We knew it was on the rise. I mean, maybe we weren't quite sure in the first year or two. If you really cast your mind back to Demonware "n-game", or other adventures we had, trying to find a business model in year one, when we had crises, various crises of faith about what we were doing. But the theme was generally multiplayer of some kind. If you remember "n-game"? it is a bit of a side quest in this conversation, but it's entertaining. In 2003, you had the right instincts. You tried to get us to launch Steam. We called it n-game, and I prototyped something... while the team was doing the middleware I went off in a side quest and I did a visual basic app for a pitch to GameStop in Dallas. We flew over with this thing.

!["N-Game" demo app, 2003 ](/images/2024/06/n_game2.jpg){: .captioned }

**Dylan:** Wow, yeah.

**Sean:** And it was a desktop client packed full of social features, where you have friends, buddy lists, you see who's online, who wasn't online, see what games you had installed, games they had installed, and matchmaking with them. So basically the whole set of social... basically *Steam*, right? with digital distribution at its core. In terms of our sense of place in history, I've got a credit to you with having the right instincts!

**Dylan:** I mean, ironically, GameStop bought our second company, *Jolt*. Yeah, right.

**Sean:** Yeah. Well, your second company.

**Dylan:** Yeah. Well, you were pretty heavily involved. And also nearly did something brilliant.

**Sean:** So we knew multiplayer was going to be, we had these instincts, we'd seen it, we'd seen it in the college labs, we saw people basically addicted to the screen shooting each other in Quake, and Soldier of Fortune, in LAN games, we'd seen it first-hand. Microsoft was putting billions into making it mainstream, we were there, and... so I'm pretty sure we knew we were in an interesting space. We also had competition emerging, you know, so it wasn't just us with this conviction.

**Dylan:** Yeah. Well, I mean, GameSpy were there, and that company Quazal in Montreal. 

**Sean:** Yeah.

**Dylan:** Do you think... because we were based in Dublin at the time and we ended up putting some people in Vancouver (which has since become a huge I think), and we had some staff in LA for a minute, should we have moved to the US looking back? Would that have...

**Sean:** yeah, life would have been different.

**Dylan:** Yeah, but I don't think the outcome necessarily would have changed.  I mean, I think Activision was sort of there, but I think we had... was the ecosystem a factor?

**Sean:** I think in terms of selling networking middleware, you could do it from anywhere. And people were doing it from anywhere.

**Dylan:** It's true, actually.

**Sean:** You know, the only issues we were faced with in terms of sales was: "what's the time zone difference?" And then we said, "it's okay, we've got an office in Vancouver, same time zone or similar". And they were like, "oh, that's fine then." When I look back, I think if we had moved to US early in our lives, like in our early 20s, as we were then (which is a good time to do it), life probably would have been different in other ways. I think we might have had advisors and investors of quality, which we did not have. The company might have gone for longer on a different path. You know, maybe we would have ended up with Steam. When it came down to it (this is really near the end of the story) when it came down to it, and we were like "it's time to sell", that decision was forced by the Irish ecosystem at the time. There wasn't a next step for us as an Irish company, other than to sell or probably die because there was no further funding. There's nowhere else to go. And we couldn't just rock up in San Francisco and look for money.

**Dylan:** Well, not without, not without a lot more work.

**Sean:** I think my answer to that is more... step back and think that the journey would have taken a different shape. But I think we could sell middleware from here.

**Dylan:** Yeah, which was an interesting point actually, 20 years ago. Rewind to the n-game thing and things that... that kind of emerged and never were, do you remember some of the other offshoots that we saw or things that were growing related to that multiplayer ecosystem at the same time? I mean, do you remember the whole in-game advertising wave?

**Sean:** Oh, well, yeah. Geez, we were trying to do that too. And what we called DNA, we should come back to. So there was a company called *Massive*, back then.

**Dylan:** Mitch Davis.

**Sean:** there's been a few companies called Massive, but this one was in-game advertising way back, so yeah, selling virtual billboard space, basically billboards in the games, dynamically to advertisers. And I think we were looking at a some joint venture with them or something, because obviously we were connected into the games already and they were live through us.

**Dylan:** yeah there was a point at which they were trying to buy us because we realized that you had Massive, you had Double Fusion, you had IGA, you had all these companies that were trying to bring ads into console gaming. And I think there was a point where we realized we were in the best place to do that, because we were literally baked in the game and not only that.

**Sean:** Why do all roads need to advertising?

**Dylan:** Yeah, it is weird, isn't it? Yeah.

**Sean:** it's not like anyone wants to be in advertising, but we were trying to be in advertising back then, although we were in games, and we should have been happy to be in games.

**Dylan:** But the internet is fundamentally an advertising driven economy.

**Sean:** Another instinct you had was in-game analytics, that this should exist. So you announced, I think, without any involvement from engineering, that Demonware had a new product called DNA, and our joke was "DNA" stood for "Does Not Axist". But nonetheless,

**Dylan:** Or was it "Dylan's Next Announcement"?

**Sean:** You launched it, and you sold it.  And all it was basically, was saying, OK, yeah, we can collect some stuff. You got stuff, counters, you want in the game; count them up, and send them into our stats service, and we'll send you a report.

**Dylan:** But do you remember the first game? The big wrestling game at the time.

**Sean:** Oh, yeah. Like, Smackdown or something like that.

**Dylan:** Yeah. Something like that, yeah.

**Sean:** what characters people were choosing and stuff.

**Dylan:** Yeah, yeah, but it was the very first time that they were actually getting data on what players were using. I think they cut their licensing costs in half. I remember them tell me anecdotally, like a couple of years later, they were like, "yeah, we saw the data and we just, we" like they, I think they had been licensing. I mean, that was probably 2007 or thereabouts.

**Sean:** That's a lot of what Demonware does these days. It basically runs Call of Duty and it has a giant data warehouse.

**Dylan:** Let's rewind to the bit I skipped over in terms of the effort. Let's call it "the everything working" section.  When do you timestamp that? That was into..

**Sean:** 2005, 2006.

**Dylan:** I think it was more 2006.

**Sean:** Yeah, well, 2005, we launched Matchmaking+.

**Dylan:** Yeah.

**Sean:** Even if it falls over a lot, it's there. And it can be integrated into the games. And now we have an answer to this "what about gamespy" thing? We're like, yeah, we sell that bit too. You can have this thing that manages the in-game communication and the real-time stuff.  And then you have all the online services that go along with it. And it's basically Xbox Live on PlayStation. Great. And you were selling it, I was following you around, and then you were like, we need to get a sales guy.

![Demonware team at GDC 2006](/images/2024/06/demonware_at_gdc.jpg){: .captioned }

**Dylan:** Mm.

**Sean:** Or gal, but it was a guy.

**Dylan:** Mm.

**Sean:** And you had one in mind. I don't know if there's anyone else we ever really seriously considered.

**Dylan:** I'm sure we interviewed some other people, but I think when we got talking to Gamespy's head of sales, or one of their heads of sales, it became immediately obvious, or that the math on it became immediately obvious. And we had never done sales other than directly selling things ourselves. So the notion of...  
Sean ... founder sales....

**Dylan:** ... the notion of like building a funnel, the notion of even having some sort of sales management tool. The notion of working prospects. Absolutely alien to us.

**Sean:** So Art Santos was working in Gamespy, widely known in the games industry. We basically pitched him saying, GameSpy is a dated piece of crap. We have the new version. People want it. And you can basically come over here and sell the good version of what you sell into the same people. And bring your little black book, make sure you bring that little black book. And he said, yeah, "I'll do it for this amount of money", and said a number that was a bigger number than we ever heard before... like not even a lot, like $120,000 or something.

**Dylan:** I can't believe you can recall these details

**Sean:** like four times what were paying ourselves. We were like, yeah, we suppose that's probably what fancy Americans get paid. He wanted equity. What did he get? Like 5% or something.

**Dylan:** I don't remember. I don't remember the equity piece. I remember trying to deal with healthcare. That was the first experience US healthcare. Well, it was bad, it was like "insurance is how much?"

**Sean:** So.. that was a new phase of my life, because I basically became his sidekick for two years. I mean, among my other jobs. But if he needed me, I was on a plane, turned up next day. He does the pitch, now "I'm going to wheel out my geek", I open my mouth for five minutes, I close it. And then... They basically sign up with us.

**Dylan:** Yeah. The *Art and Sean Show* was very effective.

**Sean:** Yeah. And I learned a lot about sales from him, from that process. I also learned that as an engineer you can be a salesperson, good salesperson. Really, it just is the job of adequately explaining what you do and having something that's worth having in the first place. So, we started signing up customer, customer, customer. It was just a very straightforward thing: "You need to do multiplayer", "you need to build on Xbox Live anyway", "you need Xbox Live for PlayStation", "where do we sign?" Actually, do you want to talk about the pricing?

**Dylan:** Do I want to talk about the pricing? I'm not sure I remember the pricing.

**Sean:** State engine $50k. With a $20k top up per SKU. Something like that.. it was less. Crazy.

**Dylan:** The entire video game's middleware industry just so massively underpriced itself for absolutely every product.

**Sean:** Yeah. Where did this price pressure come from? People were making lots of money.

**Dylan:** I think the original pricing pressure on middleware (and this kind of includes game engines) came from the fact that you had this publisher financing model where the developers would pitch the publishers on deals, and a lot of the time they would not think about middleware or they would get pushed on price, which was essentially, you had a bucket for headcount and a bucket for tools. Yeah, yeah, and I think that's where it originally came from, that you were always just trying to shovel in the thing you needed, and if you didn't go in the first revision the publisher was probably going to deduct it from your loyalty in shape or form, so I think it's probably a contributing factor.

![GDC 2006 cable car getting stocked up by Paul Hayes](/images/2024/06/gdc_2006_cable_car.JPG){: .captioned }

**Sean:** I don't think we were profitable at any point. Some listeners might think, $50K a pop, that's a pretty good license fee. But it was highly consultative, it was very expensive.

**Dylan:** Well, actually, the addressable market was very small in terms of the number of sort of studios. But like, this was the thing, when you sort of backed in the enabling tools against the size of the sort of the consumer revenue, the publisher revenue, it was just absolutely insane. I mean, I think I looked at game engines recently and there's some crazy factor that all the the mainstream game engines today, you know, the revenue they generate as a business, is something like half of 1% of the total revenue generated by the actual games that they power. Just as a means of production versus total value, it seems kind of crazy.  Anyway, maybe there's another podcast in that, but I just wanted to complain about it on the record.

**Sean:** The pricing was, it seemed like big numbers, but it was one shot kind of stuff. We'd get renewals for the next version of the title, probably, but ... we didn't have the recurring thing in there.

**Dylan:** But hold on, back to pricing again, it's like, because this is interesting, right? Like at the time we were charging like 50 grand, but like at the time the budgets for these titles would have been like what? They were probably in the low single digit millions.

**Sean:** two million, that kind of thing.

**Dylan:** Yeah.

**Sean:** And then two million marketing. That's a formula I remember from a triple A title: two million development, two million marketing/sales.

**Dylan:** I think a big triple A game, like the early early Call of Duties, were probably coming in at maybe 10, 15 I think, something like that. Where for contrast today, you are probably adding a zero to that.

**Sean:** So Art was running around. The Ubisoft deal was a big one because Ubisoft didn't just want us in one title. They wanted to make a choice of what the preferred middleware networking vendor was going to be. And they were measuring us up against Quazal, which was our extremely direct competitor in Montreal, in the same city as Ubisoft headquarters.

![Demonware bus at E3 2006](/images/2024/06/E3_2006_bus.jpg){: .captioned }

**Dylan:** and it must be said, with the same language.

**Sean:** And somehow we got the deal. That was interesting because Ubisoft allocated an internal support team to support all of their studios using Demonware. They were investing heavily in it. And then automatically every Ubisoft title was using Demonware from  that point on. They were extremely rational as a company.

**Dylan:** Well, it was interesting, right? Because I would say that at the time, with all the big video games publishers, even though Ubisoft, well they weren't the biggest, they were really one of the top three at the time.

**Sean:** number three maybe?

**Dylan:** Yeah, but they were by far the most, or seemed to have the best grasp of multiplayer gaming and community, right? By far. They almost had it at a DNA level. Did you feel that?

**Sean:** Mostly. Say, in Activision, EA or Sega or whatever other studios you look at, people ran around with their pants on fire 24/7. At Ubisoft, people were calm, collected and thought about what they wanted to do and how they wanted to do it and then they went and did it. It seemed like an organization that planned and executed, it wasn't typical of what we saw in the games industry. Yeah, their approach to using demonware was like that. They were like, okay, we're gonna do online. We're gonna do online as Ubisoft. We're gonna support it properly. We're gonna allocate an internal team. We're gonna pick who we think is the best vendor taking the correct technical approach. We're going to invest in our team training with that vendor's team. Yeah... they really should have bought us.

**Dylan:** They tried. Do you remember? I remember going to see Yves Guillemot and saying, this is the time that Activision were buying us, and I said, "hey, like, one of your competitors is gonna buy us".

**Sean:** Yeah.

**Dylan:** And I couldn't tell whether he didn't believe or he just didn't want to pay, but it didn't happen. But yeah, they were absolutely... 

**Sean:** I remember the offers, the numbers.

**Dylan:** Yeah.

**Sean:** I'm not sure I want to mention them.

**Dylan:** But this was the thing. Like, I remember even when Massive tried to buy us and came in with the most hilariously low ball offer.

**Sean:** Yeah.

**Dylan:** But it was this, it was at the time, it was very interesting, because it was like, we were clearly a technology company, right? Clearly, right. And definitely not a video games company.  And people just weren't valuing that at all, at all. At all, right? I couldn't get their heads around why you would particularly value it at all that much.

**Sean:** But yeah, Ubisoft, all those games, and suddenly, like, 2006, 2007, we were working a lot of projects. We got to talk about Call of Duty though.

**Sean:** We've got to talk about Call of Duty though, right? 

**Dylan:** Let's go. 

**Sean:** Okay. So let's see. This is the tensest moment we ever had in our working relationship. I remember not many times in my life I've been in a conversation as tense as a conversation we had after we got called up by Activision for the first time. I think we were in each other's faces shouting. 

**Dylan:** You know, I have an emotional memory of this but not the actual detail. What was, what was, remind me. 

**Sean:** They called us up and Xbox 360 and Playstation 3 were gonna come out soon and Activision had bought Infinity Ward. And they were going to do Call of Duty 2 and it was shipping as a launch title. It was a big deal. They were fine though. They had that sorted infinity award. It was amazing studio. Activision was also going to launch Call of Duty 2 : Big Red One for the original Xbox and PlayStation two.

**Sean:** So basically a totally different title done, created by Treyarch, but under the same brand with similar gameplay but for the older consoles and what they didn't have was a networking team. So you got a call saying, &quot;Hey, you Irish guys, we hear you got a networking team. We just need you all to come over here to Santa Monica for two years&quot;.

**Sean:** Something like that. But basically they were just like, yeah, we just want to hire a team. And our, the nature of our conversation was you were saying we need to do this or we're going to die. We need, revenue. We need it to happen. This is what they need. Um, I was holding onto the, product company.

**Sean:** We do this, we're not going back. Like we're just a services company. Somehow we ended up in some big shouting match where we dug in and our respective positions. Well, obviously the answer was in between, but, startups are interesting endeavors where like things like that happen and you can get into emotional situations because you both care so much.

**Dylan:** For sure. And I think it's constantly short term versus long term or versions of that model. It's interesting that essentially our product and business model evolved after that, where we ended up actually having onsite stuff and onsite support. 

**Sean:** Yeah. There's no getting away from it. It was a highly technical product that involved a very consultative sale and a post sale process where you integrated it. But anyway, we had our little shouting match. And then we decided to go back and see if we could pitch them that we would give them intense support. But we would be selling them a product in inverted commas, licensing our core software. And they would use it in the game, but we would have at least one person, maybe two, or a team on site with them in Santa Monica throughout the entire process. 

**Dylan:** I think by the way, that the reason for my, agitation was not just needing to do it from a revenue point of view, but I, think it was at the time, 'cos Art had joined by that stage, didn't he?

**Sean:** I can't remember. 

**Dylan:** I distinctly remember it being very much flagged that this was the test for the rest of Activision. 

**Sean:** And it was. 

**Dylan:** And it was, yeah. So I think, that was probably a factor there too. And I think, , it's always, so difficult to really understand , what customer politics you're playing into with those things. It's like, well everyone's gonna say it's a test. But , to what degree is that actually true? Yeah. . Or what are the real parameters for this? Because to your point, I mean, it's easy to say this is a hindsight, like it's not about shipping an entire team out to your office, right? You know, you customer don't care about that. You care about getting the thing done. Yeah. . This isn't a compromise point. Tell us all the things you need to accomplish and then we'll figure out how to configure it for that. Right. 

**Sean:** That's what it should be. Although in Activision's case, they probably also cared about, Getting people in under their particular roof so that they could bully them more directly. Yeah, very aggressive culture as has been revealed in multiple events since then, I suppose. Anyway, we, we pitched them, you're going to get onsite support. We're going to sell you your product because that's what we need as a product company is you to be on our platform teams and two time zones working 24 seven with daily handoffs between the teams onsite is going to work with your team. They're going to hand it back to Dublin. Dublin's going to work through your night, hand it back to. The team on site, whoever you were on the phone to in the sales process, you pitched that version. They said, well, we need to do due diligence on you and David Vonderhaar is going to be arriving on Tuesday. 

**Dylan:** Remember, Vonderhaar wrote Activision's online strategy document? Which essentially concluded with just buy Demonware. 'cause he, 'cause he'd gone, he'd gone from games by into Activision. So I think that was all roughly parallel. 

**Sean:** Our office was a bit of a scruffy place and I turned up the morning of his visit, I opened up the shutters. And they're in front of the shutters where some adult underwear with a large turd. So my morning started with cleaning human feces out of our doorway before our fancy client from Activision turned up to do due diligence on us. 

**Dylan:** And I remember he was so difficult as well. I remember him being incredibly difficult. 

**Sean:** Yeah, he's prickly and he had things like he wanted to see our data center.

**Sean:** We were in Hosting365, which is an Irish, at the time a big for Ireland data center. And he he wants to see our data center. We'd never seen our data center. You went out there, didn't you? Yeah. We got in the taxi and we were driving out.

**Sean:** We saw the NOC, the network operation center, which they did have. And I have to say, I haven't seen it before, but I was impressed. I was actually speaking with Philip Reynolds, who was working there at the time. And he was describing it recently to me from their point of view that Hosting365 was thrilled they were getting this visit and there's this big shot from Activision who was sitting there, looking at their NOC that they had put so much effort in the building.

**Sean:** He came away impressed and they came away delighted that they actually got a site visit. Yeah. He endorsed us. And , we got on with Call of Duty.

**Dylan:** That must have been very stressful for you. 

**Sean:** It was just incredibly busy, but you know, that kind of busyness where it's hard, but you're in flow, getting on with what's in front of you and don't have time for reflecting on the improbability of the situation you find yourself in, get on and do it. That started Call of Duty: Big Red One. 

**Dylan:** How long was a year? I think that was a year. 

**Sean:** That was a year. Even tighter. It was really tight. , they were against the clock. It was 

**Dylan:** real death march stuff. 

**Sean:** The launch date of the consoles wasn't going to change. And this title was going to be tied to launch in concert with the next gen consoles.

**Sean:** It was, it was tough there in Activision. Like John Kirk, I think, Eoin, spent a lot of time out there rotating in and out. I was out there a good bit. We had an apartment set up next to Activision, and Craig was out there for a while. We just rotating through there month on month off or something, and then doing these daily sync calls. I remember one with I think John Kirk was out there And, we're on our conference call line again before video calls. And he was just saying, there's some scuffle outside. He says, what's happening? It's like, there's a, people are like, there's a fist fight 

**Dylan:** in the studio, in the 

**Sean:** studio. Yeah. And people were just, people were sleeping under their desks, all of this, stereotypical games industry stuff, total death march, crunch all the way through people, like not having left the building in seven days, you know, not showering, eating shit, sleeping under the desks, super stressed, out fistfights breaking out in the office, and we could hear it on the phone, but, uh, the game launched and I remember, uh, to average reviews, except for one thing. I remember reading in the reviews, &quot;lag free multiplayer&quot;. So the multiplayer was good. 

**Dylan:** Well, funny. I remember that quite differently. I don't remember that review. I do remember the game launched and there being all sorts of problems. I have very distinct memory of sending a report to Vonderhaar cause people weren't able to connect, explaining some weird outage in the US on one ISP, which was why we thought, it must be this weird thing. This is a weird coincidence. And then about a week later, we found out that something hadn't been configured properly on a server. So people were only connecting to, I can't remember technically what this was, but only had one chance in two of being able to connect anyway. 

**Sean:** I don't remember that. This was pre cloud, but it was also the servers were servers we had either bought and transported to data centers or, the data centers had bought for us and installed and we were directly managing, and directly configuring, logging into the servers, setting up the configuration files on each of them. 

**Dylan:** But, right, but even the challenge of someone on the East Coast, or West Coast, trying to play and, you know, connect to an East Coast.

**Sean:** Yeah, yeah, we were thinking about that kind of stuff. 

**Dylan:** Yeah, yeah, yeah, you actually have to think about it. It worked enough.

**Sean:** Once we had Activision as a customer and we were Big Red One, sales accelerated even more. We're clearly a safe company to work with for everyone. The only people we didn't work with were EA.

**Dylan:** Gamespy had a long term deal there 

**Sean:** Can we say that we were scared shitless of playstation network? 

**Dylan:** Oh, yes When they started to actually get serious.

**Sean:** We were making our money by selling Xbox Live on Playstation, basically and Playstation was ...

**Dylan:** weird that sony didn't try and buy us 


**Dylan:** I mean it was interesting, GameSpy ended up being sort of the last standing. Ironically of the middleware plays in the multiplayer space. I mean, and then you had things that sort of X-Fire that emerged, which wasn't, which wasn't in the lobby space, but was quite adjacent to all that 

**Sean:** it's kind of like Discord these days. 

**Dylan:** X-Fire was absolutely the precursor to Discord, no doubt. And in fact, at one point we'd had conversations with X-Fire to merge, which would have been extremely interesting. But then two weeks later, X-Fire got acquired by Viacom. 

**Sean:** Who probably killed it. 

**Dylan:** They did. Yes. I mean, almost started killing it the same day they bought it. 

**Sean:** Activision has realized a huge amount of value out of Demonware. In fact, I'd say, transformed the company, allowed Activision to become an internet company. We did not capture that value at all. And the other offers we got weren't great. Incidentally, our investors didn't have a clue, right? I don't think, um I think Our best advisors were probably Steve and Hugh from Havok.

**Dylan:** Who'd raised actual investment. 

**Sean:** But really they were on the same journey as us at around the same time. So there was a limit to how much they could teach us. We didn't have anyone advising us who, was 20 years older and had been through a few things.

**Dylan:** I think that's totally true. In retrospect, I think a few things. One, we were never thinking, or certainly I was never thinking long term enough about the company. There was the utter impatience of youth. Right. Definitely. Definitely a factor. 

**Sean:** Got this, built this, bank it, move on, build next thing. 

**Dylan:** Do the next thing. Yeah. It's like, how big can this thing possibly be? Right. And I think once we started to get into the reality of the addressable market, it was like, well, how big, how big can you really build this thing? Like Havok had built out like a much more professional sales team.

**Dylan:** And, if you think about the middleware hierarchy, even though networking was this great revenue enabler, it wouldn't be for many years to come, right? Whereas visually, physics is so ...

**Sean:** more tangible. 

**Dylan:** Well, it literally sold games, right? I mean, it became a selling feature. It was a need to have a networking was still a nice to have. And I think those were definitely challenges. Would moving to the US, specifically the West Coast, probably specifically San Francisco, have opened up things? I think I would echo your point, I don't know if it would have necessarily changed the outcome, but I think it would have changed opportunities that emerged around all of that. I think that's probably for sure. 

**Sean:** Here's my story about an alternate universe that involves time machines, me or you today has a time machine, and we go back and visit ourselves and coach ourselves on ways of thinking about a business model. In my alternate universe, I go back and I grab us by the shoulders and I shake us and I say, here's two things to consider:

**Sean:** you've already tried to build Steam, a little bit too early, right? But this is already in your heads. And right now you have a database with hundreds of millions of gamer accounts in it across all platforms. No one else has all of this account information. No one else has all this data about what gamers are playing, what their scores are, who they're buddies with in these games, who they chat with. We had that database, we had an entire game social network. We just didn't have a user interface for it or anywhere where those gamers could go and log in or link their accounts. We looked down on web stuff as kids toys. We're doing real hard C++ stuff over here in the corner... I wish I could slap myself in the face! If we could go back and reposition and say, put a damn user interface on it. Yeah, give it to the gamers. You already have all their data. Let them have their data and use it and link up with these people. I think we might've been Steam, right? Or we would've been something close. Our valuation wouldn't have been, &quot;uh, what's the cost of replacing the C++ library if we have to do it ourselves?&quot; It would've been, what's the multiple of 300 million gamer accounts? I can't believe we didn't see it, especially when we'd already thought of it because we were trying to do this Steam n-game style thing in 2003.

**Dylan:** But but you have to bear in mind as well, like capital was a factor to do that.

**Sean:** And there was nowhere to get capital where we were. 

**Dylan:** No. And we didn't know how to pitch what it was. And I absolutely agree. And I think like you could have spun up almost any consumer surface, at that point with exactly , the access that you described and I think that there were interesting things to happen. When Joel got acquired by GameStop, at that point you were involved, right? We were starting to think a bit more like that when we were going into their point of sale systems and looking at like, yeah you know, I think I think there were definitely some learnings from it, but there have been efforts that sort of like gamer clubs and gamer loyalty platforms and things like that and even though the big things that emerged were essentially like communications platforms like in X-Fire, discord, Steam ...steam was successful; Steam took a long time to be successful and probably, the Valve folks would say really only as a function of the amount of money they were able to throw at it too, which came off the back of Counter Strike and everything else. Right. I think there is, you know...

**Sean:** It might've been a longer journey. It might've had also had an early exit, but maybe based on a different formula, valuation formula, um, we would've needed more capital because we were out, right. And our business model. With our shitty pricing we weren't able to scale. We weren't able to grow. We weren't able to continue. Um, we were scared of PlayStation Network , unnecessarily in retrospect, because, there's a lot of value still to create on Xbox and on PlayStation, going further, like using Demonware instead of PlayStation Network , doing custom services and a lot of stuff that kept Demonware busy for years after that, uh, despite PlayStation Network and Xbox being given away for free. But, We would have needed another round. Yeah, for sure. We did do a second. Did we got a top up? Didn't we got 500k seed round? Seed round in 2003 money, I suppose in Ireland. Um, we got another quarter of a million or something. Did we get a top up from the same investors? 

**Dylan:** Something like that. Yeah. It was small. It was small, 

**Sean:** but there wasn't another one after that, right? 

**Dylan:** Look, hindsight is, is all the things, but it was certainly a different environment, but that's why it's always interesting to have these sorts of chats, right?

**Dylan:** Cause you can sort of look back and think about it and, where you see opportunities today to apply this kind of thinking, you can. Um, because there were like, there were lots and lots and lots of companies that tried to get into the game space in terms of middleware. And we haven't talked about the many failed companies we saw along the way, that had absolutely no outcome whatsoever. 

**Sean:** We were 26 and 27, and sold it, and we were kind of set up.

**Sean:** It's gratifying that Call of Duty is there and DemonWare still runs it. And that the genesis going back to 2002 was Counter Strike was great fun and we were playing it in the lab and Quake and particularly Counter Strike. And then Call of Duty is Counter Strike

**Sean:** Ironically, I actually really liked the single player missions. 

**Dylan:** Demonware last year, celebrated its 20 year anniversary. As an acquisition, you can't put a look at that and go, that was an incredible success. And I still meet people ex-Activision people who have been gone there five, 10 years, and they're like, holy shit, that was the best deal we ever did.

**Sean:** Yeah. 

**Dylan:** But my question is not going where I think you think I'm going. My question is , why do you think it has been so successful? Was that the DNA, the roots? 

**Sean:** Activision was selling boxes in shops . That's what games companies did. Really zooming back out, the Demonware acquisition converted Activision into an online services company and Demonware became the backbone of that transition.

**Sean:** The culture of the company was slowly but surely transformed into, an online digital, games publisher. And yeah, Demonware basically was the backbone of that. The culture clash burned me out and caused me to quit, but they got there in the end. And right now, inside of Activision Central technology the platform is Demonware.

**Sean:** The message right through Activision, as I hear it, among the studios, do what you like but don't fuck with Demonware. , . Right, right, right, right. Activision makes like so much money from call of Duty in particular and Warcraft and other stuff. And like it's all kind of centralized into, I think it's all centralized through.

**Sean:** Um, maybe not Warcraft, I'm not sure. Obviously, all of Call of Duty is. I think they moved a bunch of Battle. net across to it, I believe. And I think King is doing its own thing. So why is it valuable to Activision? They turned from a company that sold DVDs into a company that delivers product digitally and was excellent at it.

**Dylan:** Which was a remarkable transition for a 

**Sean:** company to do. it's not quite the Demonware we sold them. We were 25 people when they acquired and, it's more than 10 times that now. But that's the next part of my answer. The people. Don't know how you feel, I mean this with great respect to everyone I've worked with since.

**Sean:** But it's the best team I've ever been on. Hmm. I think that was a question of timing. That team was assembled in 2002, 2003, you know, I looked around my research lab. Who wants to be in the games industry and got the first group, and then John, John Kirk over from Havok. 

**Sean:** So that was, John Tillman on Dave and myself, that was the initial dev team. Uh, then when we started to hire, we basically went back to college and we started getting people at Netsoc like Michael Collins and Steffen. Um, and then we started expanding saying who else is in an internet society that people, good people knew each other, you know, uh, Vlad, Rob Sennett, Emmanuel, um, Morgan Brickley, Morgan Brickley, like DC Redbrick or UL Skynet.

**Sean:** Craig came from there, you know, everyone knows each other. Uh, we need another great person. Who do we know? Well, and someone would say like, Rob is graduating this year. We need to hire him. Okay. Where is he? And he's in, right? And we just got the best in the country, the smartest graduates. And we had the pick of Ireland, Irish universities, ?

**Sean:** If we needed another smart programmer, we got the smartest one that was graduating that year. So the raw talent in the room was phenomenal. Even if you didn't have a lot of experience, people learned, a thousand miles an hour. That was the same year that Google moved to Ireland, 

**Dylan:** right?

**Dylan:** Well, this was my question for you. Why did they join? How much of it was, Oh, cool. It's video games versus how much of it was, Oh, this is difficult. Versus how much of it was preexisting team? 

**Sean:** Well, those are the three things. I don't know what the ratio is. Video games is cool.

**Sean:** People wanted to solve hard problems. Everything was hard back then, scaling up systems, online, we were basically inventing this stuff half the time. It certainly attracted a certain kind of person, but also the fact that, it's very powerful when you're asked to join a company by someone you already know and respect and want to work with and you've worked with in college and here's a chance to work with them professionally and get paid.

**Sean:** And what it wasn't was the money. Sure. Yeah. While we were paying ourselves like 30, 000 euro. That was a big salary for us, at the time and that's what the developers are getting paid maybe after a few years ramping up to 40, so inflation and everything but you know It's different days these days.

**Dylan:** Back then in early mid 2000s you had less startups certainly in ireland, but even generally when you look at the many startups that you look at today I think I had a much tougher time recruiting that density of talent because People are more inclined to think about their own startups as a viable path, a viable alternative.

**Sean:** Yeah, every time there's a crash, you get a good lot of good people like the 2007 2008 financial crash, you know, great news for startups. Sure. Right, it frees up talent to get into small companies and other people start companies. You know, there were a few years there where there was like a thousand startups in Dublin.

**Sean:** Now, these days, This is Dublin where it's got a lot of international tech here for a relatively small population. But the people who I would have hoped would have started their companies and been the next crop of extremely talented engineers, the top of their class in the universities and I've worked with some of them.

**Sean:** They're all working in Meta, HubSpot, Intercom, getting paid, 200, 300, maybe 400, 000 like total compensation, basically it makes zero financial sense to consider doing a startup relative to that. They'll become rich just sitting where they are.

**Sean:** There's people I thought with next to you and me, but they're there now. And they have been for the last seven or eight years. And good for them, I suppose, but not great for the economy. 

**Dylan:** That's a wrap. This was amazing. this was a lot of stuff. Okay, let's click save. Yeah. Okay, thanks for listening.


![Dylan Collins and Sean Blanchfield in Demonware HQ, 69 Middle Abbey Street, Dublin (circa 2004) ](/images/2024/06/demonware_photoshoot.jpeg){: .captioned }
