from tkinter import *


root = Tk()
root.title("tkinterMenuBoxes")

myMenu = Menu(root)
# unlike other widgets, we have to configure the menu
root.config(menu=myMenu)

# creating function
def ourCommand():
    pass
#we can use the "tearoff" option to not have the "-------------" at the beginning of the menu.
# Without this, if you click on it it will open actually the menu in a new window.
# create a menu item, ie a menu inside a menu, a sub-menu
fileMenu = Menu(myMenu, tearoff=0)
    # add_cascade, instead of pack or grid because it cascades downward
myMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="new....", command=ourCommand)
# to add a "_______" between options
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

# creating another menu item
editMenu = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy", command=ourCommand)
editMenu.add_separator()
editMenu.add_command(label="cut", command=ourCommand)


root.mainloop()
