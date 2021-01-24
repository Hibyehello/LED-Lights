import sys
try:
	from tkinter import *
except:
	from Tkinter import *

from RunLEDrpi import *
from tkinter.ttk import *


rL = LED()


class Window(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()
		
	def init_window(self):
			
		self.master.title("Led Lights")
			
		self.pack(fill=BOTH, expand=1)
			
		quitButton = Button(self, text="Quit", command=self.client_exit)
		quitButton.pack(side = BOTTOM, pady=10)
		
		
		# Make Red LED Button
		redled = Button(self, text="Turn on red Light", command=rL.Red_LED)
		redled.pack(side = TOP, pady=10)
		
		
		# Make Yellow LED Button
		yellowled = Button(self, text="Turn on Yellow Light", command=rL.Yellow_LED)
		yellowled.pack(side = TOP, pady=10)
		
		
		# Make Green LED Button
		greenled = Button(self, text="Turn on Green Light", command=rL.Green_LED)
		greenled.pack(side = TOP, pady=10)
		

		
		# Make Random Button
		randled = Button(self, text="Random Light", command=rL.Rand_LED)
		randled.pack(side = TOP, pady=10)


		# Make Lightshow
		lsButton = Button(self, text="Light Show", command=rL.LSButton)
		lsButton.pack(side = TOP, pady=10)

	def client_exit(self):
		exit()

def main():
	root = Tk()
	root.geometry("360x360")
	app = Window(root)
	root.mainloop()