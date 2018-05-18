from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from django.conf import settings
from django.db.models.signals import pre_save

# Create your models here.
def up_load_location(instance, filename): #esto nos sirve para guardar imagenes por carpetas según el id
    return "%s/%s" %(instance.id, filename)

class producto(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    imagen1 = models.ImageField(
		null=True,
		blank=True,
		height_field="height_field1",
		width_field="width_field1")
    height_field1 = models.IntegerField(default=0)
    width_field1 = models.IntegerField(default=0)
    imagen2 = models.ImageField(
        null=False,
        blank=True,
        height_field="height_field2",
        width_field="width_field2")
    height_field2 = models.IntegerField(default=0)
    width_field2 = models.IntegerField(default=0)
    imagen3 = models.ImageField(
        null=False,
        blank=True,
        height_field="height_field3",
        width_field="width_field3")
    height_field3 = models.IntegerField(default=0)
    width_field3 = models.IntegerField(default=0)
    imagen4 = models.ImageField(
        null=False,
        blank=True,
        height_field="height_field4",
        width_field="width_field4")
    height_field4 = models.IntegerField(default=0)
    width_field4 = models.IntegerField(default=0)
    contenido = models.TextField()
    precio = models.IntegerField()
    cantidad = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.titulo

def create_slug(instance, new_slug=None):           #urls compartibles, nos cambia de id a el titulo
    slug = slugify(instance.titulo)
    if new_slug is not None:
        slug = new_slug
    qs = producto.objects.filter(slug=slug).order_by("-id")
    if qs:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender , instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=producto)

# modelos de facturación

class estadosFactura(models.Model):
    nombre_estado = models.CharField(max_length=30,default='en proceso')

class tipoVenta(models.Model):
    tipo = models.CharField(max_length=30)

class factura(models.Model):
    paisEnvio = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    tipo = models.ForeignKey(tipoVenta, on_delete=models.CASCADE)
    estado_proceso = models.ForeignKey(estadosFactura, on_delete=models.CASCADE)

class detalleFactura(models.Model):
    idfactura = models.ForeignKey(factura, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    sub_total = models.IntegerField(default=0)

