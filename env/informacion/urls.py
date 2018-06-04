from django.contrib import admin
from django.urls import include, path
from informacion import views

	
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('politicas/', login_required(views.politicas), name='politicas_p'),
    path('Nosotros/', login_required(views.quienesSomos), name='quienesSomos_p'),
    path('panel/', login_required(views.panel), name='panel'),
    path('', login_required(views.index), name='index_p'),
    path('envmensaje/',login_required(views.enviarmsm), name='envmsm'),
    path('misacciones/',login_required(views.acciones), name='misacciones'),
    path('estadisticas/',login_required(views.estadisticas), name='estadisticas'),
    path('descargarPoliticas/',login_required(views.descargar.as_view()), name='descargarPoliticas')

]
