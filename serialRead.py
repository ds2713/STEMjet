import serial

controller = serial.Serial("/dev/ttyACM0", 115200, timeout=.1)

while True:
	data = controller.readline()[:-2]
	if data:
		print data
