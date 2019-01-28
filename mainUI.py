'''
language:	Python 2.7.15rc1
Function:	communicate serial port via modem
'''

from tkinter import *
import time
import keyboard
import testIO
import testUI

serial = testIO.SerialPort(None)

serial.scan()

root = Tk()

window = testUI.UI(root)

window.device['values'] = serial.device

root.mainloop()