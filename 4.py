#4-Pide el nombre de un animal y muestra el tipo de animal que es
import json
from pprint import pprint
with open('animales.json') as data_file:
	data=json.load(data_file)
nombre = input("Introduce el nombre de un animal: ")
for animal in data:
	if animal["Nombre"] == nombre:
		print(animal["Tipo"])