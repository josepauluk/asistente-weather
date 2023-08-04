import requests
import psycopg2
from config import BASE_URL, API_KEY, BD, USER, PASSWORD, HOST, PORT

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

    # Establecer la conexión con la base de datos
    conn = psycopg2.connect(database=BD, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cursor = conn.cursor()

    # Insertar los datos en la tabla
    insert_query = "INSERT INTO weather_data (city, temperature, wind_speed, latitude, longitude, description) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (city, temp, wind_speed, latitude, longitude, description))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

if __name__ == "__main__":
    city = input('Enter City: ')
    data = get_weather_data(city)
    if data["cod"] == 200:
        save_weather_data(data, city)
        print("Datos guardados en la base de datos correctamente.")
    else:
        print("Error al obtener los datos del clima para la ciudad especificada.")
