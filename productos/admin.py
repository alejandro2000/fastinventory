from django.contrib import admin
from .models import producto, estadosFactura,tipoVenta,factura,detalleFactura

# Register your models here.
class ProductoModelAdmin(admin.ModelAdmin):
    list_display = ["titulo","actualizado","timestamp"]
    list_display_links = ["actualizado"]
    list_filter = ["timestamp"]
    list_editable = ["titulo"]
    search_fields = ["titulo","contenido"]

    class Meta:
        model = producto

class ProductoModelAdmin2(admin.ModelAdmin):
    list_display = ["id","nombre_estado"]
    list_display_links = ["nombre_estado"]
    list_filter = ["nombre_estado"]
    search_fields = ["nombre_estado","id"]

    class Meta:
        model = estadosFactura

class ProductoModelAdmin3(admin.ModelAdmin):
    list_display = ["id","paisEnvio","user","estado_proceso"]
    list_display_links = ["id"]
    list_editable = ["estado_proceso"]
    search_fields = ["estado_proceso","paisEnvio","id"]

    class Meta:
        model = factura

class ProductoModelAdmin4(admin.ModelAdmin):
    list_display = ["id","idfactura","idProducto","cantidad"]
    list_display_links = ["idProducto"]
    list_filter = ["idProducto"]
    search_fields = ["idProducto","cantidad"]

    class Meta:
        model = detalleFactura

class ProductoModelAdmin5(admin.ModelAdmin):
    list_display = ["id","tipo"]
    list_display_links = ["tipo"]
    list_filter = ["tipo"]
    search_fields = ["tipo","id"]

    class Meta:
        model = tipoVenta


admin.site.register(producto, ProductoModelAdmin)
admin.site.register(estadosFactura, ProductoModelAdmin2)
admin.site.register(factura, ProductoModelAdmin3)
admin.site.register(detalleFactura, ProductoModelAdmin4)
admin.site.register(tipoVenta, ProductoModelAdmin5)
