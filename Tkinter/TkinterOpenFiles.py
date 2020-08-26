from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("TkinterWindows")

def OpenImage():
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/nellissery/Desktop/python code/spaceinvader",
                                               title="Select a file",
                                               filetypes=(("Folders", "*.FOLDER"),
                                                            ("all files", "*.*"),
                                                            ("PNG files", "*.PNG")))

    myImage = ImageTk.PhotoImage(Image.open(root.filename))
    myImageLabel = Label(image=myImage)
    myImageLabel.pack()


B = Button(root, text="Open File", command=OpenImage).pack()

root.mainloop()