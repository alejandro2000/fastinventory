from django.contrib import admin
from django.urls import include, path
from usuario import views

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('listarusuarios/', login_required(views.listarUsuarios), name='list_u'),
    path('detalleusuario/<int:idusu>', login_required(views.user_detail), name='detalle_u'),
    path('eliminarusuario/<int:idusu>', login_required(views.eliminarUsuarios), name='eliminar_u'),
    path('crearusuarios/', login_required(views.registrarUsuario.as_view()), name='crearUsuario_u'),
    path('perfilusuario/<str:username>', login_required(views.perfilUsuario), name='perfilUsuario_u'),
    path('perfilusuarioG/<int:idusu>', login_required(views.guardarPerfilUsuario), name='guardarPerfilUsuario_u'),
    path('empleados/contratar', login_required(views.contratarEmpleado), name='contratarEmpleado'),
    path('empleados/consultar', login_required(views.consultarEmpleados), name='consultarEmpleados'),
    path('empleados/asignarcontrato/<int:idusu>', login_required(views.contratar), name='contratar'),   
    path('empleados/despedir/<int:idusu>', login_required(views.despedir), name='despedir'),   
]
