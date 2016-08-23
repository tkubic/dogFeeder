import serial
import time

ser = serial.Serial("/dev/dogFeeder", baudrate=115200, timeout=1)
time.sleep(2)
#ser.flushInput()
ser.write('$H\r')		#tell GRBL to home
time.sleep(1)		#allow homing process to complete
ser.write('$X\r')		#unlock GRBL from expected error of homing
time.sleep(0.1)
print(ser.read(300))
ser.flushInput()
ser.write('G91\r' .encode())	#set to relative movements
time.sleep(0.1)
#print(ser.read(30))		#expeced 'ok' from GRBL
ser.write('G1 X1 F15\r' .encode())	#move by 'X' at feedrate 'F'
time.sleep(0.1)
ser.write('?\r')
#print(ser.read(300))		#expected 'ok' from GRBL

ser.close
