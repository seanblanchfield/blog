---
author: admin
comments: true
date: 2022-02-01 15:13:44+00:00
layout: post
link: https://seanblanchfield.com/automating-the-hy367-hy368-smart-radiator-actuator-in-home-assistant/
slug: automating-the-hy367-hy368-smart-radiator-actuator-in-home-assistant
title: Automating the HY367 / HY368 Smart Radiator Actuator in Home Assistant
wordpress_id: 1404
tags:
- Tech
---


The HY367 and HY368 Smart Radiator Actuators are relatively cheap smart thermostatic valves that you can attach to the radiators in your house, effectively turning each room into an individually-controlled heating zone. They seem to be on sale rebadged as Hysen, Blinli, Moeshouse and Tuya (I think Tuya is probably the real manufacturer). As of February 2020, you can get these for as little as $22 each on AliExpress. Unfortunately, the instruction leaflet that they come with is pretty cryptic and omits some important information. After hours of experimentation, here are some notes that may be useful for anyone else trying to integrate these into Home Assistant.
<!-- more -->
![](/images/2022/02/hy367.jpg)

The HY367 in "heat" mode

As background context, my goal is to maintain consistent temperature in each room by turning radiators on or off based on the state of separate temperature sensors in each room. I suspect that the accuracy of regular Thermostatic Radiator Valves (TRVs) are affected by their proximity to the radiator. I think these smart valves are mostly designed for people who want to set a target temperature and let the valve try to manage itself to reach it, but I think that this will have the same issue as regular TRVs: the temperature right next to the radiator is not necessarily the temperature experienced by people using the room. Therefore, I needed to find a way to explicitly open or close these valves from home assistant.

Here are my notes:

*   It is not necessary to install the Tuya app to use this. It can be paired directly with a normal Zigbee controller (in my case, a Conbee stick connected to my Home Assistant). To place it in pairing mode, hold the left and right on-screen buttons for ~10 seconds until the "WiFi" icon starts flashing. I paired it with Phoscon, but I see other people online pairing it with zigbee2MQTT.
*   It has "preset modes" including "auto" (which features a programmable schedule), "holiday", "eco", "manual" etc. To control it from Home Assistant, I set it to "manual" (to prevent it from trying to control itself). I did this via the on-device controls.  
    
*   I have configured the advanced setting "Control type of valve" to "1: ON/OFF", because this seems to match the commands I can send from Home Assistant. The alternative would be to set it to "PID" (whatever that stands for), which presumably allows the position of the valve to be explicitly set. However, I cannot see any way to send a command like that from Home Assistant (perhaps it is possible via the Zigbee2MQTT integration, which I am not using). I also have no desire to set it to a variable position. ON/OFF is all I need, given that heating flow rate should be manually adjusted with the lockshield valve on the other side of the radiator.  
    
*   I have turned on the "childlock" feature, which just locks out the valve buttons and dial after 10 mins of not being touched. Through experimentation, I have discovered that you can bypass the childlock by holding the "boost" button for 10 seconds. It does not appear to be possible to configure the 10 minute inactivity timeout.  
    
*   It has HVAC modes "heat", "off" and "auto". You can set this via Home Assistant service calls _climate.turn\_on_ (sets it to "heat"), _climate.turn\_off_ (sets it to "off") or via _climate.set\_hvac\_mode_. If set to "auto", it will turn itself on or off as necessary to reach its target temperature. Annoyingly, while it is set to "heat" or "off", it will switch back to "auto" if anything is pressed on the valve itself. Therefore, to keep it working as expected with Home Assistant, I'll need to childlock all the valves so that no one can fiddle with them. I might also set HA to frequently reset the HVAC mode in case it has somehow been switched to auto.  
    
*   The valve state reports 0 - 100, where 0 is closed and 100 is open.  
    
*   If the HVAC mode is set to "auto", you can use the _climate.set\_temperature_ service to open or close the valve. The valve will open or close as necessary, regardless of the "preset mode". E.g., it will still open/close automatically if "preset mode" is set to "manual". Bluntly, as a Home Assistant user, I think it's best to place "preset mode" into "manual" and then forget that it exists.  
    
*   If the HVAC mode is set to "heat" and "preset mode" is set to "manual", then the valve will open and stay open regardless of the current temperature or any target temperature you set.   
    
*   Similarly, if the HVAC mode is set to "off" and "preset mode" is set to manual, the valve will stay closed regardless of temperature.
*   It takes about 10 seconds for a command sent to the device to result in a state change on the device, or for the motor to activate. I suspect that the device might have a short wake-up interval of 10 seconds. This might place a high load on the 2 AA batteries that power it.

I can now leave it in "manual" preset mode, turn on the child lock, and reliably open and close it from HA by setting the HVAC mode (and basically ignore the target temperature setting and all the fancy modes). My main remaining concern is battery life. If it is short due to frequent wake ups and the work involved into running the motor, then I may limit my usage of these to one or two rooms where there is substantial net benefit vs regular TRVs.

Alibaba links for HY367 for $22: [HY367](https://ifreeq.en.alibaba.com/product/1600327674275-901867413/HY367_Zigbee_Radiator_Actuator_TRV.html?spm=a2700.shop_plgr.41413.32.33272c15ROyd7c) and HY368 for $25: [HY368](https://www.alibaba.com/product-detail/HY368-Zigbee-Radiator-Actuator-TRV_1600327750522.html?spm=a2700.wholesale.0.0.7f585cad6h6Slb).