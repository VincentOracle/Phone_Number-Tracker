import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import phonenumbers
import opencage
import folium
from tkinter import *


# # Prompts entry of PhoneNumber
# phone_number = input(
#     "Enter your PhoneNumber including country Code i.e +254........:\n")
# # First Country
# phoneNum_country = phonenumbers.parse(phone_number, "CH")  # Country History
# print(geocoder.description_for_number(phoneNum_country, "en"))  # Language

phone_number = "+2540764393092"
# OutPut
# Service Providers
service_pro = phonenumbers.parse(phone_number, "RO")
internetProvider = carrier.name_for_number(service_pro, "en")
print(internetProvider)
# Finding location in the google Map

key = '5557ee629f6947d09c5c9cc1b5928057'
pepnumbers = phonenumbers.parse(phone_number)
location = geocoder.description_for_number(pepnumbers, "en")
geocoder = OpenCageGeocode(key)
query = int(location)
results = geocoder.geocode(query)

# print(results)
lat = results[0]['geometry']['lat']
lng = results[1]['geometry']['lng']
print(lat, lng)
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("TheNumberLocation.html")
