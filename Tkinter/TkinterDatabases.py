from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Databases")


#Databases

# create a database or connect to one, and saves it into the directory that we're currently in

conn = sqlite3.connect("address_book.db")

# Creating a cursor, which is something that you send off to do stuff, meaning it can be used to execute commands

cursor = conn.cursor()


""".................................................................................................................."""
# a database consists mainly of tables, which hold all the data. table is like a spreadsheet, with columns and rows, and
# everytime a new entry is added, it becomes a new row. while columns denote the category, like "names, addresses etc"

# cursor.execute(""" CREATE TABLE addresses (
#         first_name text,
#         last_name text,
#         city text,
#         state text,
#         zipcode integer
# )
# """)

# after the table has been created, the cursor.execute command has been hashed out, as we have already made our database
# using SQL lite, something that you havent learned yet.
""".................................................................................................................."""

# we now need to create some text boxes that allow us to type information into.

fieldName = Entry(root, width=30)
fieldName.grid(row=0, column=1, padx=10, pady=10)

fieldLastName = Entry(root, width=30)
fieldLastName.grid(row=1, column=1, padx=10, pady=5)

fieldCity = Entry(root, width=30)
fieldCity.grid(row=2, column=1, padx=10, pady=5)

fieldState = Entry(root, width=30)
fieldState.grid(row=3, column=1, padx=10, pady=5)

fieldZipcode = Entry(root, width=30)
fieldZipcode.grid(row=4, column=1, padx=10, pady=5)

deleteBox = Entry(root, width=30)
deleteBox.grid(row=10, column=1)
# the text box labels

fieldNameLabel = Label(root, text="First name: ", pady=10)
fieldNameLabel.grid(row=0, column=0)


fieldLastNameLabel = Label(root, text="Last name: ")
fieldLastNameLabel.grid(row=1, column=0)

fieldCityLabel = Label(root, text="City: ")
fieldCityLabel.grid(row=2, column=0)

fieldStateLabel = Label(root, text="State: ")
fieldStateLabel.grid(row=3, column=0)

fieldZipcodeLabel = Label(root, text="Zipcode: ")
fieldZipcodeLabel.grid(row=4, column=0)

selectBoxLabel = Label(root, text="ID Select: ")
selectBoxLabel.grid(row=10, column=0)

