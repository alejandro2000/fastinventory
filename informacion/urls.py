from django.contrib import admin
from django.urls import include, path
from informacion import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('politicas/', views.politicas, name='politicas_p'),
    path('Nosotros/', views.quienesSomos, name='quienesSomos_p'),
    path('', views.index, name='index_p'),
]
