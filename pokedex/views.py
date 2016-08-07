from django.shortcuts import render, HttpResponse
from django.views.generic import View

class Home(View):
	def get(self, request): #self->Pasarle el apuntador de si mismo            request->Variable viajando en todo el 
		template_name = "home.html"
		#return HttpResponse('Bienvenido entrenador Pokemon!')
		return render(request,template_name)

class Pikachu(View):
	def get(self, request):
		return HttpResponse('Pika Pika CHUUUUUUUUU')
