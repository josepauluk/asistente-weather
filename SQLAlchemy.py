import requests
from sqlalchemy import create_engine, Column, Integer, Float, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import BASE_URL, API_KEY, BD, USER, PASSWORD, HOST, PORT

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    temperature = Column(Float)
    wind_speed = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(String)

def get_weather_data(city):
    url = BASE_URL.format(city=city, API_KEY=API_KEY)
    res = requests.get(url)
    data = res.json()
    return data

def save_weather_data(data, city):
    temp = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    latitude = data["coord"]["lat"]
    longitude = data["coord"]["lon"]
    description = data["weather"][0]["description"]

    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{BD}')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear una instancia del modelo WeatherData y guardarla en la base de datos
    weather_data = WeatherData(city=city, temperature=temp, wind_speed=wind_speed, latitude=latitude, longitude=longitude, description=description)
    session.add(weather_data)
    session.commit()

    session.close()

if __name__ == "__main__":
    city = input('Enter City: ')
    data = get_weather_data(city)
    if data["cod"] == 200:
        save_weather_data(data, city)
        print("Datos guardados en la base de datos correctamente.")
    else:
        print("Error al obtener los datos del clima para la ciudad especificada.")
