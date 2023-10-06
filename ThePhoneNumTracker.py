
# AUTHOR:Were Vincent
# DATE:03/08/2022
# Python Phone Number Tracker


from opencage.geocoder import OpenCageGeocode
import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from tkinter import *


def Search():
    #number = int(float(entry.get()))
    number = "+254703694570"
    print(number)
    print(location)

    # OutPut
    service_pro = phonenumbers.parse(number)
    internetProvider = carrier.name_for_number(service_pro, "en")
    print(internetProvider)
    # Finding location in the google Map

    key = '5557ee629f6947d09c5c9cc1b5928057'
    number = "+254703694570"
    pepnumbers = phonenumbers.parse(number)
   # location = geocoder.description_for_number(pepnumbers, "en")
    geocoder = OpenCageGeocode(key)
    query = int(location)
    results = geocoder.geocode(query)

# print(results)
    lat = results[0]['geometry']['lat']
    lng = results[1]['geometry']['lng']
    print(lat, lng)
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)
    myMap.save("C:\\Users\\n\\DesktopMyFifth.html")


#

def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


# The GUI
window = Tk()

# delete button
delete = Button(window, text="Delete", command=delete)
delete.pack(side=RIGHT)

# Backspace
backspace = Button(window, text="Backspace", command=backspace)
backspace.pack(side=RIGHT)

# Search button
search = Button(window, text="Search", command=Search)
search.pack(side=RIGHT)


# Entry Widget
entry = Entry()
entry.pack()
# entry.config(title=('Enter Phone Number'))
entry.config(font=('Consolas', 30))
entry.config(bg=('blue'))
entry.config(fg=('green'))
#entry.insert(0, 'Country Code:')

# The Number to be searched
#number = int(float(entry.get()))
number = "+254703694570"
pepnumbers = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumbers, "en")
window.mainloop()
