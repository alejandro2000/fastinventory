from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from django.conf import settings
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField

from usuario.models import user2

# Create your models here.

class categorias(models.Model):
	nombre_categoria = models.CharField(max_length=80)

	def __str__(self):
		return self.nombre_categoria

def up_load_location(instance, filename): #esto nos sirve para guardar imagenes por carpetas segun el id
	return "%s/%s" %(instance.id, filename)


class Post(models.Model):
	titulo = models.CharField(max_length=150)
	slug = models.SlugField(unique=True)
	imagen = models.ImageField(upload_to=up_load_location,
		null=True, 
		blank=True,
		height_field="height_field",
		width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	contenido = RichTextField(('contenido del post'))
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)
	categoria = models.ForeignKey(categorias, on_delete=models.CASCADE, null=True)
	user = models.ForeignKey(user2, on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ["-timestamp","-actualizado"]

def create_slug(instance, new_slug=None):           #urls compartibles, nos cambia de id a el titulo
	slug = slugify(instance.titulo)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	if qs:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender , instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)



