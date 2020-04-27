#!/usr/bin/env python3

# import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import subprocess

button_width = 5


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.grid(row=2, column=3)

    def create_widgets(self):
        self.preview = Button(
            self, width=button_width, height=2, text="preview", command=self.runpreview
        )
        self.hi_there = Button(self, width=button_width, height=2)
        self.hi_there["text"] = "(click me)"
        self.hi_there["command"] = self.say_hi

        self.middle = Button(self, width=button_width, height=3)
        self.middle["text"] = " (O) "
        self.middle["command"] = self.middleclick

        self.img = ImageTk.PhotoImage(Image.open("/home/wongkt2/dev/latest.jpg"))
        self.pic = Label(image=self.img)

        self.quit = Button(
            self,
            text="QUIT",
            fg="red",
            width=button_width,
            height=2,
            command=self.master.destroy,
        )

        self.pic.grid(row=1, column=1, columnspan=3)
        self.preview.grid(row=2, column=0)
        self.hi_there.grid(row=2, column=1)
        self.middle.grid(row=2, column=2)
        self.quit.grid(row=2, column=3)

    def say_hi(self):
        subprocess.call(["bash /home/wongkt2/bin/ph640"], shell=True)
        self.img = ImageTk.PhotoImage(Image.open("/home/wongkt2/dev/latest.jpg"))
        self.pic = Label(image=self.img)
        self.pic.grid(row=1, column=1, columnspan=3)
        print("click me")

    def middleclick(self):
        subprocess.call(["bash /home/wongkt2/dev/smallpic.sh"], shell=True)
        self.img = ImageTk.PhotoImage(Image.open("/home/wongkt2/dev/second.jpg"))
        self.pic = Label(image=self.img)
        self.pic.grid(row=1, column=1, columnspan=3)
        print("click middle")

    def runpreview(self):
        subprocess.call(
            ["/home/wongkt2/py3/bin/python /home/wongkt2/dev/preview.py"], shell=True
        )


root = Tk()
app = Application(master=root)
app.mainloop()
