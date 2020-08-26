from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("TkinterMessageBoxes")


def Popup():
    #                  ("Title Bar", " Info to be shown" )
    messagebox.showinfo("This is my Popup", "Hello World")

def PopupQuestion():
    response = messagebox.askyesno("this is pop up", "Yes or No?")
    # A yesno response return either one or two.
    if response == 1:
        Label(root, text="Yes").pack()
    else:
        Label(root, text="No").pack()


# The various types of messageboxes are:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

B = Button(root, text="Popup", command=Popup)
B.pack()
B2 = Button(root, text="other Popup", command=PopupQuestion)
B2.pack()


root.mainloop()

