from django.contrib import admin
from django.urls import include, path
from informacion import views
	
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('politicas/', login_required(views.politicas), name='politicas_p'),
    path('Nosotros/', login_required(views.quienesSomos), name='quienesSomos_p'),
    path('panel/', login_required(views.panel), name='panel'),
    path('', login_required(views.index), name='index_p'),

]
