from tkinter import *
from tkinter import ttk

class UI:
	def __init__(self, master):
		master.title("test")
		master.geometry("200x100")
		
		frame = Frame(master)
		frame.pack()
		self.message = "Hello,world"
		
		self.testButton = Button(frame, text="Start Test", command=self.startTest)
		self.testButton.grid(row=0, column=0, padx=0, pady=10)
		
		self.quitButton = Button(frame, text="Quit", command=frame.quit)
		self.quitButton.grid(row=0, column=1, padx=0, pady=10)
		
		self.device = ttk.Combobox(frame, width=16)
		self.device['values'] = ()
		self.device.config(state='readonly')
		self.device.grid(row=1, column=0, padx=0, pady=0,columnspan=2)
		
	def startTest(self):
		print (self.message)
		self.testButton.config(text = "Stop test", command=self.stopTest)
		
	def stopTest(self):
		print (self.message)
		self.testButton.config(text = "Start test", command=self.startTest)