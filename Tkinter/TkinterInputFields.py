from tkinter import *

root = Tk()

# To create an entry widget, that would allow the user to input values, same parameters apply on this widget as on
# Button part, except it is now width, we can also change the border width, using the borderwidth param

e = Entry(root, fg="red", bg="yellow", width=50, borderwidth=10)
e.pack()
e.insert(0, "Enter your name:     ")

# to get text inside the box, we use .insert

# the e.get func will allow us to retrieve the user data and use it

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="enter your name", padx=20, pady = 20, command=myClick, fg="red", bg="gold")
myButton.pack()


root.mainloop()