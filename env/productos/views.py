from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import producto, factura, detalleFactura, tipoVenta, estadosFactura
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ProductoForm
from django.contrib.auth.models import User

#para colocar decenas
import locale
import time

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
    stock = instance.cantidad
    cantidades= []
    for i in range(1,stock):
        cantidades.append(i)

    context = {
        "titulo": instance.titulo,
        "instance": instance,
        "stock": cantidades
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

        if cod in request.session['carrito']:

            lista= request.session['carrito']
            posicion= lista.index(cod)

            cantis = request.session['cantidades']

            cantiactual = cantis[posicion]

            cantis[posicion]= cant
            request.session['cantidades'] = cantis

        else: 
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
        request.session['factura']= 'pendiente'

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
        totales=[]
        for i in request.session["carrito"]:
            pro = get_object_or_404(producto, id=i)
            objs.append(pro)

        for c in request.session["cantidades"]:
            cants.append(c)


        for tot in range(len(objs)):
            vl = int(objs[tot].precio)*int(cants[tot])
            totales.append(vl)


        produ = zip(objs,cants,totales)

        contexto = {
            'producto': produ
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

def eliminardelCarrito(request,cod):
    if cod:
        #capturo las tuplas que exiten en la session
        lista = request.session['carrito']
        cantidades = request.session['cantidades']
        #identificar cual es la posición del objeto que deseo eliminar
        posicion = lista.index(str(cod))

        #elimino el objeto y sus respectivas cantidades
        del lista[posicion]
        del cantidades[posicion]

        request.session['carrito'] = lista
        request.session['cantidades'] = cantidades

        return redirect('ver_carrito')

def pagargenerarfactura(request):
    try:
        listaproductos = request.session['carrito']
        listacantidades = request.session['cantidades']

        products = zip(listaproductos,listacantidades)

        us = request.user.id
        usuario= get_object_or_404(User, id=us)

        tipd= get_object_or_404(tipoVenta, id=1)
        estf= get_object_or_404(estadosFactura, id=1)


        p = factura(
            paisEnvio=request.POST['codpai'],
            user=usuario,
            tipo=tipd,
        )
        p.save()

        facturas = factura.objects.all()
        ultimafactura = 0
        for i in facturas:
            ultimafactura = i.id

        factur = get_object_or_404(factura, id=ultimafactura)

        for p,c in products:
            prod = get_object_or_404(producto, id=p)
            detallef = detalleFactura(
                idfactura = factur,
                idProducto = prod,
                cantidad = c
            )
            detallef.save()


        request.session['factura'] = 'generada'
        del request.session['carrito']
        del request.session['cantidades']
        return redirect('ver_carrito')

    except Exception as e:
        return HttpResponse("Hubo un error al generar la factura")

def vermisfacturas(request):
    usu = request.user.id
    factu = factura.objects.filter(user=usu)
    
    filtro = request.GET.get('q')

    if filtro:
        factu = user2.objects.filter(
            Q(user__icontains=filtro)|
            Q(perfil__icontains=filtro)
            )

    paginator = Paginator(factu, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    factu = paginator.get_page(page)

    contexto = {
        'contacts': factu,
    }   
    return render(request, 'productos/misfacturas.html', contexto)

def todaslasfacturas(request):
    factu = factura.objects.all()
    
    filtro = request.GET.get('q')

    if filtro:
        factu = user2.objects.filter(
            Q(user__icontains=filtro)|
            Q(perfil__icontains=filtro)
            )

    paginator = Paginator(factu, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    factu = paginator.get_page(page)

    contexto = {
        'contacts': factu,
    }   
    return render(request, 'productos/misfacturas.html', contexto)




