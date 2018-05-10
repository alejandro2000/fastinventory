from django.contrib import admin
from .models import Post,categorias
# Register your models here.



class PostModelAdmin(admin.ModelAdmin):
	list_display = ["id","titulo","actualizado", "timestamp","imagen"]
	list_display_links = ["actualizado"]
	list_filter = ["timestamp"]
	search_fields = ["titulo","contenido"]
	list_editable = ["titulo"]
	class Meta:
		model = Post

class categoriasModelAdmin(admin.ModelAdmin):
	list_display = ["id","nombre_categoria"]
	list_display_links = ["nombre_categoria"]
	list_filter = ["nombre_categoria"]
	search_fields = ["nombre_categoria","id"]
	class Meta:
		model = categorias


admin.site.register(Post, PostModelAdmin)
admin.site.register(categorias, categoriasModelAdmin)



