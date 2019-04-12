import serial
from serial import Serial
import time
import csv


ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
# ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        print(ser_bytes[0:len(ser_bytes)-2].decode('ascii'))
    except:
        print("Keyboard Interrupt")
        break
ser.close()
    # ser_bytes = ser.readline()
    # print(ser_bytes.decode('utf-16'))


# ser = serial.Serial('../../../dev/ttyACM0', 115200) # Establish the connection on a specific port
# counter = 32 # Below 32 everything in ASCII is gibberish
# while True:
#      counter +=1
#      ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino
#      print(ser.readline()) # Read the newest output from the Arduino
#      sleep(.1) # Delay for one tenth of a second
#      if counter == 255:
#         counter = 32



# import serial

# serial_port = '/dev/ttyACM0';
# baud_rate = 115200; #In arduino, Serial.begin(baud_rate)
# write_to_file_path = "output.txt";

# output_file = open(write_to_file_path, "w+");
# ser = serial.Serial(serial_port, baud_rate)
# print(ser.name)
# while True:
#     print(ser.read())
#     line = ser.readline();
#     line = line.decode("utf-8") #ser.readline returns a binary, convert to string
#     print(line);
# output_file.write(line);