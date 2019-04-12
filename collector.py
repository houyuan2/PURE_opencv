import serial
from serial import Serial
import time
import csv
import numpy as np


ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)

v_list = []
a_list = []
for i in range(1000):
    ser_bytes = ser.readline()
    l = ser_bytes.split()
    V = float(l[0][0:len(l[0])-2])
    A = float(l[1][0:len(l[0])-1])
    v_list.append(V)
    a_list.append(A)

v_list = np.array(v_list)
a_list = np.array(a_list)

print("Average V: ", np.mean(v_list))
print("Average A: ", np.mean(a_list))

with open("test_data.csv","w") as myFile:  
   writer = csv.writer(myFile)
   writer.writerows(v_list)
   writer.writerows(a_list)
myFile.close()

ser.close()

# "0.0000V, 0.0000A"