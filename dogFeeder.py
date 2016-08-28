#!/usr/bin/python

import os
import sys
from grblCall import feed
import paho.mqtt.subscribe as subscribe
import time

time.sleep(15)
topics = ["dogFeederFeed", "dogFeederCups1", "dogFeederCups2"] #topics from openhab dogFeeder.rules
dogFeederCups1 = 1
dogFeederCups2 = 1

print("subscribing")
while 1:
    m = subscribe.simple(topics, hostname="192.168.1.15", retained=False, msg_count=3)
    for a in m:
            if a.topic == "dogFeederFeed":
                dogFeederFeed=a.payload
                print("dogFeederFeed is " + dogFeederFeed)
            if a.topic == "dogFeederCups1":
                dogFeederCups1 = a.payload
                print("dogFeederCups1 is " + dogFeederCups1)
            if a.topic == "dogFeederCups2":
                dogFeederCups2 = a.payload
                print("dogFeederCups2 is " + dogFeederCups2)

    feed(dogFeederCups1, dogFeederCups2)
    time.sleep(10)
    print("ready")
