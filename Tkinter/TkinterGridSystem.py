from tkinter import *

root = Tk()

myLabel1 = Label(root, text="hello world")
myLabel2 = Label(root, text="My name is David")
myLabel3 = Label(root, text="                ")

# The grid system, acts exactly like a grid, grids have columns, up and down, and rows. the columns and rows are
# numbered, starting from 0.

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1,column=1)

# notice that when you resize it, unlike with, pack(), it stays in the same spot, the top corner in this instance
# and does not resize.

# It is important to remember that the positioning is relative, meaning that if i put say column=1 and column=5 for two
# seperate labels, if there is nothing in the columns between them, then it will just show them directly adjacent to
# each other.

# although for readability, we seperate the creation, and the adding into screen part of the program, we can still join
# it together for egs:
# myLabel1 = Label(root, text="hello world").grid(row=0, column=0)

root.mainloop()



