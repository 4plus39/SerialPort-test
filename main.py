import sys
import platform
import glob
import serial
import time

class SerialPort(object):
	def __init__(self, name):
		self.name = name
		self.port = serial.Serial()
		self.device = []
		self.system = platform.system()
		
	def scan(self):
		if self.system.lower() == "linux":
			print ("os:linux")
			ports = glob.glob('/dev/tty[A-Za-z]*')
		elif self.system.lower() == "windows":
			print ("os:windows")
			ports = ['COM%s' % (i + 1) for i in range(256)]
		else:
			print ("Unknown os")
		
		for port in ports:
			try:
				s = serial.Serial(port)
				s.close()
				self.device.append(port)
			except (OSError, serial.SerialException):
				pass
	
	def list(self):
		for x in range(len(self.device)):
			print "number:", x, "   " , "device:", self.device[x]
		
	def config(self, baud_rate, time_out ):
		self.port = serial.Serial(self.name, baud_rate, timeout = time_out)
		
	def open(self):
		self.port.open
		
	def send(self):
		self.port.write(str.encode('ATI\r'))
		
	def read(self):
		return self.port.readlines()

class Frame(object):
	pass

test = SerialPort(None)

print "-------------------------------------"
test.scan()
print "-------------------------------------"
test.list()
print "-------------------------------------"
'''
for x in range(len(test.device)):
	print x, test.device[x]
'''

test.name = test.device[int(raw_input("Input serial device number:"))]


print (test.port.is_open)
test.config(115200, 0.1)
test.open()
print (test.port.is_open)

while True:
	print ("Start test:")
	test.send()
	print(test.read())
	time.sleep(0.1)

