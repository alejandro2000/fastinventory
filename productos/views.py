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

def agregarAlCarrito(request):
    #agregar al carrito los productos
    if "carrito" in request.session and "cantidades" in request.session:
        cod = request.POST['cod']
        cant = request.POST['cantidad']

        lista = request.session["carrito"]
        lista.append(cod)
        request.session["carrito"] = lista

        #agregar las cantidades de cada producto

        listacantidad = request.session["cantidades"]
        listacantidad.append(cant)
        request.session["cantidades"] = listacantidad
    else:
        request.session['carrito'] = []
        request.session['cantidades'] = []

        cod = request.POST['cod']
        cant = request.POST['cantidad']

        lista = request.session["carrito"]
        lista.append(cod)
        request.session["carrito"] = lista

        #agregar las cantidades de cada producto

        listacantidad = request.session["cantidades"]
        listacantidad.append(cant)
        request.session["cantidades"] = listacantidad


    
    return redirect('ver_carrito')

def carrito(request):
    """productos= ["computador",1,"tablet",2]
    productos.append("celular")
    productos.append(3)

    nombres = []
    codigos = []

    for i in range(len(productos)):
        if (i%2==0):            
            nombres.append(productos[i])
        else:
            codigos.append(productos[i])

    pro = productos.index("tablet")
    del productos[pro]"""
    if "carrito" in request.session and "cantidades" in request.session:
        objs=[]
        cants=[]
        for i in request.session["carrito"]:
            pro = get_object_or_404(producto, id=i)
            objs.append(pro)

        for c in request.session["cantidades"]:
            cants.append(c)

        contexto = {
            'carro': objs,
            'cantidades': cants,
        }
    else:
        request.session['carrito'] = []
        request.session['cantidades'] = []
        objs=[]
        cants=[]
        for i in request.session["carrito"]:
            pro = get_object_or_404(producto, id=i)
            objs.append(pro)

        for c in request.session["cantidades"]:
            cants.append(c)

        contexto = {
            'carro': objs,
            'cantidades': cants,
        }

    return render(request,'productos/carrito.html',contexto)
