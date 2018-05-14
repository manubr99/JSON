#2-Muestra cuantos animales hay en la ubicación Lora de Rio
import json
from pprint import pprint
with open('animales.json') as data_file:
	data=json.load(data_file)
contador = 0
for animal in data:
	if animal['Ubicacion'] == 'Lora del Rio':
		#pprint(animal['Nombre'])
		contador = contador+1
pprint(contador)