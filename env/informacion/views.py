# -*- coding: utf:8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.core.mail import EmailMessage
from productos.models import producto
from posts.models import Post
from usuario.models import user2

from django.http import HttpResponse
from django.views import View
from blogPersonal.utileria import render_to_pdf


from .forms import envio

def politicas(request):
	return render(request,'empresa/politicasdepv.html',{})

def quienesSomos(request):
	return render(request,'empresa/quienes_somos.html',{})

def index(request):
	return render(request,'empresa/index.html',{})

"""def login(request):
	#1. capturar los datos de usuario y Clave
	usuario = request.POST['username']
	clave = request.POST['password']
	try:
		#2. verificar que existen en la tabla personas
		per = User.objects.get(username=usuario, password=clave)
		#creamos varible de sesion con datos en una lista
		request.session['log'] = [per.identi, per.nombre, per.apellido, per.tipo_usuario]

		return redirect('index_p')
	except User.DoesNotExist:
		return redirect('index_p')

def logout(request):
	try:
		#destruimos variable de sesion
		del request.session['log']

		return redirect('login')
	except Exception as e:
		return redirect('login')"""

def panel(request):
	return render(request,'empresa/panel.html',{})


def enviarmsm(request):
	if request.method == 'POST':
		formulario = envio(request.POST)
		if formulario.is_valid():
			asunto = formulario.cleaned_data['asunto']
			mensaje = formulario.cleaned_data['mensaje']
			correo = formulario.cleaned_data['correo']
			mail = EmailMessage(asunto,mensaje,correo,to=['inventoryfast@gmail.com'])
			mail.send()
			return redirect('index_p')

def acciones(request):
	return render(request,"empresa/acciones.html")

def estadisticas(request):
	usuarios = User.objects.all()
	usurs = 0
	for obj in usuarios:
		usurs = usurs + 1

	product = producto.objects.all()
	prods = 0
	for obj in product:
		prods = prods + 1

	publicaciones = Post.objects.all()
	Posts = 0
	for obj in publicaciones:
		Posts = Posts + 1

	empleados = user2.objects.filter(perfil=4)
	empls = 0
	for obj in empleados:
		empls = empls + 1

	contexto = {
		"usuarios" : usurs,
		"productos" : prods,
		"publicaciones" : Posts,
		"empleados":empls
	}
	return render(request,"empresa/estadistica.html",contexto)

class descargar(View):

	def get(self, request, *tags, **kwargs):
		"""data = {
									'nombreusu' : request.user.username
								} lo podemos enviar por contexto"""
		pdf =  render_to_pdf("empresa/politicasDePrivacidad.html")
		return HttpResponse(pdf, content_type="application/pdf")


