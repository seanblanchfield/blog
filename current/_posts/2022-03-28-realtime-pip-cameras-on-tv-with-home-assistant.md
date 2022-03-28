---
author: Sean Blanchfield
date: 2022-03-28 13:00
layout: post
link: https://seanblanchfield.com/realtime-pip-cameras-on-tv-with-home-assistant/
slug: realtime-pip-cameras-on-tv-with-home-assistant
title: Realtime Picture-in-Picture Camera Feeds on your TV with Home Assistant
image: /images/2022/03/tv-camera-pip.jpg
tags:
- Code
- Home Automation
---

Today I am sharing how I've managed to get a RTSP camera feed to display in a picture-in-picture popup on my TV, without interrupting any other viewing that might be going on. This all happens locally, without any cloud services, and should work with any IP camera that provides an RTSP stream. This is achieved using a modest IP camera, an Android TV (in my case an Nvidia Shield set top box), a side-loaded app called Pipup on the Android TV and Home Assistant. 

<!-- more -->

Home Assistant [natively](https://www.home-assistant.io/blog/2022/03/02/release-20223/) allows you to cast a camera onto an Android TV, but when I tried to embrace this feature I found two big drawbacks. First, any content that is already being played will be rudely interrupted. For example, your Netflix show will be replaced by the doorbell feed, and you'll need to navigate back into it again to restart it. Second, video latency can very bad. If your video is from a cloud-based camera, like a Ring or Nest doorbell, you will have the unavoidable delay added by the internet roundtrip, plus the processing delay on the cloud server. In my experience, this can be 5-15 seconds under normal conditions. However, even for local video streams from IP cameras, Home Assistant adds a processing delay. My best understanding is that this processing delay is related to Home Assistant transcoding the IP camera stream into HLS (via the `generic_camera` and `ffmpeg` integrations), so they can be consumed in a web browser. For my purpose (display the door camera when someone presses the doorbell), a delay of even 10 seconds is too long.

Fixing this involved: (1) fixing camera feed performance, (2) making picture-in-picture (PiP) work on android TV, and (3) sending the camera feeds into the new PiP feature.

## Fixing Camera Feed Performance

I did my testing using a &euro;60 Reolink 520A PoE IP camera, which is hardwired into the same network as my workstantion and the Home Assistant host (a Home Assistant Blue, i.e., an Odroid N2+). This camera provides an high-res ("main") and a low-res ("sub") RTSP stream, which I could open directly in VLC. I could open the "sub" RTSP stream in VLC (at a URL like `rtsp://admin:PASSWORD@IP_ADDRESS:554//h264Preview_01_sub`), and enjoy basically no latency at about 25 FPS. However, if I viewed the same camera feed through Home Assistant, there was a delay in the stream of up to 10 seconds, and a lot of stuttering. I see two reasons for the performance problems:
1. Home Assistant is trying to transcode the RTSP stream in real-time. This will add a processing delay, which will also vary depending on system load.
1. Viewing a real-time stream over TCP (i.e., HTTP) is not optimal. Any congestion between the camera, the router, the Home Assistant host and the web browser will lead to dropped traffic, which TCP will then spend seconds trying to recover (instead of forgetting about the old frames, and focussing on the current ones). The optimal solution is to display the original RTSP stream (which is UDP, not TCP) in the web browser. Unfortunately, web browsers to do support viewing raw RTSP streams. This is why Home Assistant is transcoding them in the first place.

After exploring some options, I found a great solution in [WebRTC Card](https://github.com/AlexxIT/WebRTC), which builds on [RTSPtoWebRTC](https://github.com/deepch/RTSPtoWebRTC). My peculiar career in video games industry and the adblock wars has given me lots of experience implementing low level networking, designing real-time protocols and using WebRTC for inventive purposes. WebRTC is a browser technology that is designed for realtime media. Unlike every other protocol that web browsers speak, WebRTC is based on UDP. UDP allows it to be fast instead of reliable, in this case to move on if a video or audio frame gets lost, instead of spending seconds trying to recover it. If you do video calls in your web browser without using fancy plugins, then that video and audio may well be running over WebRTC. 

In constast to Home Assistant's default camera transcoding, *WebRTC Card* uses RTSPtoWebRTC to **proxy** your streams between the RTSP and WebRTC protocols (proxying instead of transcoding). It is basically repackaging the data as-is, without doing any CPU-intensive transcoding of the video payload. This effectively eliminates your Home Assistant's CPU as a bottleneck, resulting in a fantastic reduction in video stream delay. As its name implies, *WebRTC Card* also provides a custom lovelace card that you can use to view the WebRTC video streams.

WebRTC Card can be installed via HACS, and then can you enable it via Home Assistant's "Configuration > Devices & Services > Integrations". 

I had a little difficulty with the latest release available on HACS at the time of this writing (v2.1.1), as described in [issue #280](https://github.com/AlexxIT/WebRTC/issues/280). If the version in HACS at the time you are reading this is v2.2.0 or greater, you may not have any issues. However, to resolve my issue, needed to manually install v2.2.0 by copying the v2.2.0 "webrtc" folder from github [link](https://github.com/AlexxIT/WebRTC/tree/v2.2.0/custom_components/webrtc) into my `custom_components` directory.

I also encountered a strange problem where the custom `webrtc-card` was only intermittently found by the lovelace UI. To resolve this I manually added the relevant JS module in my Lovelace resources. You can do this from "Configuration > Dashboards > Resources", or if you use Lovelace in YAML mode, by adding something like the following:

``` yaml
lovelace:
  # ...
  resources:
    # ...
    - url: /webrtc/webrtc-camera.js?v2.2.0
    type: module
```

I could then add WebRTC cards to my UI by adding a "manual" card like this (where "PASSWORD" is obviously redacted AND "CAMERA IP" represents the local camera IP address):

``` yaml
type: 'custom:webrtc-camera'
url: 'rtsp://admin:PASSWORD@CAMERA_IP:554//h264Preview_01_sub'
```

It is also possible to avoid embedding the literal RTSP stream in the card yaml. A more elegant approach is to create a [generic_camera](https://www.home-assistant.io/integrations/generic/) entity, and then to reference that. I use a split configuration, so I added the following to my `configuration.yaml` where ("IP_CAMERAS" is a label so that this doesn't interfere with other top-level "camera:" definitions):
``` yaml
camera IP_CAMERA: !include ip_cameras.yaml
```
Then I created `ip_cameras.yaml` to define various IP cameras and their RTSP streams:
``` yaml
- platform: generic
  name: Front Driveway RTSP
  stream_source: rtsp://admin:PASSWORD@CAMERA_IP:554//h264Preview_01_sub
  # Following line not necessary, but added Reolink snapshot URL for completeness:
  still_image_url: http://CAMERA_IP/cgi-bin/api.cgi?cmd=Snap&channel=0&user=admin&password=PASSWORD 
```

Now, the WebRTC cards can be changed to reference the camera entity (from which it will extract the RTSP stream):

``` yaml
type: 'custom:webrtc-camera'
entity: camera.front_driveway
background: true # Keeps stream active even when not displayed, to speed up loading.
```

At this point, WebRTC streams were working inside my network, but I couldn't access them outside my house. This is because they run over UDP, and my router was simply rejecting all these unexpected inbound UDP packets. To make that work, I needed to set up some port forwarding at my router. As recommended by in the [documentation](https://github.com/AlexxIT/WebRTC#webrtc-external-access) I forwarded UDP traffic on 10 ports (50000-50010) from my WAN address to my Home Assistant host's LAN address. I then navigated to the integration's config options ("Configuration > Devices & Services > Integrations > WebRTC Camera") and specified the same port range. I could then view the WebRTC video streams from outside my network.

{: .callout }
> I run the excellent [Nginx Proxy Manager](https://github.com/hassio-addons/addon-nginx-proxy-manager) addon so that I can securely access my Home Assistant when I am away from the house, without proxying through any remote internet servers. I had previously run an Nginx reverse proxy on a VPS server, but this added unacceptable latency, an extra point of failure, and unnecessary bandwidth cost when trying to stream live video remotely. Now when I access a video stream remotely, the traffic consists of UDP packets traveling from my phone to my home router, with no additional bandwidth costs. In constrast to the popular alternative of port forwarding directly to [Home Assistant Core configured with DuckDNS/LetsEncrypt](https://www.home-assistant.io/blog/2017/09/27/effortless-encryption-with-lets-encrypt-and-duckdns/) (which disables unencrypted HTTP, and thereby disables direct local LAN access), the Nginx Proxy Manager approach allows you to use both TLS to your public domain name for remote access and regular HTTP to a local LAN connectivity (so you can still use Home Assistant if your internet goes down). I recommend it!

The performance difference between the new WebRTC streams and the standard HLS streams was considerable. Viewing them side-by-side from my workstation on my LAN, I could see a significant difference in quality and in timeliness.

![WebRTC vs HLS video stream comparison - 9 second difference](/images/2022/03/WebRTC-camera-comparison.png){:.captioned }

The bottom camera is the WebRTC stream, which has a delay of about 1 second, with a fluid framerate. The top stream is the HLS version, which stutters badly, and is captured here 9 seconds late, relative to the WebRTC stream. The difference is significant enough that the person visible in the WebRTC stream was never captured in the HLS stream.


## Picture-in-Picture on Android TV

Android TV doesn't provide a native API to allow the display of picture-in-picture popups. However, you can use the [PiPup](https://github.com/rogro82/PiPup) on your Android TV to display the popups for you. PiPup provides a REST API, which you can communicate with from Home Assistant. 

The original PiPup repository hasn't been updated in a few years, and has some important outstanding pull requests. Therefore, we cannot install it in the recommended way. We need madjam002's [pull request](https://github.com/rogro82/PiPup/pull/34) (also discussed in this [issue](https://github.com/rogro82/PiPup/issues/8)), which adds support for displaying embedded web content with javascript. That pull request contains a link to an [APK build of PiPup](https://github.com/rogro82/PiPup/pull/34#issuecomment-933015085) with the relevant improvements. Download that APK (*app-debug.apk*).

Make sure you have enabled developer options on your Android TV, and find out what the IP address of your Android TV is. Instructions are given on Stackoverflow [here](https://stackoverflow.com/questions/31421872/adb-connection-to-an-androidtv#:~:text=You%20need%20to%20use%20ADB,are%20now%20a%20developer%22%20appears.).

The following commands assume you have ADB installed on your workstation. 

``` bash
adb connect YOUR_ANDROID_TV_IP_ADDRESS
adb install app-debug.apk

# Confirm installation with
adb shell pm list packages | grep pip
# Note that the apk identifies itself as "nl.begner.pipup"
# Given permissions for it to draw a system alert window (required on Nvidia Shield at least)
adb shell appops set nl.begner.pipup SYSTEM_ALERT_WINDOW allow

```

You can now confirm that it is working by using cURL to post a command to the app's REST API. Put the example payload (copied from the original docs) into a file `post.json`:
``` json
{
    "duration": 30,
    "position": 0,
    "title": "Your awesome title",
    "titleColor": "#0066cc",
    "titleSize": 20,
    "message": "What ever you want to say... do it here...",
    "messageColor": "#000000",
    "messageSize": 14,
    "backgroundColor": "#ffffff",
    "media": { 
        "image": {
            "uri": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/cfcc3137009463.5731d08bd66a1.png", 
            "width": 480
        }
    }
}
```
Now POST it to your TV, and you should see a popup (replace `ANDROID_TV_IP_ADDRESS`).
``` bash
curl -d "@post.json" -H "Content-Type: application/json" -X POST http://ANDROID_TV_IP_ADDRESS:7979/notify
```

## Displaying PiP Camera Feeds 

We use the [RESTful command integration](https://www.home-assistant.io/integrations/rest_command/) to interact with PiPup from Home Assistant. I use a split YAML configuration, so I enabled it by adding the following to `configuration.yaml`:
``` yaml
rest_command: !include rest_commands.yaml
```
I then created `rest_commands.yaml` and added the following two commands to it (replace `ANDROID_TV_IP_ADDRESS` as appropriate):


{% raw  %}
``` yaml
pipup_image_on_tv:
  # Use Pipup to display notifications on Android TV devices.
  url: http://ANDROID_TV_IP_ADDRESS:7979/notify
  content_type: 'application/json'
  verify_ssl: false
  method: 'post'
  timeout: 20
  payload: >
    {
      "duration": {{ duration | default(20) }},
      "position": {{ position | default(0) }},
      "title": "{{ title | default('') }}",
      "titleColor": "{{ titleColor | default('#50BFF2') }}",
      "titleSize": {{ titleSize | default(10) }},
      "message": "{{ message }}",
      "messageColor": "{{ messageColor | default('#fbf5f5') }}",
      "messageSize": {{ messageSize | default(14) }},
      "backgroundColor": "{{ backgroundColor | default('#0f0e0e') }}",
      "media": { 
        "image": {
          "uri": "{{ url }}",
          "width": {{ width | default(640) }},
          "height": {{ height | default(480) }}
        }
      }
    }


pipup_url_on_tv:
  # Use with Webrtc camera as described here:
  # https://github.com/AlexxIT/WebRTC/wiki/Cast-or-share-camera-stream#html-page
  url: http://ANDROID_TV_IP_ADDRESS:7979/notify
  content_type: 'application/json'
  verify_ssl: false
  method: 'post'
  timeout: 20
  payload: >
    {
      "duration": {{ duration | default(20) }},
      "position": {{ position | default(0) }},
      "title": "{{ title | default('') }}",
      "titleColor": "{{ titleColor | default('#50BFF2') }}",
      "titleSize": {{ titleSize | default(10) }},
      "message": "{{ message }}",
      "messageColor": "{{ messageColor | default('#fbf5f5') }}",
      "messageSize": {{ messageSize | default(14) }},
      "backgroundColor": "{{ backgroundColor | default('#0f0e0e') }}",
      "media": { 
        "web": {
          "uri": "{{ url }}", 
          "width": {{ width | default(640) }},
          "height": {{ height | default(480) }}
        }
      }
    }
```

{% endraw  %}

After a restart, we have two new services available: `rest_command.pipup_image_on_tv` and `rest_command.pipup_url_on_tv`. We can pass these parameters as follows (e.g., from the Developer Tools):
``` yaml
service: rest_command.pipup_image_on_tv
data:
  title: hey
  message: I can see you
  titleColor: red
  position: 0
  url: https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/cfcc3137009463.5731d08bd66a1.png
```

The above values can be templated. For example, the URL of a camera snapshot is contained in the `entity_picture` attribute of your camera entities (including with a short-lived auth token). To display a camera snapshot, you could call the service as follows (e.g., from an automation) (replacing `PUBLIC_ROOT_URL` with whatever your public Home Assistant URL is, e.g., "https://example.duckdns.org:8123/" or perhaps your NabuCasa address):


{% raw  %}
``` yaml
service: rest_command.pipup_image_on_tv
data:
  title: Doorbell
  message: "There's somebody at the door"
  url: PUBLIC_ROOT_URL{{ state_attr('camera.driveway_doorbell', 'entity_picture') }}"
```
{% endraw %}

Displaying an image is nearly instant, but if you can tolerate 1-2 seconds for a video stream to initialize, you can also show the live video stream using WebRTC Card. To do this, we use the `webrtc.create_link` service (documented [here](https://github.com/AlexxIT/WebRTC/wiki/Cast-or-share-camera-stream)) to generate a temporary video stream webpage at a nominated URL. We then send the URL of that page to the PiPup service. To put this together, we need to create a Home Assistant script, which gives us the ability to generate a random URL and store it in a variable, which we can then pass into `webrtc.create_link` and then into `rest_command_pipup_url_on_tv`.

Here is the yaml of a working script, which you can add to your `scripts.yaml` or define using the UI at "Configuration > Automations & Scenes > Scripts"  (remember to replace `PUBLIC_ROOT_URL`):

{% raw  %}
``` yaml
display_driveway_pip_popup_on_tv:
  alias: Display Driveway PIP Popup on TV
  mode: single
  variables:
    link_id: '{% for _ in range(40) %}{{ range(10)|random }}{% endfor %}'
  sequence:
  - service: webrtc.create_link
    data:
      link_id: '{{ link_id }}'
      entity: camera.front_driveway
      open_limit: 1
      time_to_live: 60
  - service: rest_command.pipup_url_on_tv
    data:
      title: Door
      message: Someone is at the front door
      width: 640
      height: 480
      url: PUBLIC_ROOT_URL/webrtc/embed?url={{ link_id }}&webrtc=false

```
{% endraw  %}

Now, whenever you want to pop the camera feed up on your TV, just call `script.display_driveway_pip_popup_on_tv`. Voilà!

![Pop up over Netflix](/images/2022/03/tv-camera-pip.jpg)
The above image is still showing a feed from my driveway camera instead of my doorbell camera. The next step is to get rid of my Nest Camera and replace is with something better. I'll cover that in my next post.

