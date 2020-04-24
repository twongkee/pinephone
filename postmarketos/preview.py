from tkinter import *
import os
from PIL import ImageTk, Image

firstpic = 0
root = Tk()
frames_list = []
btn_list = []


def pagenext():
    print("next click")
    command = root.destroy()


turn = "close"
turnLabel = Button(root, text=turn, font="Helvetica 12", command=pagenext)
turnLabel.grid(row=5, columnspan=2)

path = "/home/wongkt2/thumbnails"
pics = []
for pathroot, d_names, f_names in os.walk(path):
    # print( root, d_names, f_names)
    for f in f_names:
        if "jpg" == f[-3:]:
            print(f"{pathroot} {f}")
            pics += [pathroot + "/" + f]


imgs = []
for p in pics:
    print(p)
    imgs.append(ImageTk.PhotoImage(Image.open(p)))

# todo fix end cases
def process_turn(index):
    global firstpic
    turnLabel.config()
    print(f"clicked {index}")
    if index == 7:
        print("go next page")
        for n in range(8):
            if n + firstpic + 8 < len(imgs):
                btn_list[n]["image"] = imgs[n + firstpic]
                print(firstpic, n, len(imgs))
        if firstpic < len(imgs) - 8:
            firstpic += 8
        print(firstpic, index, len(imgs))
    if index == 0:
        print("go prev page")
        for n in range(8):
            if firstpic - n > 0:
                btn_list[n]["image"] = imgs[firstpic - n]
                print(firstpic, n, len(imgs))
        if firstpic > 7:
            firstpic -= 8
        print(firstpic, index, len(imgs))


def create_frames_and_buttons():
    ndex = 0
    i = 0
    x = 0
    for i in range(4):
        for x in range(2):
            frames_list.append(Frame(root, width=160, height=120))
            frames_list[ndex].propagate(False)
            frames_list[ndex].grid(row=i, column=x, sticky="nsew", padx=2, pady=2)
            btn_list.append(
                Button(
                    frames_list[ndex],
                    text="",
                    font="Helvetica 16 bold",
                    image=imgs[ndex],
                    command=lambda ndex=ndex: process_turn(ndex),
                    # command= process_turn(ndex),
                )
            )
            btn_list[ndex].pack(expand=True, fill=BOTH)
            print(f"x{x} i{i} ndex{ndex}")
            # x += 1
            ndex += 1
        # i += 1
    root.resizable(width=False, height=False)


create_frames_and_buttons()

root.mainloop()
