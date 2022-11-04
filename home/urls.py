from django.urls import path
from home import views

urlpatterns = [
	path('', views.index, name='index')
	path('login', views.iniciar_sesion, name='login'),
]