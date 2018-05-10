from django.shortcuts import render

# Create your views here.

def politicas(request):
	return render(request,'empresa/politicasDePrivacidad.html',{})

def quienesSomos(request):
	return render(request,'empresa/quienes_somos.html',{})

def index(request):
	return render(request,'empresa/index.html',{})
