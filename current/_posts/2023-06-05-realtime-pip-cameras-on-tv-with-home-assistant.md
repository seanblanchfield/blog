---
author: Sean Blanchfield
date: 2023-06-05 13:00
layout: post
link: https://seanblanchfield.com/realtime-pip-cameras-on-tv-with-home-assistant-v2/
slug: realtime-pip-cameras-on-tv-with-home-assistant-v2
title: Real-Time Picture-in-Picture Camera Feeds on your TV with Home Assistant
image: /images/2022/03/tv-camera-pip.jpg
tags:
- Code
- Home Automation
---

I've found a way to get a RTSP camera feed to display in a picture-in-picture popup on my TV, without interrupting any other viewing that might be going on. This all happens locally, without any cloud services, and should work with any IP camera that provides an RTSP stream. This is achieved using a modest IP camera, an Android TV (in my case an Nvidia Shield set top box), a side-loaded app called Pipup on the Android TV and Home Assistant. Read on to find out how.

<!-- more -->

{: .callout }
> This is an updated version of a guide I wrote in March 2022, which was based upon the *WebRTC Camera* home assistant integration. Its author, [@AlexxIT](https://github.com/AlexxIT) has since launched *go2rtc*, which replaces it and is a significant improvement. I have updated this guide accordingly.


Home Assistant [natively](https://www.home-assistant.io/blog/2022/03/02/release-20223/) allows you to cast a camera feed to an Android TV, but when I tried to embrace this feature I found two big drawbacks. First, any content that is already being played will be rudely interrupted. For example, your Netflix show will be replaced by the doorbell feed, and you'll need to navigate back into it again to restart it. Second, video latency can very bad. If your video is from a cloud-based camera, like a Ring or Nest doorbell, you will have the unavoidable delay added by the internet roundtrip, plus the processing delay on the cloud server. In my experience, this can be shocking 5-15 seconds under normal conditions. However, even for local video streams from IP cameras, Home Assistant adds a processing delay. My best understanding is that this processing delay is related to Home Assistant transcoding the IP camera stream into HLS (via the `generic_camera`, `stream` and `ffmpeg` integrations), so they can be consumed in a web browser. A stream delay of 10+ seconds is a problem for all of us who want our door camera to usefully display when someone presses the doorbell. In my limited testing, the normal result is that I get to watch an action replay of my awkward pandemic-era tipping interaction with the delivery guy as soon as I plop myself back in the couch. No one wants that.

Fixing this involved: (1) fixing camera feed performance, (2) making picture-in-picture (PiP) work on android TV, and (3) sending the camera feeds into the new PiP feature.

## Fixing Camera Feed Performance

I did my testing using a &euro;60 Reolink 520A PoE IP camera, which is hardwired into the same gigabit network as my workstation and the Home Assistant host (a Home Assistant Blue, i.e., an Odroid N2+). This camera provides an high-res ("main") and a low-res ("sub") RTSP stream, which I could open directly in VLC. I could open the "sub" RTSP stream in VLC (at a URL like `rtsp://admin:PASSWORD@IP_ADDRESS:554//h264Preview_01_sub`), and enjoy less than 1 second latency at about 25 FPS. However, if I viewed the same camera feed through Home Assistant, there was a delay in the stream of up to 10 seconds, and a lot of stuttering. I see two reasons for the performance problems:
1. Home Assistant is trying to transcode the RTSP stream in real-time. This will add a processing delay, which will also vary depending on system load.
1. Viewing a real-time stream over TCP (i.e., HTTP) is not optimal. Any congestion between the Home Assistant host, the router and the web browser will lead to dropped packets, which will cause TCP to pause the stream while it spends seconds trying to confirm retransmission (instead of forgetting about the past, and focussing on the present). The optimal solution is to display the original RTSP stream (which is UDP, not TCP) in the web browser. Unfortunately, web browsers do not support viewing raw RTSP streams. This is why Home Assistant is transcoding them in the first place.

In the original version of this guide, I discussed using [WebRTC Camera](https://github.com/AlexxIT/WebRTC) (built on top of [RTSPtoWebRTC](https://github.com/deepch/RTSPtoWebRTC)) to solve this problem. This has now been superceded by [go2rtc](https://github.com/AlexxIT/go2rtc), which was created by the same author, and is a lot more capable. *go2rtc*  connects to all your cameras on one side, and proxies them via multiple protocols (with optional format transcoding) to the rest of your network. In our use-case, it connects to camera RTSP streams, and repackages them into the WebRTC protocol, which web browsers can understand.  

My career in the video games industry and my adventures in the adblock wars have given me lots of experience implementing low level networking, designing real-time protocols and using WebRTC for inventive purposes, so thankfully I understand the fundamentals of this already. WebRTC is a browser technology that is designed for realtime media. Unlike every other protocol that web browsers speak, WebRTC is based on UDP. UDP is fast instead of reliable. In this case, UDP allows the stream to move on when a video or audio frame gets lost, instead of stalling the stream and spending seconds trying to recover the old data. If you do video calls in your web browser without using fancy plugins, then that video and audio may well be running over WebRTC. 

{: .callout }
> Trouble viewing RTSP streams in VLC on Ubuntu/Debian? [Debian disabled RTSP support](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=982299) in their build of VLC. To open RTSP streams in VLC, you need to build your own version or install from the Snap store instead.

Whereas Home Assistant's default video transcoding is pretty CPU-intensive, *go2rtc* (under normal usage) simply repackages data as-is from RTSP UDP packets into WebRTC UDP packets, without doing any transcoding of the video payload. This effectively eliminates your Home Assistant's CPU as a bottleneck, resulting in a fantastic reduction in video stream delay. To view these streams in Home Assistant, you use the [WebRTC Camera](https://github.com/AlexxIT/WebRTC) integration, which provides a WebRTC javascript client that can connect to the *go2rtc* server.  If you are also using [Frigate](https://frigate.video/) as your NVR, then you are probably more than halfway there already - Frigate v12 includes *go2rtc* as a core component, and [Frigate HASS Card](https://github.com/dermotduffy/frigate-hass-card) has native support for it.

To proceed, you need to have *go2rtc* running somewhere, e.g.:
* As part of Frigate (this is what I do)
* As a stand-alone Docker container
* As a Home Assistant add-on (which is a docker container managed by Home Assistant)

In addition, you need to install the [WebRTC Camera](https://github.com/AlexxIT/WebRTC) integration via HACS, which allows us to test everything, as well as request short-lived URLs that contain live video streams to display on the TV.

Cameras must be configured in your *go2rtc* config file (or in your Frigate config file). I have both the *main* stream and *sub* stream configured for every camera, which has the following benefits:
- It centralizes configuration for all cameras in one place
- It standardizes all camera URLs used in Home Assistant and elsewhere, even though the cameras are from different manufacturers.
- It eliminates usernames and passwords from the camera URLs used in Home Assistant and elsewhere.
- It relieves cameras of the CPU load involved in serving multiple clients. Every camera now has exactly one client.

Cameras configured in *go2rtc* can be tested using its config page (available on port 1984) and by connecting directly to the proxied RTSP streams in VLC. 

> ![Generic Camera config for a go2rtc proxied stream](/images/2023/06/go2rtc_generic_camera_config.png){: .captioned .right-half}

When I confirmed everything in go2rtc was working correctly, I proceeded to create a Home Assistant [generic_camera](https://www.home-assistant.io/integrations/generic/) for each of them. Note that *go2rtc* version 1.5 provides a live still image for each camera on a standard URL (if using Frigate, [the docs explain](https://docs.frigate.video/configuration/advanced/#custom-go2rtc-version) how to upgrade the *go2rtc* version). This allows each generic camera to be configured with the URL of the RTSP stream hosted by *go2rtc* and a still image transcoded by *go2rtc*. 

WebRTC camera UI cards could then be defined to reference the generic camera entity (from which it will extract the RTSP stream):

``` yaml
type: 'custom:webrtc-camera'
entity: camera.driveway_sub
```

At this point, WebRTC streams were working inside my network, but I couldn't access them when away from my house. To fix this, I needed to set up some port forwarding at my router and to tell *go2rtc* what my public IP address was. This would allow the WebRTC client in the mobile web browser to attempt to connect to my router's public IP, and for those UDP packets to get forwarded to the *go2rtc* server.  

First, I forwarded port **8555** from my router back to the LAN IP address that the *go2rtc* server was running on. This is the port that [*go2rtc* uses for WebRTC communication](https://github.com/AlexxIT/go2rtc#configuration). I then specified the public IP and port in the *go2rtc* configuration file:
``` yaml
webrtc:
  candidates:
    - <PUBLIC IP ADDRESS>:8555
``` 

After this, it was possible to view the camera streams remotely over WebRTC.

The performance difference between the new WebRTC streams and the standard HLS streams was considerable. Viewing them side-by-side from my workstation on my LAN, I could see a significant difference in quality and in timeliness.

![WebRTC vs HLS video stream comparison - 9 second difference](/images/2022/03/WebRTC-camera-comparison.png){:.captioned }

The bottom camera is the WebRTC stream, which has a delay of about 1 second, with a fluid framerate. The top stream is the HLS version, which stutters badly, and is captured here 9 seconds late, relative to the WebRTC stream. The difference is significant enough that the person visible in the WebRTC stream was never captured in the HLS stream.


## Picture-in-Picture on Android TV

Android TV doesn't provide a native API to allow the display of picture-in-picture popups. However, you can use the [PiPup](https://github.com/rogro82/PiPup) app on your Android TV to display the popups for you. PiPup provides a REST API, which you can communicate with from Home Assistant. 

The original PiPup repository hasn't been updated in a few years, and has some important outstanding pull requests. Therefore, we cannot install it in the recommended way. We need madjam002's [pull request](https://github.com/rogro82/PiPup/pull/34) (also discussed in this [issue](https://github.com/rogro82/PiPup/issues/8)), which adds support for displaying embedded web content with javascript. That pull request contains a link to an [APK build of PiPup](https://github.com/rogro82/PiPup/pull/34#issuecomment-933015085) with the relevant improvements. Download that APK ("*app-debug.apk*").

Make sure you have enabled developer options on your Android TV, and know what its IP address is (instructions are given on Stackoverflow [here](https://stackoverflow.com/questions/31421872/adb-connection-to-an-androidtv#:~:text=You%20need%20to%20use%20ADB,are%20now%20a%20developer%22%20appears.)).

The following commands assume you have ADB installed on your workstation, and that you are running Linux or MacOS. If you are running Windows,  `grep` and/or `curl` might be missing or work differently for you (you can instead use equivalent Windows commands, or install Windows versions of the `grep` and `curl` commands from something like *GnuWin32*, or skip testing the installation with the `grep` and `curl` bits below). 

``` bash
adb connect YOUR_ANDROID_TV_IP_ADDRESS
adb install app-debug.apk

# Confirm installation
adb shell pm list packages | grep pip
# Note that the apk identifies itself as "nl.rogro82.pipup"
# Grant permissions for it to draw a system alert window (required on Nvidia Shield at least)
adb shell appops set nl.rogro82.pipup SYSTEM_ALERT_WINDOW allow

```

You can now confirm that it is working by using cURL to post a command to the app's REST API. Put this example payload (copied from the original docs) into a file `post.json`:
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

Use the [RESTful command integration](https://www.home-assistant.io/integrations/rest_command/) to interact with PiPup from Home Assistant. I use a split YAML configuration, so I enabled it by adding the following to `configuration.yaml`:
``` yaml
rest_command: !include rest_commands.yaml
```
I then created `rest_commands.yaml` and added the following two commands to it (replace `ANDROID_TV_IP_ADDRESS` as appropriate):


{% raw  %}
``` yaml
pipup_image_on_tv:
  # Use Pipup to display image notifications on Android TV devices.
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
          "width": {{ width | default(640) }}
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

After a restart, we have two new services available: `rest_command.pipup_image_on_tv` and `rest_command.pipup_url_on_tv`. We can pass parameters to these services as follows (you can try this out "Developer Tools > Services"):
``` yaml
service: rest_command.pipup_image_on_tv
data:
  title: hey
  message: I can see you
  titleColor: red
  position: 0
  url: https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/cfcc3137009463.5731d08bd66a1.png
```


The above values can be templated. For example, camera entities in Home Assistant typically have a `entity_picture` attribute that contains a URL to a current camera snapshot (including a short-lived auth token). To display a camera snapshot, you could call the service as follows from an automation (replace `<PUBLIC_ROOT_URL>` with the literal value of your public Home Assistant root URL, e.g., "https://example.duckdns.org:8123/"):


{% raw  %}
``` yaml
service: rest_command.pipup_image_on_tv
data:
  title: Doorbell
  message: "There's somebody at the door"
  url: <PUBLIC_ROOT_URL>{{ state_attr('camera.driveway_doorbell', 'entity_picture') }}"
```
{% endraw %}

Displaying an image in this way is nearly instantaneous, but if you can tolerate 1-2 seconds for a video stream to initialize, you can also show the live video stream using WebRTC. To do this, we use the `webrtc.create_link` service (documented [here](https://github.com/AlexxIT/WebRTC/wiki/Cast-or-share-camera-stream)) to generate a temporary video stream webpage at a nominated URL. We then send the URL of that page to the PiPup service. To put this together, we need to create a Home Assistant script, which gives us the ability to store a random ID in a variable, which we can then pass into the `webrtc.create_link` service and then into the `rest_command_pipup_url_on_tv` service.

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
      entity: camera.driveway_sub
      open_limit: 1
      time_to_live: 60
  - service: rest_command.pipup_url_on_tv
    data:
      title: Door
      message: Someone is at the front door
      width: 640
      height: 480
      url: PUBLIC_ROOT_URL/webrtc/embed?url={{ link_id }}

```
{% endraw  %}

Now, whenever you want to pop the camera feed up on your TV, just call `script.display_driveway_pip_popup_on_tv`. Voilà!

![Pop up over Netflix](/images/2022/03/tv-camera-pip.jpg)
The above image is still showing a feed from my driveway camera instead of my doorbell camera. The next step is to get rid of my Nest Camera and replace is with something better. I'll cover that in my next post.

