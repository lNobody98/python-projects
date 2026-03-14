#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

respuesta = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(respuesta.text, "html.parser")

libros = soup.find_all("article", class_="product_pod")
for libro in libros:
    titulo = libro.h3.a["title"]
    precio = libro.find("p", class_="price_color").text
    print(titulo)
    print(precio)
    print("----------------")
