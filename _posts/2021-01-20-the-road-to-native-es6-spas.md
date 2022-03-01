---
author: Sean Blanchfield
comments: true
date: 2021-01-20 13:53:19+00:00
layout: post
link: https://seanblanchfield.com/the-road-to-native-es6-spas/
slug: the-road-to-native-es6-spas
title: The road to native ES6 SPAs
image: /images/2021/01/road.jpg
tags:
- Code
---

**TL;DR**. _In this post I go on a major rant against the Javascript/Babel/Webpack/Node development stack, and then talk about the problems I'm facing in my attempt to jettison that stack and instead make my javascript application run natively in web browsers. (Run javascript in a browser? Revolutionary, I know!)_
<!-- more -->

## The Rant

I started professional software development writing C++ for video games on strange platforms like Playstation 2. It was a world of compilers, linkers, cross-compilers, symbol stripping, tedious debugging tools, and frustrating build times. For most of the 2010s I thought this was all ancient history (these days even embedded systems benefit from high-level languages). But these arcana are no longer anachronistic to the javascript developers of 2021, who toil against the same challenges, just with new names. Instead of compilers and cross-compilers, we have transpilers (which, like a cross between a compiler and a Star Trek transporter, sometimes have catastrophic accidents). Instead of linkers we have "bundlers", which perform roughly equivalent roles. Instead of compiling with symbols, we include source maps. Instead of upgrading our workstations so we can build an exe, we are upgrading our CI hardware so we can build a Javascript bundle.

In fact, the current situation is even more dire. In the old days, we would be deeply suspect of any 3rd party library that tried to bring in its own dependencies. The few indirect dependencies that ended up compiled into our products were subjected to the same scrutiny as the direct dependencies that required them. Contrast that to your current `packages-lock.json` file or `node_modules` directory.

Let me tell you about _my_ `node_modules` directory. For a vanilla Vue.js SPA project with recommended webpack/babel build pipeline, configured with Vuex and Vue Router, Vuetify, plus 16 additional dependencies that I intentionally added for UI features, running "npm install" creates 509Mb of dependencies across 1185 packages.

What are these 1185 dependencies? I don't know. What are they doing? I can't afford the time to find out. They mostly seem to be dev dependencies, so although they could be up to all kinds of [no good](https://www.theregister.com/2018/11/26/npm_repo_bitcoin_stealer/), it's mostly me that's at risk (but by extension, any of them could probably try to inject code into the final bundle, which would be executed by end-users). I am also nervous that some of these dependencies (which I didn't put there), throw deprecation and security warnings when I do an "npm install".

Add these 509Mb of dependencies to a slim docker linux image, Node.js itself, and puppeteer for server-side pre-rendering, and my frontend dev docker image weighs in at least at 1.5Gb. That's big enough that building/pushing/pulling the image lengthens deployments. Meanwhile, javascript build/bundling performance is horrendous. On my i7 8-core laptop, starting up the javascript dev server can take minutes. On the cheap kind of virtual server that I am inclined to use for CI during development, bundling the javascript application can take 30 mins or longer (in fact, half the time it crashes during prerendering due to some unhandled timeout deep down in puppeteer's guts). Therefore, I need to spend money on putting some real horsepower behind my CI server just to handle building javascript. In short, build times are now worse than they've been at any time in my career since 2001.

I could also moan about cumulative weeks lost to babel or webpack misconfiguration thermonuclear explosions, or about the misery of trying to use Chrome dev tools to debug babel's version of async-await code.

Perhaps the strangest realization I've had over the last two years of diving head first back into web development is that the typical frontend developer doesn't seem to realize there's anything wrong with the current situation. It's as if there's an utter generation gap between the developers who suffered (and fixed) poor tooling in the 1990s, and those suffering through it today.

For now, let me draw a line under the modern Node.js/webpack/babel SPA build pipeline by saying that IMO it may be the worst dev experience I've encountered so far, with dramatic consequences for my productivity.

## The Solution (?)

There must be a better way. Why can't we build a real SPA using vanilla ES6 in the web browser? Ruby on Rails creator DHH agrees:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Native ES6, with module support, in browsers is the most exciting development in JavaScript since the advent of transpiling. And it’s the opposite! A return to JavaScript that doesn’t require a horrendously complex tool chain and build tools is 😍</p>&mdash; DHH (@dhh) <a href="https://twitter.com/dhh/status/1334428951180173313?ref_src=twsrc%5Etfw">December 3, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

The basis of this argument is that the Node.js/Webpack/Babel build pipeline for front-end javascript was initially necessary because:

