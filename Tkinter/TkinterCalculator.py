from tkinter import *

root = Tk()

# to change the title

root.title("Tkinter Calculator")

e = Entry(root, fg="Navy", bg="SlateGrey", width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

def number(num_string):
    try:
        number = int(num_string)
    except ValueError:
        number = float(num_string)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clr():
    e.delete(0, END)

def button_add():
    print(e.get())
    global first_number
    global operator
    operator = "addition"
    first_number =  e.get()
    e.delete(0, END)

def button_minus():
    global first_number
    global operator
    operator = "subtraction"
    first_number =  e.get()
    e.delete(0, END)

def button_product():
    global first_number
    global operator
    operator = "multiplication"
    first_number =  e.get()
    e.delete(0, END)

def button_quotient():
    global first_number
    global operator
    operator = "division"
    first_number =  e.get()
    e.delete(0, END)

def button_power():
    global first_number
    global operator
    operator = "exponential"
    first_number =  e.get()
    e.delete(0, END)

def button_erase():
    input_list = list(e.get())
    list_erased = input_list[:-1]
    list_erased_joined = "".join(list_erased)
    e.delete(0, END)
    e.insert(0, list_erased_joined)

def button_dot():
    e.insert(END, ".")

def button_factorial():
    print(e.get())
    global first_number
    global operator
    operator = "addition"
    first_number =  e.get()
    e.delete(0, END)


def button_equal(first_num):
    second_number = e.get()
    e.delete(0,END)
    if operator == "addition":
        answer = number(first_number) + number(second_number)
        e.insert(0, answer)
    if operator == "subtraction":
        answer = number(first_number) - number(second_number)
        e.insert(0, answer)
    if operator == "multiplication":
        answer = number(first_number) * number(second_number)
        e.insert(0, answer)
    if operator == "division":
        answer = number(first_number) / number(second_number)
        e.insert(0, answer)
    if operator == "exponential":
        answer = number(first_number) ** number(second_number)
        e.insert(0, answer)


# buttons are created

button_1 = Button(root, text="1", padx=40, pady=20,command=lambda: button_click(1), fg="navy", bg="tomato")
button_2 = Button(root, text="2", padx=40, pady=20,command=lambda: button_click(2), fg="navy", bg="tomato")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3),fg="navy", bg="tomato")

button_4 = Button(root, text="4", padx=40, pady=20,command=lambda: button_click(4),fg="navy", bg="tomato")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5),fg="navy", bg="tomato")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6),fg="navy", bg="tomato")

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7),fg="navy", bg="tomato")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8),fg="navy", bg="tomato")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9),fg="navy", bg="tomato")

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0),fg="navy", bg="tomato")
button_pi = Button(root, text="3.1428", padx=25, pady=20, command=lambda: button_click(3.1428),fg="navy", bg="silver")

button_plus = Button(root, text="+", padx=39, pady=20, command=button_add,fg="navy", bg="silver")
button_multiply = Button(root, text="*", padx=39, pady=20, command=button_product,fg="navy", bg="silver")
button_divide = Button(root, text="/", padx=41, pady=20, command=button_quotient,fg="navy", bg="silver")
button_subtract = Button(root, text="-", padx=42, pady=20, command=button_minus,fg="navy", bg="silver")
button_exponent = Button(root, text="**", padx=38, pady=20, command=button_power,fg="navy", bg="silver")
button_decimal = Button(root, text=".", padx=40, pady=20,command=button_dot, fg="Navy", bg="silver")



button_eql = Button(root, text="=", padx=87, pady=20, command=lambda: button_equal(first_number),fg="Navy", bg="SlateGrey")
button_clear = Button(root, text="clear", padx=79, pady=20, command=button_clr,fg="Navy", bg="SlateGrey")
button_del = Button(root, text="del", padx=37, pady=20,command=button_erase, fg="Navy", bg="SlateGrey")

# put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_plus.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan= 2)
button_eql.grid(row=5, column=1, columnspan=2)

button_divide.grid(row=6, column=0)
button_multiply.grid(row=6,column=1)
button_subtract.grid(row=6, column=2)

button_exponent.grid(row=7, column=0)
button_pi.grid(row=7, column=1)
button_del.grid(row=7, column=2)

button_decimal.grid(row=8, column=0)




root.mainloop()