# function to save a record
def update():
    global editor
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()

    recordId = deleteBox.get()
    # the below statement is in SQL and tells that we need to update the things in these columns for our oid,
    # the dictionary designates what these things are(:first, :last etc)

    global fieldNameEditor
    global fieldLastNameEditor
    global fieldCityEditor
    global fieldStateEditor
    global fieldZipcodeEditor


    cursor.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        city = :city,
        state = :state,
        zipcode = :zipcode
    
        WHERE oid = :oid""",
        {"first" : fieldNameEditor.get(),
         "last" : fieldLastNameEditor.get(),
         "city" : fieldCityEditor.get(),
         "state" : fieldStateEditor.get(),
         "zipcode" : fieldZipcodeEditor.get(),

         "oid" : recordId
        }           )





    fieldNameEditor.delete(0, END)
    fieldLastNameEditor.delete(0, END)
    fieldCityEditor.delete(0, END)
    fieldStateEditor.delete(0, END)
    fieldZipcodeEditor.delete(0, END)


    conn.commit()
    conn.close()
    editor.destroy()
# function to edit a record
def edit():
    root.withdraw()
    global editor
    editor = Tk()
    editor.title('Update A Record')
    editor.geometry("400x300")
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # conn cursor
    cursor = conn.cursor()

    recordId = deleteBox.get()
    # query database
    cursor.execute("SELECT * FROM addresses WHERE oid =" + recordId)
    records = cursor.fetchall()

    # create global variables for text box names
    global fieldNameEditor
    global fieldLastNameEditor
    global fieldCityEditor
    global fieldStateEditor
    global fieldZipcodeEditor

    # create text boxes
    fieldNameEditor = Entry(editor, width=30)
    fieldNameEditor.grid(row=0, column=1, padx=10, pady=10)

    fieldLastNameEditor = Entry(editor, width=30)
    fieldLastNameEditor.grid(row=1, column=1, padx=10, pady=5)

    fieldCityEditor = Entry(editor, width=30)
    fieldCityEditor.grid(row=2, column=1, padx=10, pady=5)

    fieldStateEditor = Entry(editor, width=30)
    fieldStateEditor.grid(row=3, column=1, padx=10, pady=5)

    fieldZipcodeEditor = Entry(editor, width=30)
    fieldZipcodeEditor.grid(row=4, column=1, padx=10, pady=5)

    # the text box labels

    fieldNameLabelEditor = Label(editor, text="First name: ", pady=10)
    fieldNameLabelEditor.grid(row=0, column=0)

    fieldLastNameLabelEditor = Label(editor, text="Last name: ")
    fieldLastNameLabelEditor.grid(row=1, column=0)

    fieldCityLabelEditor = Label(editor, text="City: ")
    fieldCityLabelEditor.grid(row=2, column=0)

    fieldStateLabelEditor = Label(editor, text="State: ")
    fieldStateLabelEditor.grid(row=3, column=0)

    fieldZipcodeLabelEditor = Label(editor, text="Zipcode: ")
    fieldZipcodeLabelEditor.grid(row=4, column=0)

    editButton = Button(editor, text="Save record", command=update)
    editButton.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    # loop through results
    for record in records:
        fieldNameEditor.insert(0,record[0])
        fieldLastNameEditor.insert(0, record[1])
        fieldCityEditor.insert(0, record[2])
        fieldStateEditor.insert(0, record[3])
        fieldZipcodeEditor.insert(0, record[4])


# function to delete a button
def delete():
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
    # delete a record
    cursor.execute("DELETE from addresses WHERE oid= " + deleteBox.get())
    conn.commit()
    conn.close()

# create a submit button
def submit():
    # for some reason we also have to reconnect to the database when inside a function
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()


    # insert text into table, using SQL
    cursor.execute("INSERT INTO addresses VALUES (:fieldName, :fieldLastName, :fieldCity, :fieldState, :fieldZipcode)",
              {      "fieldName" : fieldName.get(),
                     "fieldLastName": fieldLastName.get(),
                    "fieldCity": fieldCity.get(),
                     "fieldState": fieldState.get(),
                     "fieldZipcode": fieldZipcode.get(),}
              )

    conn.commit()
    conn.close()
    # clear the text boxes
    fieldName.delete(0, END)
    fieldLastName.delete(0, END)
    fieldCity.delete(0, END)
    fieldState.delete(0, END)
    fieldZipcode.delete(0, END)


submitButton = Button(root, text="Add record to database", command=submit)
submitButton.grid(row=5, column=0, columnspan=2, pady=10, padx=10,ipadx=100)

# create a query button
def query():
    conn = sqlite3.connect("address_book.db")
    #create cursor
    cursor = conn.cursor()

    # query the database
    # * means everything
    # in most databases you have to create a primary key for each record in the database, a primary key is a unique
    # number. in SQLite3 the primary id is created automatically. since it is done automatically, the key is ignored,
    # to call on the primary key, we use "oid", primary keys might be useful to delete specific records
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    # cursor.fetchall gets all the records, cursor.fetchone gets the first record, cursor.fetchmany(num) gets num
    # amount of records, print(c.fetchall()), will not work, so we need to put it on a label
    print(records)
    printRecords = ""
    # loop through results
    for record in records:
        printRecords += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[5]) + "\n"

    queryLabel = Label(root, text=printRecords)
    queryLabel.grid(row=8, column=0, columnspan=2)

queryButton = Button(root, text="Show records", command=query)
queryButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create a delete button

deleteButton = Button(root, text="Delete record", command=delete)
deleteButton.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create an update button

editButton = Button(root, text="edit record", command=edit)
editButton.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# after we make a change, we have to "commit" it.
conn.commit()

# to close the connection after program has ended
conn.close()



root.mainloop()