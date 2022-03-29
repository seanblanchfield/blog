---
author: Sean Blanchfield
comments: true
date: 2022-02-23 22:58:15+00:00
layout: post
link: https://seanblanchfield.com/automating-heating-with-home-assistant/
slug: automating-heating-with-home-assistant
title: Automating Heating with Home Assistant
image: /images/2022/02/wall-panel-1.jpg
tags:
- Code
- Home Automation
---

I’ve been on a mission to use Home Assistant to optimize my home heating, with the dual goals of reducing gas usage and increasing comfort. It’s worked out very well - I’ve mostly eliminated wasteful overheating, and I now have much more consistent temperatures throughout the house. Thanks to the power of [Home Assistant](https://www.home-assistant.io/), I managed to do this without having to invest in new smart devices. In fact, I ended up selling my Google Nest thermostat! I thought I’d share some notes on the process.

<!-- more -->

## **Key lessons:**

*   Smart Thermostatic Radiator Valves (TRVs) are not necessary. Regular TRVs get you most of the way there, if you use them well.
*   My Google Nest Thermostat was part of the problem, and I needed to get rid of it to improve my home heating. The problem is that any central thermostat will shut down the boiler as soon as it reaches its target temperature, even if there are other areas in the house that still need to be heated.
*   Home Assistant is a wonderful investment that pays increasing dividends over time. In this case, my Home Assistant was already connected to enough smart sensors that it already knew way more about the temperatures in the house than Nest did.
*   Home Assistant’s built-in Generic Thermostat integration is a pretty good replacement for Nest temperature control.
*   Putting Home Assistant in charge of the boiler opens up many more opportunities for heating automation than could ever be achieved with Nest. For example, Home Assistant already knows who is home and if any external doors are open.

## **The Initial Problem**

It is inevitable that some rooms in a house will cool faster than others (e.g., due to poorer insulation, or more external wall area relative to room volume). Meanwhile, some other rooms will heat faster than others, due to bigger radiators, better insulation, changing sunlight or the presence of large appliances like ovens or dryers. In my house, our nursery both cooled faster and heated faster than any other room in the house. The thermostat (a Nest) controlled the boiler from the living area, and would often turn off the boiler while the nursery was still chilly.   

## **Failed Solutions:**

*   _Increase the target temperature on the TRV._ This would only result in the temperature swinging between too hot and too cold, instead of being mostly too cold. 
*   _Move the thermostat_. Moving the thermostat to the nursery would simply have reversed the problem. The boiler would shut off as soon as the nursery reached the target temperature, while larger rooms were still heating.
*   _Install Smart TRVs_. This doesn’t actually address the initial problem at all. Smart TRV can’t heat a room if the boiler has been switched off by a central thermostat.

## **The Home Assistant Solution**

A preliminary step was some basic plumbing maintenance to make sure the radiators were working well. I mapped out how the radiators were connected by following pipes, judging which radiators heated up first, and made some educated guesses. I then [balanced the radiators](https://ukradiators.com/advice-centre/the-simple-guide-to-balancing-radiators/) to ensure that they all received a good flow of heat from the boiler. After figuring all this out, I drew up a schematic, noted the lockshield valve positions on it and posted it inside my boiler cabinet as a favour to future-me.

![](/images/2022/02/radiator-schematic.png)

I then removed the Nest Thermostat, disconnected the Nest Heat Link from the boiler, and two hours later had sold it for a fair price via a local classified ads website. I replaced the Nest Heat Link with a relay switch that I could control from Home Assistant (a spare Fibaro FGS-212 Z-wave relay switch that I had in a drawer). I was able to directly transplant the wiring from the Nest Heat Link into the relay switch. I could now control the boiler from Home Assistant.

![The Fibaro FGS-212 Z-wave relay switch with the wiring formerly used by the Nest Heat Link
](/images/2022/02/fibaro.jpg){: .captioned }

Next came the Home Assistant configuration. I used the **[min/max](https://www.home-assistant.io/integrations/min_max/)** [platform](https://www.home-assistant.io/integrations/min_max/) to pick out the coolest temperature sensor from a list of sensors that were already installed around the house (most of these are primarily motion sensors that also expose a temperature sensor, but some are [WirelessTags](https://wirelesstag.net/) that I had previously installed for monitoring temperatures).

``` yaml
sensor thermostat:
 - platform: min_max
   type: min
   name: coolest_room_temperature
   entity_ids:
     - sensor.bathroom_temperature_calibrated
     - sensor.boxroom_temperature_calibrated
     - sensor.dining_room_temperature_calibrated
     - sensor.hall_temperature_calibrated
     - sensor.kitchen_temperature_calibrated
     - sensor.landing_temperature_calibrated
     - sensor.master_bedroom_temperature_calibrated
     - sensor.stairs_toilet_temperature_calibrated
```

{: .callout }
> These “\_calibrated” sensors are actually template sensors that I had previously created to incorporate a temperature correction. From experimentation I have determined that my Fibaro and Aeotec sensors are highly accurate, but my Philips Hue motion sensors report temperatures 1 - 2 degrees Celsius below the true temperature.

I then used the [Generic Thermostat](https://www.home-assistant.io/integrations/generic_thermostat/) platform to tell Home Assistant to use the boiler relay switch and the temperature sensor to make a new Thermostat entity.  

``` yaml
climate:
 - platform: generic_thermostat
   unique_id: combi_boiler_generic_thermostat
   name: Boiler Thermostat
   heater: switch.combi_boiler_relay_switch
   target_sensor: sensor.coolest_room_temperature
   target_temp: 18
   cold_tolerance: 0.0
   hot_tolerance: 0.0
   precision: 0.5
   min_cycle_duration:
     seconds: 30
   initial_hvac_mode: "heat"
   away_temp: 15
   comfort_temp: 21
   home_temp: 19
   sleep_temp: 17
```

The above code is using the preset functionality introduced in [Home Assistant release 2022.02](https://www.home-assistant.io/blog/2022/02/02/release-20222/), to define various presets, such as *away*, *comfort*, *home*, *sleep* etc.   

I could then add the new thermostat entity to the Home Assistant UI and use it to control my home heating.

![](/images/2022/02/thermostat.png)

I began writing some automations to automatically switch between the “home” and “sleep” presets, but for usability’s sake I instead installed the [Scheduler Component](https://github.com/nielsfaber/scheduler-component) and set up the schedule there (thanks to the helpful tips in [this post](https://community.home-assistant.io/t/simple-thermostat-with-preset-modes-management/338845)).

![](/images/2022/02/scheduler.png)

I supplemented this with some automations to switch the thermostat into “away” mode if everyone has left the house, and to switch back into either “home” or “sleep” mode whenever any returns. I then added some more automations to avoid wasting energy by temporarily switching off the boiler if any external doors are left open for any reason. I’m sure that over time, the list of heating automations will expand.  

The final piece of the puzzle was to spend a few days monitoring the temperatures in the house, adjusting the TRVs in each room to ensure that each room could reach the target temperature but would not overshoot it.  

The end result is very even heating throughout the house, with all rooms within 1&#8451; of each other. The thermostat settings are available on the main wall tablet, and easy for anyone to use. The regular radiator system is balanced and the TRVs are tuned so that each room will heat quickly to the target temperature and stop.  Meanwhile, Home Assistant makes sure that the boiler is on whenever a radiator TRV might want to open up, and that the boiler turns off whenever it is not needed or would be wasteful.

![Thermostat controls in use on a Home Assistant wall panel](/images/2022/02/wall-panel-1.jpg){: .captioned }

## **Limitations**

Although I’m happy with this approach, it has the drawback that if I want to increase the target temperature, I need to first retune all the TRVs to make it possible for that temperature to be reached. Right now, the TRVs allow each room to reach about 20&#8451;. If I increased the thermostat to 21&#8451; (or set the thermostat to the “comfort” preset), the rooms would not reach it due to the TRVs closing the radiators, and the boiler would never be shut off.  

A related drawback is that if turn the thermostat down the house temperature may become uneven. For example, if I change the preset to “sleep”, the target temperature is changed to 17&#8451;. The boiler will kick in for a bit if any room drops below 17&#8451;. During the time the boiler is on, some smaller rooms may heat up to their maximum TRV temperature of 20&#8451;, which is a waste of energy, and might leave those rooms uncomfortably hot.  

## **The Marginal Value of Smart TRVs**

Smart TRVs are cheaply available, such as the ZigBee-controlled [HY386](https://www.alibaba.com/product-detail/HY368-Zigbee-Radiator-Actuator-TRV_1600327750522.html?spm=a2700.wholesale.0.0.7f585cad6h6Slb) (currently €22.28 on AliExpress). I discussed this in [some detail]({% link current/_posts/2022-02-01-automating-the-hy367-hy368-smart-radiator-actuator-in-home-assistant.md %}) in a previous post. I see two main benefits to replacing existing my regular TRVs with these smart TRV:

1.  They can be reconfigured with new target temperatures whenever the thermostat temperature is changed. This fully addresses the limitations discussed above.
2.  They can be explicitly actuated by Home Assistant based on the temperature from a separate sensor in the middle of the room. This might be an improvement on letting them actuate themselves based on the temperature they read from their location at near the bottom of the radiator.

I haven’t decided if these benefits are compelling enough to warrant the installation of eleven new battery-hungry devices around the house.

## **Bonus Achievement: Monitoring Gas Energy**

Unfortunately we do not have smart gas meters in Ireland. However, I realised that I could now make some reliable estimates of real-time gas consumption in Home Assistant. My only gas powered appliance is my boiler, and now that boiler is exclusively controlled by Home Assistant. So long as the radiators are balanced and the TRVs are properly set, then the boiler should only be switched on when heating is required, during which time it should use a steady amount of gas. This conclusion allowed me to create some virtual energy sensors based on boiler run time, and add these into the Home Assistant Energy dashboard.  

![](/images/2022/02/gas-consumption.png)

Gas consumption chart from the Home Assistant Energy Dashboard

To start with, I needed to track how long the boiler was run for.   

{% raw %}
``` yaml
sensor boiler_energy:
 - platform: history_stats
   name: 'Boiler Cumulative Time Today'
   entity_id: switch.combi_boiler_relay_switch
   state: "on"
   type: time
   start: "{{ now().replace(hour=0, minute=0, second=0) }}"
   end: "{{ now() }}"
```
{% endraw %}

I then started taking manual readings from my gas meter, and noting them down in a spreadsheet along with the value of the '_Boiler Cumulative Time Today_' sensor. Soon enough I could tell that I was typically using about 14kWh of gas every hour that the boiler was on.  

I stored this in a new input helper called `input_number.combi_boiler_power_usage`, and then created a new template sensor that evaluates to the boiler’s current power consumption in Watts:  


{% raw %}
``` yaml
template:
 - sensor:
   - name: combi_boiler_current_power_usage
     unique_id: combi_boiler_current_power_usage
     unit_of_measurement: W
     device_class: power
     state_class: measurement
     state: >
       {{ is_state('switch.combi_boiler_relay_switch', 'on') | iif(states('input_number.combi_boiler_power_usage'), 0) }}
```
{% endraw %}

I then added a new sensor using the “integration” platform to integrate (in the calculus sense of the word) the boiler power over time to get total energy:  

``` yaml
sensor:
 - platform: integration
   name: boiler_energy_kwh
   source: sensor.combi_boiler_current_power_usage
   unit_prefix: k
   method: left
```

I could then go to the Energy Dashboard and add this new sensor `sensor.boiler_energy_kwh` as a “_Gas Source_”.  

## **Next Steps**

The virtual energy sensor approach is basically to use some prior knowledge about a device’s energy profile and some current knowledge about its state to work out how much power it is currently using. I realised that I could apply this strategy to a wide range of electrical devices in the house. About 5 minutes later I realised that I wasn’t the first person to think of this, and that Bram Gerritsen had already created the wonderful [Powercalc](https://github.com/bramstroker/homeassistant-powercalc) integration to do just this. In my next post I’ll describe how I used Powercalc to accurately track power for the majority of devices in my house without using any power meters.