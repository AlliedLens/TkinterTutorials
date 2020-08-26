from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("TkinterWindows")


def open():
    top = Toplevel()
    lbl = Label(root, text="Hello")
    lbl.pack()
    lbl2 = Label(top, text="Heyyy")
    buttonQuit = Button(top, text="close window", command=top.destroy)
    buttonQuit.pack()

B = Button(root, text="click", command=open)
B.pack()

mainloop()