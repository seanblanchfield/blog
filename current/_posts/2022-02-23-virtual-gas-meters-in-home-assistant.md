---
author: Sean Blanchfield
comments: true
date: 2022-02-23 22:58:15+00:00
layout: post
link: https://seanblanchfield.com/virtual-gas-meters-home-assistant/
slug: virtual-gas-meters-home-assistant
title: Virtual Gas Meters in Home Assistant
image: /images/2022/02/gas-consumption.png
tags:
- Code
- Home Automation
---


Unfortunately, we do not have smart gas meters in Ireland. However, I realised that I could use Home Assistant to create virtual gas meters, which provide a good real-time estimate of gas usage. 

The only appliance that uses gas in our house is our combi-boiler, which has the job of heating the radiators for central heating, and heating domestic hot water. In my [previous post](/2022/02/automating-heating-with-home-assistant) I discussed how I took direct control of my central heating by replacing Nest with a z-wave relay controlled by Home Assistant. This meant that Home Assistant now knew exactly when the boiler was burning gas. So long as the radiators are balanced and the TRVs are properly set, then the boiler should only be switched on when heating is required, during which time it should use a steady amount of gas. This conclusion allowed me to create some virtual energy sensors based on boiler run time, and add these into 
the Home Assistant Energy dashboard.  

![](/images/2022/02/gas-consumption.png)

Gas consumption chart from the Home Assistant Energy Dashboard

## Tracking Central Heating Gas Usage

To start with, I needed to study gas consumption vs boiler activity.   

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

I then started taking manual readings from my gas meter, and noting them down in a spreadsheet along with the value of the '_Boiler Cumulative Time Today_' sensor. The meter readings were in cubic meters, which I could convert to kWh by multiplying by the "conversion factor" given on my gas utility bills. My current conversion factor is 11.401kWh / cubic meter, but this can vary depending on the source of the gas supply.  My comparing the meter readings to the number of hours the boiler ran between each reading, I could estimate that I was typically using about 14kWh of gas every hour that the boiler was on.  
![Recorded number of hours the boiler ran each day, as the Spring weather improved)](/images/2022/02/cumulative_boiler_run_time.png){: .captioned }

I stored my estimate of 14000 Wh/hour in a new input helper called `input_number.combi_boiler_power_usage`, and then created a new template sensor that evaluates to the boiler’s current power consumption in Watts:  


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


The state of the above sensor will evaluate to zero if the boiler relay switch is off, or to the value of the `input_number.combi_boiler_power_usage` input helper if the boiler is on. Some note on the attributes defined above:

*   `unit_of_measurement: W` is important. According to the docs for the [integration](https://www.home-assistant.io/integrations/integration/) platform, a sensor that measures in units of “W” will be integrated into an energy sensor in units of kWh.
*   `device_class: power` is important. From my testing, this is necessary for the integration platform to produce an output sensor that has the attribute `device_class: energy`, which is necessary for it to work with the Energy Dashboard.
*   `state_class: measurement`. According to the [sensor platform docs](https://developers.home-assistant.io/docs/core/entity/sensor/#available-state-classes) this describes the sensor as measuring a current value (vs a predicted value or an aggregate of some kind), and it is necessary to opt into long-term statistics. I haven’t tested if it is strictly necessary for our purposes, but it seems like good practice.


I then added a new sensor using the [integration](https://www.home-assistant.io/integrations/integration/) platform (i.e., the Home Assistant integration called "integration", in the calculus sense of the word) to integrate (as in sum up) the boiler power over time to get total energy. I originally implemented this in yaml, but these days you can achieve the same thing by adding an Integration helper.

![Turning the power sensor into an energy sensor using an Integration helper](/images/2022/02/integration-helper.png){: .captioned .left-half }

Here is the original yaml code that achieved the same thing:

``` yaml
sensor:
 - platform: integration
   name: boiler_energy_kwh
   source: sensor.combi_boiler_current_power_usage
   unit_prefix: k
   method: left
```

I could then go to the Energy Dashboard and add this new sensor `sensor.boiler_energy_kwh` as a “_Gas Source_”.  

## Tracking Domestic Hot Water Gas Usage

My combi boiler also heats hot water for the shower and wash basins in the house. It is supplied with pumped tank water for this. Whenever a hot water tap / faucet opens, the pump starts and the boiler heats the water on the fly. The pump is only feeds the boiler, and nothing else. I could therefore apply a similar strategy to track gas used to heat hot water. All I needed to do was figure out when the pump was running, and what the average gas used was per second.

I installed a [Shelly 1PM](https://www.shelly.cloud/en-ie/products/product-overview/shelly-plus-1-pm-2-pack/shelly-plus-1-pm) to track the pump activity. Whenever the pump is consuming energy, I know that the boiler is heating hot water.

To calculate gas energy used for domestic hot water heating, I studied gas usage during a period during the Summer, when central heating was completely turned off. I noted that during a period of about 80 days, the pump ran for 33.549 hours and that 40.78 cubic meters (464.995 kWh) of gas was used (according to manual readings taken from the physical gas meter). This means that my boiler has a gas power consumption of 13.86kW for domestic hot water heating.

I then used a similar strategy as outlined above for central heating to get this represented in Home Assistant. 

## If you made it this far...
  
A *virtual energy sensor strategy* exists, which allows you to use some prior knowledge about a device energy consumption and some current knowledge about device state to work out how much power the device is currently using. You can go wild and apply this strategy to most of the electrical devices in your house, and get a very detailed real-time and actionable picture of your energy consumption.

Bram Gerritsen has created the wonderful [Powercalc](https://github.com/bramstroker/homeassistant-powercalc) integration to do just this. In [my next post](/2022/02/virtual-energy-meters-with-powercalc) I describe how I used Powercalc to accurately track power for the majority of devices in my house without using any power meters.