from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegistroForm, ComentarioForm
from .models import Libro, Autor, Comentario
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def index(request):
	return render(request, 'home/index.html')

def iniciar_sesion(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			nombre_usuario = form.cleaned_data['usuario']
			clave = form.cleaned_data['clave']

			usuario = authenticate(request, username=nombre_usuario, password=clave)

			if usuario is not None:
				login(request, usuario)
				return HttpResponseRedirect(reverse('index'))

			messages.add_message(request, messages.ERROR, 'Error: Usuario o contraseña incorrectos.')
			messages.add_message(request, messages.ERROR, 'Ejemplo 2.')
			messages.add_message(request, messages.ERROR, 'Ejemplo 3')
	else:
		form = LoginForm()

	return render(request, 'home/login.html', {'form': form})

def registro(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST)

		if form.is_valid():
			nombre_usuario = form.cleaned_data['usuario']
			clave = form.cleaned_data['clave']
			confirmacion = form.cleaned_data['confirmacion']

			if clave != confirmacion:
				messages.add_message(request, messages.ERROR, 'Error: La contraseña no coincide con la confirmación.')
			else:
				try:
					user = User.objects.create_user(username=nombre_usuario, password=clave)
					user.save()

					usuario = authenticate(request, username=nombre_usuario, password=clave)
					login(request,usuario)

					return HttpResponseRedirect(reverse('index'))
				except:
					messages.add_message(request, messages.ERROR, 'Error: El nombre  de usuario ya existe')
	else:
		form = RegistroForm()

	return render(request, 'home/registro.html', {'form': form})

def cerrar_sesion(request):
	logout(request)

	messages.add_message(request, messages.ERROR, 'Nos vemos!')
	return HttpResponseRedirect(reverse('index'))

def buscar(request):
	q = request.GET.get('q', '')

	str(q).strip()

	if len(q) == 0:
		messages.add_message(request, messages.ERROR, 'Ingresa el ISBN, titulo o autor de un libro a buscar.')
		return HttpResponseRedirect(reverse('index'))
	else:
		libros = Libro.objects.filter(Q(isbn__icontains=q) | Q(titulo__icontains=q) | Q(autores__nombre__icontains=q)).all()

		return render(request, 'home/buscar.html', {'libros':libros})


def libro(request, isbn):
	try:
		libro = Libro.objects.get(isbn=isbn)
	except:
		libro = None

	if request.method == 'POST':
		
		form = ComentarioForm(request.POST)

		if form.is_valid():
			c = Comentario(libro=libro,
							usuario=User.objects.get(pk=request.user.id),
							mensaje=form.cleaned_data['comentario'])
			c.save()

			return HttpResponseRedirect(reverse('libro', args=(libro.isbn,)))
	else:
		form = ComentarioForm()

	return render(request, 'home/libro.html', {'libro': libro, 'form': form})