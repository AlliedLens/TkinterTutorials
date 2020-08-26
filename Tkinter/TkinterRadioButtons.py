from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("TkinterRadioButtons")

# The intvar function allows Tkinter to keep track of changes over time that happen to the variable, so that if a change
# does happen, it'll know that.

# r = IntVar()

TOPPINGS = [
    # "item to show", "val returned"
    ("Pepperoni", "Pepperoni"),
    ("Mushroom", "Mushroom"),
    ("Olive", "Olive"),
    ("Cheese", "Cheese"), ]

pizza = StringVar()



for text, topping in TOPPINGS:
    Radiobutton(root, text=text, value=topping, variable=pizza).pack(anchor=W)

# r.set(), would assign a value to the Tkinter variable above
# To pass a string, we'd use StrVar function

pizza.set("Cheese")

def clicked(func_value):
    myLabel = Label(root, text=func_value)
    myLabel.pack()

# Tkinter variables behave differently from other python variables, we assign a value to each of these widgets below,
# with the variable param, which calls the variable, and the value param, which assigns a value to the variable.

#Radiobutton(root, text="option_1", variable=r, value=1, command=lambda : clicked(r.get())).pack()
#Radiobutton(root, text="option_2", variable=r, value=2, command=lambda : clicked(r.get())).pack()
b = Button(root, text="click for topping", command=lambda: clicked(pizza.get())).pack()
myLabel = Label(root)
myLabel.pack()

mainloop()