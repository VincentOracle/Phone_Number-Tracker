
# Python Program that tracks phone Numbers Geological Position and the Service providers
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

my_number1 = "+254703694570"
my_number2 = "+917980846985"
# First Country

country1 = phonenumbers.parse(my_number1, "CH")
print(geocoder.description_for_number(country1, "en"))
# Service Providers
service_prov1 = phonenumbers.parse(my_number1, "RO")
print(carrier.name_for_number(service_prov1, "en"))

# Second Country
country2 = phonenumbers.parse(my_number2, "CH")
print(geocoder.description_for_number(country2, "en"))

# Service Providers
service_prov2 = phonenumbers.parse(my_number2, "RO")
print(carrier.name_for_number(service_prov2, "en"))
