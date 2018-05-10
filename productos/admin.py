from django.contrib import admin
from .models import producto

# Register your models here.
class ProductoModelAdmin(admin.ModelAdmin):
    list_display = ["titulo","actualizado","timestamp"]
    list_display_links = ["actualizado"]
    list_filter = ["timestamp"]
    list_editable = ["titulo"]
    search_fields = ["titulo","contenido"]

    class Meta:
        model = producto

admin.site.register(producto, ProductoModelAdmin)
