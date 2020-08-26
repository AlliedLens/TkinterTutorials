from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images&Icons")
root.iconbitmap("C:/Users/nellissery/Desktop/medical_brain_icon_147355.ico")

location = "C:/Users/nellissery/Desktop/"

image0 = ImageTk.PhotoImage(Image.open("C:/Users/nellissery/Desktop/download.jpg"))
image1 = ImageTk.PhotoImage(Image.open("C:/Users/nellissery/Desktop/download (1).jpg"))
image2 = ImageTk.PhotoImage(Image.open("C:/Users/nellissery/Desktop/images.jpg"))
image3 = ImageTk.PhotoImage(Image.open("C:/Users/nellissery/Desktop/images (1).jpg"))

image_list = [image0,image1,image2,image3]
my_label = Label(image=image0)

img_number = 0

status = Label(root, text="image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

def forward():
    global img_number
    global my_label
    global button_forward
    global button_backward
    if img_number == 3:
        button_forward = Button(root, text=">>", state=DISABLED)
    else:
        my_label.grid_forget()
        img_number += 1
        my_label  = Label(image=image_list[img_number])
        my_label.grid(row=0, column=0, columnspan=3)
        status = Label(root, text="image " +  str(img_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=E + W)

def backward():
    global img_number
    global my_label
    global button_forward
    global button_backward
    if img_number == 0:
        button_backward = Button(root, text="<<", state=DISABLED)
        button_backward.grid(row=1, column=0)
    else:
        my_label.grid_forget()
        img_number -= 1
        my_label  = Label(image=image_list[img_number])
        my_label.grid(row=0, column=0, columnspan=3)
        status = Label(root, text="image " + str(img_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                       anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=E + W)

    return

button_quit = Button(root, text="Exit program", command = root.quit)

button_backward = Button(root,text="<<",command=backward)
button_forward = Button(root, text=">>", command=forward)



my_label.grid(row=0, column=0, columnspan=3)

button_quit.grid(row=1,column=1, pady=10)
button_backward.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=E+W)

root.mainloop()