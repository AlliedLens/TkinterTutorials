from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("DropDownBoxes")
root.geometry("400x400")

clickedVar = StringVar()
clickedVar.set("Monday")

days = ["Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"]

drop = OptionMenu(root, clickedVar, *days)
drop.pack()

def showSelection():
    myLabel= Label(root, text=clickedVar.get())
    myLabel.pack()

myButton = Button(root, text="show selection", command=showSelection)
myButton.pack()



root.mainloop()
