---
author: Sean Blanchfield
date: 2024-07-07 10:00:00
layout: post
link: https://seanblanchfield.com/restore-corrupted-ha-database
slug: restore-corrupted-ha-database
title: How to restore a corrupted Home Assistant sqlite3 database
image: /images/2024/07/bad_db.jpeg
---

An ungraceful restart of my Home Assistant host left me with a corrupted sqlite3 database. 
This is the database where Home Assistant core stores the history of all entity state. I could have deleted the old database and started over, but a better solution is to fix it. Here's how I fixed it by SSHing into Home Assistant.

<!-- more -->

Prerequisites:
- You are able to SSH into Home Assistant, e.g., using the [SSH &amp; Web Terminal](https://github.com/hassio-addons/addon-ssh) Addon.
- You have enough free space on your Home Assistant box to temporarily hold the repaired copy of the database. 

## Steps

Log into the Home Assistant host via SSH, and change to the `/config` directory.

Check how much free space you have.
``` bash
df -h /
```
Check the size of your corrupted database is smaller than the free space:
```bash
ls -lh home-assistant_v2.db
```
Stop Home Assistant core, so it's not writing to the database while we're operating on it.
```bash
ha core stop
```
(this might take a minute)

Run the *sqlite3* [.recover](https://www.sqlite.org/recovery.html) command to produce SQL statements to reconstruct the database, and pipe them into a new SQL database:
```bash
sqlite3 home-assistant_v2.db ".recover" | sqlite3 home-assistant_v2.db.fixed
```
This might produce some output corresponding to problems it found in the corrupted database.


Depending on the size of your database, recovery might take a long time. You can check progress by comparing the size of the recovered database with the original. From a new SSH session, run:

```bash
watch ls -lh home-assistant_v2.db home-assistant_v2.db.fixed
```

When it's done, backup the old corrupted database and put the restored one in its place:
```bash
mv  home-assistant_v2.db home-assistant_v2.db.`date -I`.corrupted
mv home-assistant_v2.db.fixed home-assistant_v2.db
```

Start Home Assistant core again
``` bash
ha core start
```

Log into Home Assistant and check everything is okay, e.g., by looking at the system logs and checking that the history of some entities is intact. 

If everything is looking good, you can delete the old corrupted database:
```bash
rm home-assistant_v2.db.*.corrupted
```
