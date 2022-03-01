---
author: Sean Blanchfield
comments: true
date: 2022-02-24 13:36:07+00:00
layout: post
link: https://seanblanchfield.com/virtual-energy-meters-with-powercalc/
slug: virtual-energy-meters-with-powercalc
title: Virtual Energy Meters with PowerCalc
image: /images/2022/02/gas-consumption-1.png
tags:
- Code
- Home Automation
---

In my last post I described how I [optimised my home heating]({% link _posts/2022-02-23-automating-heating-with-home-assistant.md %}) with Home Assistant and then created virtual energy sensors to monitor my estimated gas usage from Home Assistant’s Energy Dashboard. In this post I’ll describe how I used the same strategy to monitor the real-time energy use of the majority of devices in my house without using any power meters. A big shout out to the amazing [Powercalc](https://github.com/bramstroker/homeassistant-powercalc) integration for Home Assistant, which makes this a relatively simple process, with extremely powerful results.

<!-- more -->

## **Recap**

My initial goal was to create an virtual energy sensor for my gas boiler, which could be monitored by the energy dashboard:

I first needed to create a virtual power meter:  

{% raw  %}
``` yaml
template:
 - sensor:
   - name: combi_boiler_current_power_usage
     unique_id: combi_boiler_current_power_usage
     unit_of_measurement: W
     device_class: power
     state_class: measurement
     state: >
       {{ is_state('switch.combi_boiler_relay_switch', 'on')  iif(states('input_number.combi_boiler_power_usage'), 0) }}

```
{% endraw  %}

The state of the above sensor will evaluate to zero if the boiler relay switch is off, or to the value of the `input_number.combi_boiler_power_usage` input helper if the boiler is on. Some note on the attributes defined above:

*   `unit_of_measurement: W` is important. According to the docs for the [integration](https://www.home-assistant.io/integrations/integration/) platform, a sensor that measures in units of “W” will be integrated into an energy sensor in units of kWh.
*   `device_class: power` is important. From my testing, this is necessary for the integration platform to produce an output sensor that has the attribute `device_class: energy`, which is necessary for it to work with the Energy Dashboard.
*   `state_class: measurement`. According to the [sensor platform docs](https://developers.home-assistant.io/docs/core/entity/sensor/#available-state-classes) this describes the sensor as measuring a current value (vs a predicted value or an aggregate of some kind), and it is necessary to opt into long-term statistics. I haven’t tested if it is strictly necessary for our purposes, but it seems like good practice.

To turn the power sensor into a virtual energy meter,  I defined an “integration” sensor as follows:

``` yaml
sensor:
 - platform: integration
   name: boiler_energy_kwh
   source: sensor.combi_boiler_current_power_usage
   unit_prefix: k
   method: left
```

I now had a working energy sensor:

![](/images/2022/02/energy-sensor.png)

Note the attributes `device_class: energy` and `state_class: total`, which make this sensor compatible with the Home Assistant’s energy management dashboard. I could now add the sensor to the energy dashboard as follows:

![](/images/2022/02/Configure-gas.png)

This approach can be generalized to create a virtual energy meter for anything you can estimate the current power of. The pattern is a power meter, followed by an energy meter:

``` yaml
template:
- sensor:
  - name: test_virtual_power_sensor
    unit_of_measurement: W
    device_class: power
    state_class: measurement
    state: 10
 
sensor:
- platform: integration
  name: test_virtual_energy_meter
  source: sensor.test_virtual_power_sensor
  unit_prefix: k
  method: left
```

My next mission was to create a new virtual sensor to represent the roughly fixed amount of gas we use heating domestic hot water each day. However, I realised that I could avoid creating all these sensors by hand, and instead use the Powercalc integration to create them for me.   

## **The Powercalc Integration**

Bram Gerritsen’s [Powercalc integration](https://github.com/bramstroker/homeassistant-powercalc) automates the creation of the kind of virtual energy sensors I created above. It is especially powerful when it comes to lights, as it automatically recognises the [device and model of popular smart lights](https://github.com/bramstroker/homeassistant-powercalc/blob/master/docs/supported_models.md) and looks up its current state in a community-contributed lookup table to find a good estimate of its current power usage. In my case, it automatically detected every smart light in the house.  

Powercalc not only makes it easy to estimate your lights, but it allows you to produce virtual energy meters for any device that Home Assistant knows the state of, such as relay switches, robot vacuums, media players, smart speakers, phones, cameras, and anything with an IP address on your network. Any dumb devices that are always on and have stable power usage can also be added in. With a bit of templating you could also represent dumb devices that operate on a predictable schedule.    

The first step was to take stock of all the electrical devices in my house. I made a spreadsheet, and gave each device a category: 

*   *Smart lights*. Powercalc would look after these automatically.
*   *HA-integrated devices*. Current power consumption could be predicted from the current state of these devices.
*   *Always-on*. Power consumption can be predicted because it is always the same.
*   *Dumb devices*. Devices that Powercalc won’t work for.

I came up with 69 devices, only 9 of which Powercalc wouldn’t work for.   

I then worked through each of the HA-integrated devices to identify a sensor in HA that represented the state of that device. I also came up with estimates of power usage of each device by combining internet research with some empirical testing with a power meter, and a little guesswork.  

Here is the final spreadsheet:

<iframe id="pageswitcher-content" frameborder="0" marginheight="0" marginwidth="0" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQcgEZkUH7OBNENvPLtQoxfKLQCeZs6tSh6sumrL9ajUL83w4Z8IIsmXHSKs2bIbin5XHVHIDdKv2Z3/pubhtml/sheet?headers=false&amp;gid=0" style="display: block; width: 100%; height: 100%;"></iframe>

## **Reviewing Device Sensors**

Before proceeding to create a Powercalc configuration, I reviewed the devices in the spreadsheet to make sure each of them had an appropriate Home Assistant sensor to work with. 

I found a few devices that were always on,  but didn’t have any representation in Home Assistant. Powercalc allows you to deal with these using the [fixed\_daily\_energy](https://github.com/bramstroker/homeassistant-powercalc#daily-fixed-energy) directive, but this only produces an energy sensor, and does not produce a power sensor. I wanted to be able to see a real-time estimate of total current power consumption, including these devices.  To work around this, I created template sensors in Home Assistant to represent the always-on state of each of these devices. I needed to create a template sensor for each device, because each `entity_id` configured in Powercalc must be unique.   

``` yaml
template:
  binary_sensor:
  - name: fridge_always_on
    state: on
 
  - name: garden_camera_always_on
    state: on
 
# ...etc
```

For convenience, I added a template sensor to do a better job of giving the current state of the robot vacuum:

{% raw  %}
``` yaml
- name: xiaomi_vacuum_charging_state
 unique_id: xiaomi_vacuum_charging_state
 icon: 'mdi: battery-charging-medium'
 state: >-
   {% if states('vacuum.xiaomi_vacuum_cleaner') == 'docked' %}
     {% if state_attr('vacuum.xiaomi_vacuum_cleaner', 'battery_level')int < 100 %}
       charging
     {% else %}
       docked
     {% endif %}
   {% else %}
   cleaning
   {% endif %}
```
{% endraw %}

I found that although my Synology NAS was integrated with Home Assistant, there wasn’t a binary sensor to tell if it is currently powered on or not. I fixed this with a ping sensor.

``` yaml
binary_sensor:
- platform: ping
  host: 10.0.0.35
  count: 3
  scan_interval: 60
  name: Diskstation
```

I did the same thing for my main workstation, and used the state of the resulting `binary_sensor` to represent the power usage of my computer, monitor, dock and associated equipment.  

## **The Powercalc Config**

The next job was to translate the spreadsheet into a Powercalc config. To make this easier to manage, I split the Powercalc configuration out by adding the following into configuration.yaml:

``` yaml
# Energy tracking
# Powercalc for power/energy estimates
powercalc:
 
sensor powercalc_label: !include powercalc.yaml
```

Here is my final powercalc.yaml file:  

{% raw  %}
``` yaml

- platform: powercalc
  create_group: All Estimated Usage
  entities:

    - create_group: All Lights
      entities:

      - create_group: Upstairs Lights
        entities:
        - entity_id: light.landing_light

        - create_group: Bedroom Lights
          entities:
            - entity_id: light.master_bedroom_light
            - entity_id: light.back_bedroom_light
            - entity_id: light.boxroom_light

        - create_group: Bathroom Spots
          entities:
            - entity_id: light.bathroom_spot_1
            - entity_id: light.bathroom_spot_2
            - entity_id: light.bathroom_spot_3
            - entity_id: light.bathroom_spot_4

      - create_group: Downstairs Lights
        entities:
        - entity_id: light.hall_light
        - entity_id: light.stairs_toilet_light
        - entity_id: light.living_room_light
          manufacturer: innr
          model: RB 285 C

        - entity_id: light.living_room_lamp
        - entity_id: light.dining_room_light
        - entity_id: light.utility_room_light

        - create_group: Kitchen Spots
          entities:
            - entity_id: light.kitchen_spot_1
            - entity_id: light.kitchen_spot_2
            - entity_id: light.kitchen_spot_3
            - entity_id: light.kitchen_spot_4
            - entity_id: light.kitchen_spot_5
            - entity_id: light.kitchen_spot_6

        - create_group: Driveway Lights
          entities:
            - entity_id: light.front_driveway_lamp_left
            - entity_id: light.front_driveway_lamp_right
            - entity_id: light.front_porch_light

        - create_group: Kitchen Cabinets
          entities:
            - entity_id: switch.north_kitchen_cabinet_lights
              # 14W + 4W LED strips.
              # Measured locally as 18W, with 1.1W added by relay switch when under load.
              # standby power represents passive power consumed by relay switch (measured at 0W)
              standby_power: 0.0
              fixed: 
                power: 19.1

            - entity_id: switch.south_kitchen_cabinet_lights
              # 10W + 10W LED strips.
              # Measured locally as 20W, with 1.1W added by relay switch when under load.
              # standby power represents passive power consumed by relay switch (measured at 0W)
              standby_power: 0.0
              fixed: 
                power: 21.1
        
        - entity_id: switch.garden_lights
          # 2X 30W LED bulbs plus relay plug (measured at 1.1W under load)
          # standby power represents passive power consumed by relay switch (measured at 0W).
          standby_power: 0.0
          fixed:
            power: 61.1
        
        - entity_id: switch.attic_lamp
          # 1X 30W LED bulb plus relay plug (measured at 1.1W under load)
          # standby power represents passive power consumed by relay switch (measured at 0W).
          standby_power: 0.0
          fixed:
            power: 31.1
        
    - create_group: Always On Devices
      entities:

      # The following devices are integrated into HA, but are generally always on.
      - entity_id: switch.siren
        name: Siren
        # Locally measured at 0.5W
        standby_power: 0.5
        fixed:
          # See https://help.aeotec.com/support/solutions/articles/6000167689-siren-gen5-technical-specifications-
          power: 0.5
      
      - entity_id: binary_sensor.router
        fixed:
          # Netgear Nighthawk R7000 - measured locally.
          power: 9.0
      
      - entity_id: binary_sensor.diskstation
        fixed:
          # Synology Diskstation DS218, measured locally
          power: 14.9
        
      - entity_id: switch.air_ionizer
        name: Air Ionizer
        fixed:
          # 3.4W according to device label, 3.6W as measured locally. 
          # Attached to relay plug, which adds 1.1W under load.
          power: 4.7
      
      - entity_id: binary_sensor.aarlo_connected_living_room_camera
        name: Living Room Camera
        # Arlo Q
        # Locally measured as 2.4W standby, 2.5W playing
        standby_power: 2.4
        fixed:
          power: 2.5
        
      - entity_id: binary_sensor.aarlo_connected_baby_monitor
        name: Baby monitor
        # Arlo ABC1000 Baby/Pet Monitor
        # Locally measured as 3.1W playing, 3W when off
        standby_power: 3.0
        fixed:
          power: 3.1
      
      # The following entities are using "always on" template sensors that always evaluate to the 'on' state.
      - entity_id: binary_sensor.garden_camera_always_on
        name: Garden Camera
        fixed:
          # See https://services.google.com/fh/files/misc/nestiqoutdoor_productenvironmenteeport.pdf
          # 34kWh / year = 3.88W
          power: 3.88

      - entity_id: binary_sensor.doorbell_always_on
        name: Doorbell
        fixed:
          # See https://services.google.com/fh/files/misc/nestiqoutdoor_productenvironmenteeport.pdf
          power: 3.88

      - entity_id: binary_sensor.nest_protect_always_on
        name: Nest Protect
        fixed:
          # Estimate - can't find data
          power: 0.1
      
      - entity_id: binary_sensor.smoke_detectors_always_on
        name: Smoke Detectors
        fixed:
          # See https://community.element14.com/challenges-projects/design-challenges/energy-harvesting/b/blog/posts/carbon-monoxide-detector-power-consumption
          # 1mA @ 3V = 0.003W
          # X2 (kitchen, hall)
          power: 0.006
      
      - entity_id: binary_sensor.network_switch_always_on
        name: Network Switch
        fixed:
          # See https://eu.dlink.com/pl/pl/-/media/business_products/dgs/dgs-1008p/datasheet/dgs_1008p_d1_datasheet_en_eu.pdf
          # Switch power is just 0.25W, but measured at 4.5W - 5W. It is powering a PoE camera.
          power: 5
      
      - entity_id: binary_sensor.fridge_always_on
        name: Fridge
        fixed:
          # Fridge label states daily consumption of 0.66kwH / day = 27.5W
          power: 27.5

      - entity_id: binary_sensor.modem_always_on
        name: Modem
        fixed:
          # Virgin Media Hub, measured locally
          power: 11.6
      
      - entity_id: binary_sensor.home_assistant_host_always_on
        name: Home Assistant Host
        fixed:
          # Home Assistant Blue, ODroid N2+ (measured locally)
          power: 3.2
      
      - entity_id: binary_sensor.wireless_tag_manager_always_on
        name: Wireless Tag Manager
        fixed:
          # Estimated from max current 0.3A @ 5V.
          power: 1.5
      
      

    - create_group: Variable Consumption Devices
      entities:
      
      - entity_id: switch.combi_boiler_relay_switch
        name: Combi Boiler Electricity
        # See https://www.vokera.co.uk/wp-content/uploads/2013/11/Vision-Combi-25-30C-User-Installation-and-Servicing-manual.pdf
        # Rated as drawing 119W of power while on, presumably to run pump.
        # Standby power represents passive power consumed by relay switch.
        # Relay switch measured as using 1.1W when under load.
        standby_power: 0.0
        fixed:
          power: 120.1
      
      - entity_id: switch.bathroom_extractor_fan
        # Extractor fan rated at 25W but measured locally at 22.1W.
        # standby power represents passive power consumed by relay switch
        standby_power: 0.0
        fixed:
          # Fan power at 22.1W plug relay at 1.1W
          power: 23.2
      
      - create_group: All Speakers
        entities:
          - entity_id: media_player.back_bedroom_assistant
            # Google Nest Mini - Locally measured at 1.5W
            standby_power: 1.5
            fixed:
              states_power:
                playing: 2.5
                idle: 1.5

          - entity_id: media_player.master_bedroom_assistant
            # Google Nest Mini - Locally measured at 1.5W
            standby_power: 1.5
            fixed:
              states_power:
                playing: 2.5
                idle: 1.5

          - entity_id: media_player.hall_assistant
            # Google Nest Mini - Locally measured at 1.5W
            standby_power: 1.5
            fixed:
              states_power:
                playing: 2.5
                idle: 1.5

          - entity_id: media_player.dining_room_speaker
            fixed:
              # Sonos One Gen 2
              # See: https://support.sonos.com/s/article/256?language=en_US
              # See: https://en.community.sonos.com/components-228996/power-consumption-6763681
              # (Locally measured at following values)
              power: 3
              states_power:
                playing: 5

          - entity_id: media_player.master_bedroom_speaker
            fixed:
              # Sonos Play:1
              # See: https://support.sonos.com/s/article/256?language=en_US
              # (Locally measured at following values)
              power: 3.5
              states_power:
                playing: 4.2

      - create_group: TV
        entities:
          - entity_id: media_player.beam
            fixed:
              # Sonos Beam Gen 2 + 2X Sonos Play:1 for LHS/RHS channels
              # See https://support.sonos.com/s/article/256?language=en_US
              # Locally measured Beam @ 4.0W idle, 9W playing
              # 4W + 3.5 + 3.5
              power: 11.0
              states_power:
                # See https://en.community.sonos.com/components-228996/power-consumption-6763681
                # 9W + 4.2W + 4.2W = 17.4
                playing: 17.4

          - entity_id: media_player.shield_android
            name: Television
            # Ratings for Nvidia shield plus Panasonic P42ST30B TV
            # Locally measured:
            #   TV: 11.6W standby, 183W idle (static image), 265W playing video
            #   Nvidia shield: 3.5W standby/off, 5W idle/paused, 7.5W playing.
            standby_power: 19.1
            fixed:
              states_power:
                idle: 188
                paused: 188
                playing: 272.5

      - create_group: Phone Charging
        entities:
          
          - entity_id: binary_sensor.pixel_5_is_charging
            name: Pixel5 Phone
            fixed:
              power: "{{ iif(is_state('binary_sensor.pixel_5_battery_state', 'charging'), 10.5, 0.1) }}"
          
          - entity_id: binary_sensor.p20_pro_is_charging
            name: P20Pro Phone
            # P20 Pro. Locally measured 0W when not plugged in, and 10.5W when charging via "supercharger".
            fixed:
              power: "{{ iif(is_state('sensor.p20_pro_battery_state', 'charging'), 10.5, 0) }}"

      - create_group: Tablet Charging
        entities:

          - entity_id: binary_sensor.samsung_tablet_is_charging
            name: Samsung Tablet
            # See https://www.notebookcheck.net/Review-Samsung-10-1-Galaxy-Tab-2-Tablet-MID.77084.0.html
            # Locally measured at 5.6W interactive, 2.6W standby
            fixed:
              power: "{{ iif(is_state('binary_sensor.samsung_tablet_interactive', 'on'), 5.6, 2.6) }}"

          - entity_id: binary_sensor.wall_panel_is_charging
            name: Wall Panel
            # See https://www.notebookcheck.net/Amazon-Fire-HD-10-2019-Tablet-Review-A-10-inch-tablet-at-a-bargain-price.445713.0.html
            fixed:
              power: "{{ iif(is_state('binary_sensor.wall_panel_interactive', 'on'), 3.74, 0.28) }}"


      - entity_id: sensor.xiaomi_vacuum_charging_state
        name: Robot Vacuum
        fixed:
          states_power:
            # Measured locally at following values:
            charging: 29
            docked: 2.9
            cleaning: 0
      
      - entity_id: binary_sensor.workstation
        name: Workstation
        standby_power: 0
        fixed:
          power: 85

    
    # Boiler hot water estimate (based on 0.7M3 daily usage in summer)
    - name: Domestic Hot Water Energy
      daily_fixed_energy:
        value: 7.9807
```
{% endraw %}
## **The end result**

I created a new dashboard to view real-time power consumption:  

![](/images/2022/02/current-power.png)

I also added the top-level Powercalc’s summary sensor into the energy dashboard, along with pricing info from my electricity tariff, and a couple of Powercalc sub-groups as “individual devices”:

![](/images/2022/02/energy-dashboard.png)

## **Next Steps**

Although I now have detailed power consumption estimates for 60 out of 69 devices in my house, the remaining 9 big dumb appliances are probably the biggest energy hogs. To measure them I need to install some power meters. After some research I have selected the [Shelly EM](https://shelly.cloud/products/shelly-em-smart-home-automation-device/) with two clamps, and will be installing this in my consumer unit / fuse box / breaker box to measure power usage at the main 63A switch using a 120A CT clamp, and power usage on my 32A oven/hob circuit using a 50A CT clamp. I will be supplementing this with a handful of [Shelly Plus 1PM](https://shelly.cloud/shelly-plus-1pm/) and [Shelly 2PM Plus](https://shelly.cloud/shelly-plus-2pm/) relays to measure power at the other large appliances.