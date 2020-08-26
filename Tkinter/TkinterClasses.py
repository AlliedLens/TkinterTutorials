from tkinter import *

root = Tk()
root.title("tkinterClasses")

# classes in tkinter are first made by normally defining a class, and we add the root window as one of our params in
# __init__
class David:        # master refers to root window
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text="Click me", command= self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("classes")

classRun = David(root)



root.mainloop()