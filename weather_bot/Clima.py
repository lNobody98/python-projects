import requests

API_KEY = "b0fa483cbde002b1422fe6c2106cdce1"
ciudad = input("¿Nombre de la Ciudad?")
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
respuesta = requests.get(url)
datos = respuesta.json()
print(datos)

if datos["cod"] == 200:
    print(f"Ciudad: {datos['name']}")
    print(f"Temperatura: {datos['main']['temp']}")
    print(f"Clima: {datos['weather'][0]['description']}")
    print(f"Humedad: {datos['main']['humidity']}")
else:
    print("Ciudad no encontrada")
