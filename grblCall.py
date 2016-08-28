import serial
import time

def feed(cups1, cups2):
    ser = serial.Serial("/dev/dogFeeder", baudrate=115200, timeout=1)
    time.sleep(2)
    #ser.flushInput()
    #ser.write('$H\r' .encode())		#tell GRBL to home
    #time.sleep(1)		#allow homing process to complete
    #ser.write('$X\r' .encode())		#unlock GRBL from expected error of homing
    #time.sleep(0.1)
    #print(ser.read(300))
    ser.flushInput()
    ser.write('G91\r' .encode())	#set to relative movements
    time.sleep(0.1)
    #print(ser.read(30))		#expeced 'ok' from GRBL
    ser.write('G1 X' .encode())	#move by 'X' at feedrate 'F'
    ser.write(cups1 .encode())
    ser.write('Y' .encode())
    ser.write(cups2 .encode())
    ser.write('F15\r' .encode())
    ser.close
   
#dogFeederCups1 = '1'
#dogFeederCups2 = '1'
#feed(dogFeederCups1, dogFeederCups2)
 
 
