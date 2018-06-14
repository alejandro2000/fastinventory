from django.contrib import admin
from django.urls import include, path
from posts import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.post_list), name='list_p'),
    path('publicacion', login_required(views.post_list_panel), name='list_admin'),
    path('tecnologia/', login_required(views.list_tecnologia), name='list_tecnologia'),
    path('cine', login_required(views.list_cine), name='list_cine'),
    path('deportes', login_required(views.list_deportes), name='list_deportes'),
    path('salud', login_required(views.list_salud), name='list_salud'),
    path('entrevistas', login_required(views.list_entrevista), name='list_entrevista'),
    path('crearpost/', login_required(views.post_create), name='create_p'),
    path('guardarpost/', login_required(views.post_save), name='guardar_p'),
    path('actualizarpost/<slug>', login_required(views.post_update), name='update_p'),
    path('actualizarpostg/<slug>', login_required(views.actualizarPost), name='actualizarPost'),
    path('detallePost/<slug>', login_required(views.post_detail), name='detail_p'),
    path('eliminarpost/<slug>', login_required(views.post_delete), name='delete_p'),
]
