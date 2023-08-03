# https://www.youtube.com/watch?v=nksauZe87Nw
import requests

city = input('Enter City: ')

# Para 5 días 
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
#BASE_URL = "https://api.openweathermap.org/data/2.5/onecall/timemachine?"
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=49c13bdb94527dbe6310d58ea4765102&units=metric".format(city)

# Se solicita la url para analizar
res = requests.get(url)

# Se reestructura mejor los datos para interpretarlos
data = res.json()
#print(data)

# Definr tres caracteristicas ambientales: 
# Temperatura, dirección del viento y descripción general de tiempo
# También laitud y longitud
temp = data["main"]["temp"]
wind_speed = data["wind"]["speed"]

latitude = data["coord"]["lat"]
longitude = data["coord"]["lon"]

description = data["weather"][0]["description"]

print("emperatura: ", int(temp),"°C")
print("Velocidad del viento: ", wind_speed, "m/s")
print("Latitud: ", latitude)
print("Longitud: ", longitude)
print("Descripción: ", description)