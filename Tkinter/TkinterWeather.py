from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title("Weather Api")
root.configure(background="green")

# haven't gotten API key, so program will not work.
# where url is supposed to be.

apiRequest = requests.get("put your api key here")

try:
    api = json.loads(apiRequest.content)
    city = api[0]["ReportingArea"]
    quality = api[0]["AQI"]
    category = api[0]["Category"]["Name"]
except Exception as e:
    api = "Error......"

myLabel = Label(root, text = city + "air quality" + str(quality) + " " + category, font=("Times New Roman", 38))
myLabel.pack()

root.mainloop()