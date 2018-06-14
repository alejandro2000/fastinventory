from django.contrib import admin

# Register your models here.
from .models import user2, perfiles, estados, productosdeseados
# Register your models here.



class extendUsuarioModelAdmin(admin.ModelAdmin):
	list_display = ["id","user","perfil","imagen"]
	class Meta:
		model = user2


class perfilesModelAdmin(admin.ModelAdmin):
	list_display = ["id","nombre_perfil"]
	class Meta:
		model = perfiles

class estadosModelAdmin(admin.ModelAdmin):
	list_display = ["id","nombre"]
	class Meta:
		model = estados

class deseosModelAdmin(admin.ModelAdmin):
	list_display = ["id","id_producto","id_user2"]
	class Meta:
		model = productosdeseados


admin.site.register(user2, extendUsuarioModelAdmin)
admin.site.register(perfiles, perfilesModelAdmin)
admin.site.register(estados, estadosModelAdmin)
admin.site.register(productosdeseados, deseosModelAdmin)

