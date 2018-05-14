#1- Muestra los nombre de todos los gatos
import json
from pprint import pprint
with open('animales.json') as data_file:
	data=json.load(data_file)
for animal in data:
	if animal["Tipo"] == "Gato":
		print(animal["Nombre"])