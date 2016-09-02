#!/usr/bin/python

import serial
import time

ser = serial.Serial("/dev/dogFeedSensors", baudrate=115200, timeout=1)
time.sleep(2)
ser.flushInput()
ser.write('r')
time.sleep(0.1)
oldtime = time.time()
while True :
    if ((time.time()-oldtime) >  5):
        ser.write('r')
        oldtime = time.time()
    try:
        state=ser.readline().rstrip('\n')
	variable, value = state.split('=',1)
	if variable:
            print(variable + '=' + value)
    except:
        pass
ser.close
