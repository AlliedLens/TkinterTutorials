from tkinter import *

root = Tk()
root.title("Checkboxes")
root.geometry("400x400")

var = StringVar()

# the value returned by a checkbox is either zero, or one, by default, however this can be changed by changed by the
# the onvalue and offvalue

c = Checkbutton(root, text="check this box", variable=var, offvalue="off", onvalue="on")
c.deselect()
c.pack()


def showResult():
    myLabel = Label(root, text=var.get())
    myLabel.pack()

myButton = Button(root, text="show result", command= showResult )
myButton.pack()



root.mainloop()