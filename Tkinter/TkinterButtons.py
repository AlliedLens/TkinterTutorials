from tkinter import *

root = Tk()
# if you want the button to do something, we have to create a function

def myClick():
    myLabel = Label(root, text="The button has been clicked. hooray!")
    myLabel.pack()

# to execute this function, we need to use the "command" parameter in our Button() function

myButton = Button(root, text="CLick Me", padx=50, pady = 50, command=myClick, fg="red", bg="gold")
myButton.pack()

# observe that the text will be printed anew as many times as it is pressed,and keep in mind that there is no need to
# add parentheses to the function you use for "command"

# to disable a button we use the parameter state=DISABLED, the padx and pady parameters give us the dimensions of the
# button. fg and bg parameters can be used to change the colors




root.mainloop()

