from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.producto_list, name="productos"),
    path('create/', views.producto_create, name="crear_p"),
    path('detalle/<slug:slug>', views.producto_detail, name="detalle_prod"),
    path('edit/<slug:slug>', views.producto_update, name="update"),
    path('delete/<slug:slug>', views.producto_delete, name="delete"),
    path('agregar/<slug:slug>/<int:cant>', views.agregarAlCarrito, name="agregar_carrito"),
    path('carrito/', views.carrito, name="ver_carrito"),

]