1.  Any large project needs to organise code into modules, and browser javascript didn't support that yet. So you could do it in Node.js instead.
2.  People use all kinds of web browsers, many of which support old dialects of javascript. To solve for this, you want to write to one particular JS spec and convert it for use in multiple browsers, using something like Babel.
3.  There would be a large performance penalty on web browsers if they tried to download hundreds or thousands of javascript modules separately. Instead, you would bundle them up, for which you need a server-side javascript build process like webpack or rollup.

These were very valid reasons in the past, but not necessarily in January 2021. According to [CanIUse](https://caniuse.com/es6-module), 92.48% of web browsers in use now support Javascript modules. This will probably be more like 96% by the end of the year. Meanwhile, they report that ES6 is supported by 94.37%. Therefore, if you are willing to detect and reject IE and Opera Mini, then points (1) and (2) above are no longer an issue. Meanwhile, the performance question addressed by point (3) is largely addressed by HTTP/2 (which is now supported on [95.5% of devices](https://caniuse.com/?search=http%2F2), or in other words, supported by recent versions of every major browser except Opera Mini).

_Preemptive defense_: I know bundling tools like webpack will always be able perform some additional optimization, like tree-shaking, but I could also argue that the root problem there is bloat due to poor dependency discipline.

Taken together, this means that in theory we should be able to write a pure ES6 SPA today without Node.js, a "bundler" or a "transpiler". Inspired, and in a fit of frustration, I decided to try to port my entire SPA codebase back to ES6. It didn't quite work out (yet). The high-level reason is that it turns out that not only have we collectively used our Node.js build pipeline to solve the original three problems, but we've gone further and solved some other problems too, and our frameworks and tools now have some inconvenient assumptions built-in.

Consider any code or dependencies that try to access information about the Node/Webpack execution environment. The webpack "[module](https://webpack.js.org/api/module-variables/)" API and the Node "[util](https://nodejs.org/api/util.html)" and "[process](https://nodejs.org/api/process.html)" APIs do not exist (and would not make sense) in code running in a web browser. In a conversion to browser ES6, you need to eliminate any dependency on these utilities.

A bigger issue is that Webpack allows you to use custom "loaders" to handle different kinds of files you want to process in your project. Typically you end up using the "import" keyword to bring these into your project. You might import a CSS file, or a stylus file, or a markdown file. However, ES6 modules only allow _javascript modules_ to be imported. There is no way it can possibly support importing a file type just because someone wrote a webpack loader for it. Therefore, porting to vanilla ES6 means finding an alternative way of handling non-JS file types. You could load resources like CSS files directly in your index.html (which unfortunately introduces a new dependency between your index.html page and various sub-components that require the resource). However, files that require pre-processing, like Markdown or Stylus need more work. You could create a manifest of these files somewhere and run them through a javascript pre-processor (if you can find one that works in a web browser, not just in Node.js). Either that, you need to go backwards and reintroduce a server-side Node.js build step.

> The tragic norm is that the legality of javascript import statements depend entirely on the contents of your project configuration files.

Taking this problem a bit further, in Vue.js you can import a ".vue" file, which is a Single-File Component ("SFC") that couples together the HTML template, CSS and javascript that drive a particular component (which is quite nice, and is further helped by editor support for code highlighting, linting and formatting). In this case, the javascript code that runs in the web browser is the result of a pre-processing build step, and it is accompanied with source maps for debugging. You could presumably try to load a manifest of these files from javascript, parse the contents and attach the pieces to the DOM, but you would probably have a very hard time debugging the result. [Vue3-SFC-Loader](https://github.com/FranckFreiburger/vue3-sfc-loader) is a project that attempts this, but admittedly faces serious debugging drawbacks (at least on Chrome). Another approach is to ditch the official Single File Component format and write pure-Javascript (e.g., attach HTML templates to Vue components as raw strings, and place component CSS in a global stylesheet). However, this would be at the cost of all that excellent tooling (e.g., editor support for .vue files), departs from the intended usage of the framework, and could lead to incompatibilities with future versions and add-on libraries.

The meta-issue is that there hasn't been a strict distinction maintained between language features, Node.js features and webpack features. Popular javascript frameworks have lurking dependencies on webpack and Node. The tragic norm is that the legality of javascript import statements depend entirely on the contents of your project configuration files. In the Node.js/Webpack/Babel world we could get away with loose distinctions. If we want to write pure web browser ES6, these distinctions must be honored again, and we will need to perform an exorcism on some incorrect assumptions that are deeply embedded in a large stack of frameworks and development tools.