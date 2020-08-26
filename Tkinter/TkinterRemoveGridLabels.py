from tkinter import *

root = Tk()

myLabel = Label(root)

def myClick():
    global myLabel
    myLabel.grid_forget()
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, "end")
    myLabel.grid(row=3, column=0, pady=10)
    if myLabel.winfo_exists() == 1:
            print("x")
    myButton["state"] = DISABLED

def myDelete():
    global myLabel
    myLabel.grid_forget()
    if myLabel.winfo_exists():
            print("x")
    myButton["state"] = NORMAL

e = Entry(root, width=50)
e.grid(row=0, column=0, padx=10, pady=10)

myButton = Button(root, text="Enter your Name", command=myClick)
myButton.grid(row=1, column=0, pady=10)

deleteButton = Button(root, text="Delete text", command=myDelete)
deleteButton.grid(row=2, column=0, pady=10)

root.mainloop()