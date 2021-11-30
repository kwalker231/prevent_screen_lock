#created by kwalker231 @2021
import random
import pyautogui
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk

class noLockGUI(tk.Tk):
	def __init__(self, *args, **kwargs):
		super(noLockGUI, self).__init__()
		self.running = True
		self.screenSize = pyautogui.size()

#GUI component:
		self.guiFrame = ttk.Frame(self)
		self.guiFrame.pack(fill=BOTH,expand=True)

		self.statuslabel = ttk.Label(self.guiFrame, text="Press Start To Randomly Move Mouse")
		self.statuslabel.pack(anchor=CENTER)
		self.startbutton = ttk.Button(self.guiFrame, text ='start',command=self.startMove)
		self.startbutton.pack(anchor=CENTER)
		self.stopbutton = ttk.Button(self.guiFrame, text ='stop', command=self.stopMove)
		self.stopbutton.pack(anchor=CENTER)
		self.quitbutton = ttk.Button(self.guiFrame, text='quit', command=self.destroy)
		self.quitbutton.pack(anchor=SW, expand=True)

	def startMove(self):
		self.running = True
		while self.running:
			x = random.randint(-(self.screenSize.width/6), self.screenSize.width/6)
			y = random.randint(-(self.screenSize.height/6), self.screenSize.height/6)
			pyautogui.moveRel(x,y)
			self.statuslabel.config(text="Program Running: "+"x: "+str(pyautogui.position().x)+" y: "+str(pyautogui.position().y))
			for i in range(10):
				time.sleep(0.5)
				root.update()


	def stopMove(self):
		self.running = False
		self.statuslabel.config(text="Press Start To Randomly Move Mouse")


if __name__ == "__main__":
	root = noLockGUI()
	root.title("No Screen Lock")
	root.geometry("300x200")
	#style = ttk.Style()
	#style.configure('TFrame', background='white')

	root.mainloop()