from tkinter import *

root = Tk()

def myClick():
    global myLabel
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, "end")
    myLabel.pack(pady=10)
    if myLabel.winfo_exists() == 1:
            print("x")
    myButton["state"] = DISABLED

def myDelete():
    global myLabel
    myLabel.destroy()
    if myLabel.winfo_exists():
            print("x")
    myButton["state"] = NORMAL

e = Entry(root, width=50)
e.pack(padx=10, pady=10)

myButton = Button(root, text="Enter your Name", command=myClick)
myButton.pack(pady=10)

deleteButton = Button(root, text="Delete text", command=myDelete)
deleteButton.pack(pady=10)

root.mainloop()