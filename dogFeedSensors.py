#!/usr/bin/python

import serial
import time
import paho.mqtt.publish as publish

def upperfirst(x):
    return x[0].upper() + x[1:]

broker = "192.168.1.15"

ser = serial.Serial("/dev/dogFeedSensors", baudrate=115200, timeout=2)
time.sleep(2)
ser.flushInput()
time.sleep(2)
ser.write('r')
time.sleep(0.1)
oldtime = time.time()
while True :
    if ((time.time()-oldtime) >  10):
        ser.write('r')
        oldtime = time.time()
        variable =""
        value = ""
    try:
        state=ser.readline().rstrip('\n')
	variable, value = state.split('=',1)
	if variable:
            variable = "dogFeeder" + upperfirst(variable)
            print(variable + '=' + value)
            publish.single(variable, str(int(value)), hostname=broker)
    except:
        pass
ser.close
