import serial
import csv

# Adjust the COM port and baud rate based on your Arduino configuration
ser = serial.Serial('COM3', 9600)

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        
        # Split the data into values
        data = line.split(',')
        
        print(data)
    

except KeyboardInterrupt:
    print("Interrupted.")
    ser.close()
