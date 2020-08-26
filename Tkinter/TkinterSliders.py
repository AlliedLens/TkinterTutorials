from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("TkinterSliders")
root.geometry("400x400")


verticalSlider = Scale(root, from_=400, to=0)
verticalSlider.pack()

horizontalSlider = Scale(root, from_=400, to=0, orient=HORIZONTAL)
horizontalSlider.pack()

def adjust():
    root.geometry(str(horizontalSlider.get()) + "x" + str(verticalSlider.get()) )

myButton = Button(root, text="Click me to adjust size", command=adjust)
myButton.pack()


root.mainloop()