import serial
from serial import Serial
import time
import csv


ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
for i in range(1000):
        ser_bytes = ser.readline()
        print(ser_bytes.decode('ascii'))
ser.close()

# "0.0000V, 0.0000A"