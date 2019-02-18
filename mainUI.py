import tkinter as tk
import time
import keyboard
import testIO
import testUI

serial = testIO.SerialPort(None)

serial.scan()

root = tk.Tk()

window = testUI.UI(root)

window.device['values'] = serial.device

serial.config(115200, 0.1)



root.mainloop()
