from tkinter import *

root = Tk()
root.title("tkinterKeyboardEvents")


        # event is a param given here, to prevent the error
        # TypeError: clicker() takes 0 positional arguments but 1 was given
        # and to allow us to store where the button was clicked
def clicker(event):
                                                        # event.x and event.y give an int value of x and y coordinates
                                                        # while event.char  or event.keysym returns the key pressed, if
                                                        # event.width and event.height give the height and width of the
                                                        # widget
    myLabel = Label(root, text="you clicked a button at " + str(event.x) +" and " + str(event.y) + event.char + event.keysym)
    myLabel.pack()

myButton = Button(root, text="you clicked a button")
# to do event driven things in Tkinter, Egs: pressing Q makes an event happen
# we do this through "binding", which allows us to bind a particular function to a widget, done by the .bind function

            #"<Button-1>" representing a left mouse click, which is the event needed,
            # "<Button-2>" gives middle mouse, "<Button-3>" gives right mouse click
            # "<Enter>" represents the act of the mouse entering the coords of the button,
            # "<Leave>" represents the act of the mouse entering, then leaving the button coords
            # "<FocusIn>" represents tabbing the button with the keyboard
            # "<Return>" represents the enter key, after tabbing
            # "<Key>" represents any keyboard key, after tabbing
            # while the second param gives us the action provoked by that event
myButton.bind("<Key>", clicker)
myButton.pack(pady=20)




root.mainloop()