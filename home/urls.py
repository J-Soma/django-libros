from django.urls import path
from home import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login', views.iniciar_sesion, name='login'),
	path('registro', views.registro, name='registro'),
	path('logout', views.cerrar_sesion, name='logout'),
	path('buscar', views.buscar, name='buscar'),
	path('libro/<str:isbn>', views.libro, name='libro')
]