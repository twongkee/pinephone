from tkinter import *
import os
from PIL import ImageTk, Image
import subprocess

firstpic = 0
root = Tk()
frames_list = []
btn_list = []


def closepreview():
    print("closed click")
    command = root.destroy()


def pagenext():
    print("page next")


turn = "close"
turnLabel = Button(root, text=turn, font="Helvetica 12", command=closepreview)
turnLabel.grid(row=6, columnspan=2)


path = "/home/wongkt2/thumbnails"
pics = []
for pathroot, d_names, f_names in os.walk(path):
    # print( root, d_names, f_names)
    for f in f_names:
        if "jpg" == f[-3:]:
            print(f"{pathroot} {f}")
            pics += [pathroot + "/" + f]

# todo, currently loading all thumbnails
# may be too many, so rethink just loading a few?
imgs = []
blankimg = ImageTk.PhotoImage(Image.open("/home/wongkt2/dev/blank.jpg"))
for p in pics:
    print(p)
    imgs.append(ImageTk.PhotoImage(Image.open(p)))

# todo fix end cases
def process_turn(index):
    global firstpic
    global blankimg
    turnLabel.config()
    print(f"clicked {index}, first {firstpic}")
    
    if index < 8:
        picfile = pics[firstpic+index][25:]
        print(f"image {picfile}")
        print([f"/home/wongkt2/pyg2/bin/python /home/wongkt2/dev/pgimage.py {picfile}"])
        subprocess.call([f"/home/wongkt2/pyg2/bin/python /home/wongkt2/dev/pgimage.py /home/wongkt2/{picfile}"], shell=True)
    if index == 8:
        print("go next page")
        if firstpic < len(imgs) - 8:
            firstpic += 8
        for n in range(8):
            if n + firstpic + 8 < len(imgs):
                btn_list[n]["image"] = imgs[n + firstpic]
                print(firstpic, n, len(imgs))
        if firstpic > len(imgs) - 8:
            print("\n===\nlast page\n\n")
            for n in range(8):
                btn_list[n]["image"] = blankimg
            max = len(imgs) - firstpic
            for n in range(max):
                btn_list[n]['image'] = imgs[n + firstpic]
        print(firstpic, index, len(imgs))
    if index == 9:
        print("go prev page")
        if firstpic > 7:
            firstpic -= 8
        for n in range(8):
            if firstpic >= 0:
                btn_list[n]["image"] = imgs[firstpic + n]
                print(firstpic, n, len(imgs))
        print(firstpic, index, len(imgs))

    print(f"end clicked {index}, first {firstpic}")

prev = "prev"
prevLabel = Button(root, text=prev, font="Helvetica 12", command=lambda ndex=9:process_turn(ndex))
prevLabel.grid(row=5,column=0)
more = "next"
moreLabel = Button(root, text=more, font="Helvetica 12", command=lambda ndex=8:process_turn(ndex))
moreLabel.grid(row=5, column=1)

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
                    image=imgs[ndex],
                    command=lambda ndex=ndex: process_turn(ndex),
                )
            )
            btn_list[ndex].pack(expand=True, fill=BOTH)
            print(f"x{x} i{i} ndex{ndex}")
            ndex += 1
    root.resizable(width=False, height=False)


create_frames_and_buttons()

root.mainloop()
