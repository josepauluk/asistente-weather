from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy_utils
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings
import requests

def get_engine(user, password, host, port, db):
    url = f"postgresql://{user}:{password}@{ost}:{port}/db"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

engine = get_engine(
    settings['pg_user'],
    settings['pg_password'],
    settings['pg_host'],
    settings['pg_port'],
    settings['pg_db']
    )

engine.url
# postgresql://alpha:***@localhost:5432/alpha

def get_engine_from_settings():
    keys = ['pg_user', 'pg_password', 'pg_hots', 'pg_port', 'pg_db']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad config file')
    
    return get_engine(
        settings['pg_user'],
        settings['pg_password'],
        settings['pg_host'],
        settings['pg_port'],
        settings['pg_db']
        )

def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session

session = get_session()

session

 # Create a PostgreSQL engine
engine = create_engine(settings['url'])
 # Check if the database exists, if not, create it
if not database_exists(engine.url):
    create_database(engine.url)
 # Create a session factory
Session = sessionmaker(bind=engine)
 # Make a GET request to a URL
response = requests.get('https://example.com')
 # Print the response content
print(response.content)

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