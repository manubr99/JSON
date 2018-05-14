#5-Pide una ubicación y muestra el tipo y el nombre de los animales que hay en dicha ubicación 
import json
from pprint import pprint
with open('animales.json') as data_file:
	data=json.load(data_file)
ubicacion = input("Introduce una ubicación: ")
for animal in data:
	if animal["Ubicacion"] == ubicacion:
		print(animal["Nombre"],"es", animal["Tipo"])