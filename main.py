'''
language:	Python 2.7.15rc1
Function:	communicate serial port via modem
'''
import platform
import glob
import serial
import time
import keyboard

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
		for index in range(len(self.device)):
			print "number:", index, "   " , "device:", self.device[index]
			
	def input(self):
		self.name = self.device[int(raw_input("Input serial device number:"))]
		
	def config(self, b_rate, t_out):
		self.port = serial.Serial(self.name, b_rate, timeout = t_out)
		
	def send(self):
		self.port.write(str.encode('ATI\r'))
		
	def read(self):
		return self.port.readlines()


test = SerialPort(None)

# text mode interface
print "-------------------------------------"
test.scan()
print "-------------------------------------"
test.list()
print ""
test.input()
print "-------------------------------------"

# serial port settings
test.config(115200, 0.1)

# show serial port settings
if test.port.is_open == True:
	print "Serial port =",test.name
	print ("Baud rate = 115200")
	print ("Time out = 0.1")

print "-------------------------------------"
print ("!!! ---Start test--- !!!")

while True:
	test.send()
	#print(test.read())
	time.sleep(0.1)
	if keyboard.is_pressed('q'):
		print ("!!! ---Quit test--- !!!")
		print "-------------------------------------"
		break
