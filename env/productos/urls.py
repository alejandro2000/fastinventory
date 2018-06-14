from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.producto_list_usua), name="productos_usua"),
    path('productos_panel/', login_required(views.producto_list), name="productos"),
    path('create/', login_required(views.producto_create), name="crear_p"),
    path('detalle/<slug:slug>', login_required(views.producto_detail), name="detalle_prod"),
    path('edit/<slug:slug>', login_required(views.producto_update), name="update"),
    path('delete/<int:id>', login_required(views.producto_delete), name="delete"),
    path('agregar/', login_required(views.agregarAlCarrito), name="agregar_carrito"),
    path('carrito/', login_required(views.carrito), name="ver_carrito"),
    path('eliminardelcarrito/<int:cod>', login_required(views.eliminardelCarrito), name="del_carrito"),
    path('generarfactura', login_required(views.pagargenerarfactura), name="generar_factura"),
    path('misfacturas/', login_required(views.vermisfacturas), name="misfacturas"),
    path('todaslasfacturas/', login_required(views.todaslasfacturas), name="todaslasfacturas"),
    path('subirFactura/<int:id>', login_required(views.adjuntar_factura), name="adjuntar_f"),
    path('descargarFactura/<int:id>', login_required(views.imprimirFactura), name="descargar_factura"),

]
