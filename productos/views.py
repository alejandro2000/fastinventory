from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import producto
from .forms import ProductoForm

# Create your views here.
def producto_create(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Nuevo producto agregado")
        return redirect('productos')
    context = {
		'form': form
	}
    return render(request, "productos/produc_form.html", context)

def producto_detail(request, slug=None):
    instance = get_object_or_404(producto, slug=slug)
    context = {
        "titulo": instance.titulo,
        "instance": instance
    }
    return render(request, "productos/produc_detail.html", context)

def producto_list(request):
    queryset = producto.objects.all()
    context = {
        "titulo": "list",
        "object_list": queryset
    }
    return render(request, "productos/productos.html", context)

def producto_update(request, slug=None):
    instance = get_object_or_404(producto, slug=slug)
    form = ProductoForm(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Producto editado")
        return redirect('productos')
    context = {
        "titulo": instance.titulo,
        "instance": instance,
        "form": form,
    }
    return render(request, "productos/produc_form.html", context)

def producto_delete(request, slug=None):
    instance = get_object_or_404(producto, slug=slug)
    instance.delete()
    messages.success(request, "Producto eliminado")
    return redirect('productos')

def agregarAlCarrito(request, slug=None, cant=None):
    if "productos" in request.session:
        request.session["productos"].append([slug,cant])
    else:
        request.session["productos"]= [slug,cant];
    messages.success(request, slug + " agregado con exito")
    return redirect('productos')

def carrito(request):
    productos= {'slug':'motocicleta','codigo':1}
    return render(request,'productos/carrito.html',{'productos':productos})
