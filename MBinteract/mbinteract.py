import serial


ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.open()

while True:
    ser.send