---
author: Sean Blanchfield
date: 2023-02-25 16:00
layout: post
link: https://seanblanchfield.com/anntem-433mhz-rf-receiver
slug: anntem-433mhz-rf-receiver
title: Overview and Configuration of the Anntem 433Mhz RF Receiver
image: /images/2023/02/anntem-433mhz-rf-receiver.png
tags:
- Code
- Electronics
---

I figured out how to configure and use the barely-documented but highly efficient [433Mhz EV1527 RF receiver from Anntem](https://www.aliexpress.com/item/32913158676.html). Unlike most receivers of its type, this uses just 100&micro;A, giving your device a potential standby battery life of 4 or more years. Here's a short Youtube video I made with all the details.

<!-- more -->
<div class="video-container">
    <iframe class="video" src="https://www.youtube.com/embed/MGSSIwKDliA" allowfullscreen></iframe>
</div>

<style>
.video-container {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%;
}
.video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}
</style>

# Transcript

Recently, I was looking for an RF wake-up receiver for my current project. It’s a battery powered project, and I need it to be powered off until a low power module receives an RF signal and wakes the whole thing up. While hunting around for something cheap, available and suitable, I found this module on AliExpress, by Anntem. It was advertised as the “DC3.5V 6V 9V 12V RF wireless remote control 433Mhz lithium battery power outlet on/off mini small switch module controller”.

Unfortunately it didn’t come with any documentation, but I figured out how it works so I thought I’d share a tutorial here. I should mention that Anntem has a Youtube channel, as shown here. They seem to make lots of different types of RF receivers and transmitters, but unfortunately they don’t have a video covering the one I bought. Also, their videos are quite short, not primarily in english and are a little ambiguous. 

The receiver module comes with a battery-powered transmitter (like a regular garage door opener kind of thing). In fact, I got this with two identical transmitters. They work in the 433Mhz band, which is license free in a lot of countries for use by short-range low-power devices like this one. Each transmitter has a unique built-in ID that you can’t change. Because I ordered my receiver with two remotes, these two remotes have the same ID. The receiver can be paired to particular transmitter IDs.

Let’s do a quick review of the receiver. This is the antenna. You can stretch it out and play with it to try to get a better reception. I didn’t find that necessary, because I can transmit about 30 meters through my house and car without issue. There are 4 wires attached to it. Here is VCC and GND. Then we have a blue wire, which is our signal out. Then we have a second GND lead, which is physically connected to the first. 

The transmitter has two buttons. When you buy them you can get them with different icons on them, but I am sure they are all the same on the inside. Each button transmits a different code.

These transmitters are using the EV1527 chip to encode the radio signals, which is widely used in RF remotes. The RF receiver could be more specifically called an EV1527 receiver, because it should work with any of the many types of EV1527 transmitter that you can buy online. You can also get EV1527 learning remotes, which can clone the ID from an existing remote that you have.  The EV1527 chip uses amplitude shift keying, or ASK, to send a transmitter ID and a button ID, and any compatible receivers in range will check the transmitter ID to see if it is paired to it. You can look up more about this online by searching for EV1527.

The receiver and remotes just worked out of the box for me, but I needed to pair an additional receiver to the same remotes. You might also just be interested in the different modes you can configure this to work in.  Programming it involves shorting these two little pads here. I don’t have my good camera here so I’m going to do this the old fashioned way and use a magnifying glass. Here are the two pads. If we short them we can send commands to the module. We can place it in different modes, factory reset it, or pair a new remote. If you have a RF receiver that is similar but not identical to this, you might see these pads somewhere else on the PCB, or you might have a pushbutton soldered over them so you don’t need to use tweezers like me.

First, let’s do a quick demo. When I press this button on the remote, we see the multimeter reading the voltage on the blue signal wire. It went up to 9V. That happens to be the voltage my power supply is set to. The receiver is currently in momentary mode so whenever I hold this down we get the 9V and when I release it goes to zero. We can set the receiver to momentary mode, latched mode, toggle mode and a few versions of latched mode with different timeouts. 

A note on power consumption and what attracted me to this receiver in the first place. This particular model of receiver, which is on the battery powered side of my project, has very low power consumption, which it achieves by being asleep most of the time. I took information from the product listing and from my own testing to figure out what the sleeping schedule looks like. In summary, every 800ms it sleeps for 790ms and wakes up for 10ms. While sleeping it has ultra low power consumption of about 5microamps and when it's awake it draws about 7milliamps, which all averages out to about 100 microamps, which is ideal for battery-powered projects like mine. 

In my project, everything except this receiver is fully powered off during standby, giving me a standby or quiescent current of just 100 microamps, which is theoretically years of standby time.

Let’s try programming it. It’s all about shorting these pads. Let's see if we can get the magnifying glass on it so you can see, which is a little fiddly with a camera in the way. If I short it with the tweezers I get 1 flash, pause, 2 flashes, pause, 3 flashes, and I can release at any point to leave it in a certain configuration. That goes all the way up to a pattern of 8 flashes and then it stops. 
If I touch these and wait for one flash – it can be a bit tricky to make sure you have contact – that’s one flash. It should now be in momentary mode. So if I press my primary button… I get VCC, release it and it goes back to zero. The secondary button in this instance does nothing, because it’s in momentary mode. 
If I wait for 2 flashes it should go into latched mode. So if I hold the contacts. 1… 2. I should now be in latched mode. If I hold the primary button I get VCC, press it again it stays at VCC, press the secondary button it cancels it and it goes back down to ground. 
The next mode is toggle and that’s at 3 flashes. 1. 2. 3. It should now be in toggle mode. When I press the primary button I get VCC, if I press it again it cancels it. One more time. Primary button gives me VCC. If I pressed it again it would go back to ground, but I can also use the secondary button to cancel it. So that’s toggle mode and in that mode we really only need to use the primary button. I don’t know what use that is, but I guess the circuit might be used in other kinds of controllers that just have one button and maybe they are shipped from the factory in toggle mode. 

So that’s 1 flash, 2 flashes and 3 flashes. 4, 5, 6, 7 flashes give you different versions of latched mode with automatic timeouts. For example, 6 flashes is latched mode with automatic timeout after 60 seconds. See the table at the end of this video for a summary of all these modes.

If we wait for 8 flashes, we factory reset the receiver, so let’s try to do that. 1. 2. 3. 4. 5. 6. 7. 8. It should now be reset. So that means that the remote now does nothing. It is unpaired from the remote. At this point we could get a different remote with a different ID built into it, or we can pair this remote again, or in fact we could swap the buttons. 

During the pairing procedure you press a primary button first and then a secondary button, and the receiver learns the transmitter ID and those button IDs. In my case, I’m interested in having the bottom button as the primary button and the top button as the secondary, but you might want it the other way around. So, how do we do this? This is about very briefly shorting the two pads. When the LED lights solidly, it is indicating that it is in pairing mode. So let’s try it. There we go. Now first I’ll select the bottom button as the primary … top button as secondary.. Okay it should now be paired. And I think it should have reverted to momentary mode, which is the first mode you set this waiting for just one flash.  Yes, momentary mode. Holding it down: 9V. Release: down to ground. 

I hope that was useful. Here’s a table listing all the available modes.

