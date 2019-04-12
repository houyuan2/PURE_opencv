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
   s = ser_bytes.decode('ascii')
   l = s.split()
   if len(l) != 2:
      continue
   print(l)
   V = float(l[0][0:len(l[0])-2])
   A = float(l[1][0:len(l[1])-1])
   v_list.append(V)
   a_list.append(A)

np_v_list = np.array(v_list)
np_a_list = np.array(a_list)

print("Average V: ", np.mean(np_v_list))
print("Average A: ", np.mean(np_a_list))

with open("test_data.csv","w") as f:  
   fnames = ['V', 'A']
   writer = csv.DictWriter(f, fieldnames=fnames)

   writer.writeheader()
   for i in range(len(v_list)):
      writer.writerow({'V' : v_list[i], 'A': a_list[i]})
   f.close()

ser.close()

# "0.0000V, 0.0000A"
# ['11.9795V,', '0.0000A']
# ['11.9795V,', '0.0000A']
# ['11.9941V,', '0.0000A']
# ['11.9795V,', '0.0000A']
# ['11.9941V,', '0.0000A']