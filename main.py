'''
language:	Python 2.7.15rc1
Function:	communicate serial port via modem
'''

import time
import keyboard
import testIO

serial = testIO.SerialPort(None)

# text mode interface
print "-------------------------------------"
serial.scan()
print "-------------------------------------"
serial.list()
print ""
serial.input()
print "-------------------------------------"

# serial port settings
serial.config(115200, 0.1)

# show serial port settings
if serial.port.is_open == True:
	print "Serial port =",serial.name
	print ("Baud rate = 115200")
	print ("Time out = 0.1")

print "-------------------------------------"
print ("!!! ---Start test--- !!!")

while True:
	serial.send()
	#print(serial.read())
	time.sleep(0.1)
	if keyboard.is_pressed('q'):
		print ("!!! ---Quit test--- !!!")
		print "-------------------------------------"
		break