from tkinter import *
from tkinter import ttk


root = Tk()
root.title("tkinterDropDownAndComboBoxesEvents")

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

def selected():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()

def comboClick(event):
    myLabel = Label(root, text=myCombo.get())
    myLabel.pack()

clicked = StringVar()
clicked.set(days[0])

drop = OptionMenu(root, clicked, *days)
drop.pack(pady=20)

myButton = Button(root, text="Select from list", command=selected)
myButton.pack()

myCombo = ttk.Combobox(root, value=days)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboClick)
myCombo.pack(pady=10)

root.mainloop()