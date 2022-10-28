import os
import csv
from dotenv import load_dotenv
from home.models import Autor, Libro

load_dotenv()

archivo = open(os.getenv('IMPORT_FILE'), 'r')
lector = csv.DictReader(archivo)

for fila in lector:

	try:
		# Verificar si el autor existe en la base de datos
		a = Autor.objects.get(nombre=fila['author'])
	except:
		# Si el autor no existe, guardarlo en la base de datos
		a = Autor(nombre=fila['author'])
		a.save()

	try:
		# Verificar si el libro existe en la base de datos
		l = Libro.objects.get(isbn=fila['isbn'])
	except:
		# Si el libro no existe, guardarlo en la base de datos
		l = Libro(isbn=fila['isbn'], titulo=fila['title'], fecha_pub=fila['year'])
		l.save()

		l.autores.add(a)
		l.save()

	print(l, end=' - ')
	print(a)

archivo.close()