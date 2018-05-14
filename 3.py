#3-Pide el nombre de un animal y muestra las observaciones y los rasgos del animal
import json
from pprint import pprint
with open('animales.json') as data_file:
	data=json.load(data_file)
nombre = input("Escribe el nombre de un animal:")
for animal in data:
	if animal["Nombre"] == nombre:
		print("Observacion:",animal["Observacion"])
		print("Rasgo:",animal["Rasgos"])