from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):
	nombre = models.CharField(max_length=120)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Autores' # Nombre a mostrar en admin

class Libro(models.Model):
	isbn = models.CharField(max_length=13, unique=True)
	titulo = models.CharField(max_length=200)
	fecha_pub = models.IntegerField()

	autores = models.ManyToManyField(Autor, related_name='libros')

	def __str__(self):
		return f'{self.isbn} - {self.titulo}, {self.fecha_pub}'

class Comentario(models.Model):
	libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='comentarios')
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
	mensaje = models.CharField(max_length=200)