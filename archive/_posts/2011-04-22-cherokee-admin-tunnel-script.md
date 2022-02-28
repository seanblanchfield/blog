---
author: admin
comments: true
date: 2011-04-22 13:56:54+00:00
layout: post
link: https://seanblanchfield.com/cherokee-admin-tunnel-script/
slug: cherokee-admin-tunnel-script
title: Cherokee-admin tunnel script
wordpress_id: 102
tags:
- Code
- Python
- Tech
---

Cherokee is now my favorite web server, having all the performance of Nginx, but designed for usability. The addition of the market feature has made it possible to leave behind the headaches of re-learning the peculiarities of all of your favorite pieces of software every time you set up a server. For example, I moved this blog to EC2 a while back. I installed Cherokee automatically from the repositories, then used the Cherokee market to install both WordPress and phpmyadmin automatically. Lovely.
<!-- more -->
To manage the Cherokee server you use the cherokee-admin utility through a web UI. However, to fire it up you normally have to:

1.  SSH to the server
2.  Run cherokee-admin and leave the session open
3.  Create an SSH tunnel from your machine to localhost port 9090 on the server.

You tend to have to do this a lot, and it is a bit tedious. For this reason I wrote a little python script to automate those steps, and have put it in a bitbucket repository.

Run it locally, and it will start the cherokee-admin program on your server and create a tunnel to it. CTRL-C shuts everything down.Run it with -h or --help for options. You need to provide the hostname, username and SSH keyfile.

You can get it [here](https://bitbucket.org/seanblanchfield/cherokeeadmintunnel).