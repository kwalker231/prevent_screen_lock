import random
import pyautogui
import time
import tkinter as tk
import keyboard
from tkinter import *
from tkinter import ttk

pyautogui.FAILSAFE = False

class noLockGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(noLockGUI, self).__init__()
        self.running = False
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
        self.waitlabel = ttk.Label(self.guiFrame, text="wait (sec)")
        self.waitlabel.pack(anchor=E, expand=True)
        self.waittextbox = Text(self.guiFrame, height = 1, width = 5)
        self.waittextbox.pack(anchor=E, expand=True)
        self.quitbutton = ttk.Button(self.guiFrame, text='quit', command=self.destroy)
        self.quitbutton.pack(anchor=SW, expand=True)
        #self.updatecoord()

    def updatecoord(self):
        if self.running:
            self.statuslabel.config(text="Program Running: "+"x: "+str(pyautogui.position().x)+" y: "+str(pyautogui.position().y))
            self.after(100, self.updatecoord)

    def startMove(self):
        s = self.waittextbox.get("1.0",END)
        s = s.strip('\n')
        if not s.isnumeric():
            wait = 5.0
        else:
            wait = int(s)

        if 1 > wait:
            self.statuslabel.config(text="wait time need to be larger than 1")
            return
        wait = wait/10.0
        self.running = True
        while self.running:
            x = random.randint(-(self.screenSize.width/6), self.screenSize.width/6)
            y = random.randint(-(self.screenSize.height/6), self.screenSize.height/6)
            pyautogui.moveRel(x,y)
            #self.statuslabel.config(text="Program Running: "+"x: "+str(pyautogui.position().x)+" y: "+str(pyautogui.position().y))
            self.updatecoord()
            for i in range(10):
                if keyboard.is_pressed('q'):
                    self.stopMove()
                time.sleep(wait)
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