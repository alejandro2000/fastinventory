from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.producto_list), name="productos"),
    path('create/', login_required(views.producto_create), name="crear_p"),
    path('detalle/<slug:slug>', login_required(views.producto_detail), name="detalle_prod"),
    path('edit/<slug:slug>', login_required(views.producto_update), name="update"),
    path('delete/<slug:slug>', login_required(views.producto_delete), name="delete"),
    path('agregar/', login_required(views.agregarAlCarrito), name="agregar_carrito"),
    path('carrito/', login_required(views.carrito), name="ver_carrito"),

]
