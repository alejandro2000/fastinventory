from django.db import models
from django.contrib.auth.models import User
from productos.models import producto

# Create your models here.




class perfiles(models.Model):
	nombre_perfil = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre_perfil

	class Meta:
		ordering = ["id"]

class estados(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ["id"]

def up_load_location(instance, filename): #esto nos sirve para guardar imagenes por carpetas según el id
	return "%s/%s" %(instance.id, filename)

class user2(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to=up_load_location,
		null=True, 
		blank=True,
		height_field="height_field",
		width_field="width_field")
	height_field = models.IntegerField(default=0, null=True)
	width_field = models.IntegerField(default=0, null=True)
	edad = models.IntegerField(default=0)
	tarjetaCredito = models.IntegerField(default=0)
	direccion = models.CharField(max_length=50)
	telefono = models.IntegerField(default=0)
	fechaRegistro = models.DateTimeField(auto_now_add=True, auto_now=False)
	estado = models.ForeignKey(estados, on_delete=models.CASCADE, default=1, null=True, blank=True)
	perfil = models.ForeignKey(perfiles, on_delete=models.CASCADE, null=True, blank=True, default=1)

	class Meta:
		ordering = ["id"]

class productosdeseados(models.Model):
	id_producto  = models.ForeignKey(producto, on_delete=models.CASCADE)
	id_user2 = models.ForeignKey(User, on_delete=models.CASCADE)



