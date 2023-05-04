import requests
from bs4 import BeautifulSoup
import time

# Definir el código del producto que deseas buscar
# codigo_producto = input("Que deseas buscar ")

# Hacer una petición HTTP a la página de Truper
url = 'https://www.calculadora-de-derivadas.com'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
inputExpression = soup.find("input", {"name": "expression"})

payload = {"expression": "x**2"}
response = requests.post(url, data=payload)

soup = BeautifulSoup(html, "html.parser")

time.sleep(4)

derivate_div = soup.find("div", class_="calc-math")

result = derivate_div.find("span").text.split()

print(result)