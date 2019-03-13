import tkinter as tk
import time
import keyboard
import testIO
import testUI

def scanning(): 
    if testUI.running:  # Only do this if the Stop button has not been clicked
        serial.name = app.device.get()
        serial.config(115200, 0.1)
        serial.send()

    # After 0.1 second, call scanning again (create a recursive loop)
    root.after(100, scanning)

serial = testIO.SerialPort(None)

serial.scan()

root = tk.Tk()
app = testUI.UI(root)
app.device['values'] = serial.device

root.after(100, scanning)  # After 0.1 second, call scanning
root.mainloop()
