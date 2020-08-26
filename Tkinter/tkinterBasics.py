from tkinter import *
# In Tkinter, everything is a widget, the first thing you create is the root widget.
# A window is an instance of Tkinter’s Tk class.
#There are two steps to creating something on Tkinter, we first have to define the thing, and then put it in a window.
root = Tk()

#  Use the Label class to add some text to a window.
myLabel = Label(root, text="Hello World")
#To put the myLabel in the root widget, we can use .pack., wich isnt a frequently used function.
myLabel.pack()

# When you .pack() a widget into a window, Tkinter sizes the window as small as it can while still
# fully encompassing the widget.
# we now need to create an event loop, when a graphical interface is created, it is constantly looping, which allows
# it to observe instantaneous changes.
root.mainloop()

# root.mainloop() tells Python to run the Tkinter event loop. This method listens for events, such as button clicks or
# key presses, and blocks any code that comes after it from running until the window it’s called on is closed.

