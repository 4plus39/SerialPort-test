'''
language:	Python 2.7.15rc1
Function:	communicate serial port via modem
'''

from tkinter import *
import time
import keyboard
import testIO
import testUI

test = testIO.SerialPort(None)


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
