from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

def politicas(request):
	return render(request,'empresa/politicasDePrivacidad.html',{})

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
