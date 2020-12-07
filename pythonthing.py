import sys
from tkinter import *
from RunLED import *
from tkinter.ttk import *

rL = LED()
#rL.Red_LED() 
#rL.Yellow_LED()
#rL.Green_LED()

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
		#quitButton.place(x=160, y=280)
		
		# Make Red LED Button
		redled = Button(self, text="Turn on red Light", command=rL.Red_LED)
		redled.pack(side = TOP, pady=10)
		#redled.place(x=130, y = 100)
		
		# Make Yellow LED Button
		yellowled = Button(self, text="Turn on Yellow Light", command=rL.Yellow_LED)
		yellowled.pack(side = TOP, pady=10)
		#yellowled.place(x=121, y = 150)
		
		# Make Green LED Button
		greenled = Button(self, text="Turn on Green Light", command=rL.Green_LED)
		greenled.pack(side = TOP, pady=10)
		#greenled.place(x=121, y = 200)

		

		randled = Button(self, text="Random Light", command=rL.Rand_LED)
		randled.pack(side = TOP, pady=10)
		#randled.place(x=140, y=50)

	def client_exit(self):
		exit()


root = Tk()
root.geometry("360x360")
app = Window(root)

root.mainloop()