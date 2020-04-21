#!/usr/bin/env python3

# quick python tkinter , pillow wrapper to take pictures on pinephone


# import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import subprocess


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.grid(row=2, column=3)

    def create_widgets(self):
        self.hi_there = Button(self, width=10, height=2)
        self.hi_there["text"] = "(click me)"
        self.hi_there["command"] = self.say_hi

        self.middle = Button(self, width=10, height=3)
        self.middle["text"] = " (O) "
        self.middle["command"] = self.middleclick

        self.img = ImageTk.PhotoImage(Image.open("/home/wongkt2/dev/latest.jpg"))
        self.pic = Label(image=self.img)

        self.quit = Button(
            self, text="QUIT", fg="red", width=10, height=2, command=self.master.destroy
        )

        self.pic.grid(row=1, column=1, columnspan=3)
        self.hi_there.grid(row=2, column=1)
        self.middle.grid(row=2, column=2)
        self.quit.grid(row=2, column=3)

    def say_hi(self):
        print("hi there, everyone!")

    def middleclick(self):
        subprocess.call(["bash /home/wongkt2/dev/smallpic.sh"], shell=True)
        self.img = ImageTk.PhotoImage(Image.open("/home/wongkt2/dev/second.jpg"))
        self.pic = Label(image=self.img)
        self.pic.grid(row=1, column=1, columnspan=3)
        print("click middle")


root = Tk()
app = Application(master=root)
app.mainloop()
