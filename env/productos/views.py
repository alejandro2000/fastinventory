from django.http import HttpResponse, Http404
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import producto, factura, detalleFactura, tipoVenta, estadosFactura
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ProductoForm
from django.db.models import Q
from django.contrib.auth.models import User
from posts.models import Post
from usuario.models import user2

#para imprimir las facturas
from blogPersonal.utileria import render_to_pdf
from django.views import View

#para colocar decenas
import locale
import time

#para escoger un elemento a la zar de una lista
import random

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
    contact_list = producto.objects.all()

    filtro = request.GET.get('q')

    if filtro:
        contact_list = producto.objects.filter(
            Q(titulo__icontains=filtro)|
            Q(contenido__icontains=filtro)|
            Q(id__icontains=filtro)
            )

    paginator = Paginator(contact_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = {
        "titulo": "list",
        "object_list": contacts
    }
    return render(request, "productos/productos.html", context)

def producto_list_usua(request):

    contact_list = producto.objects.all()

    filtro = request.GET.get('q')

    if filtro:
        contact_list = producto.objects.filter(
            Q(titulo__icontains=filtro)|
            Q(contenido__icontains=filtro)|
            Q(id__icontains=filtro)
            )

    paginator = Paginator(contact_list, 20) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = {
        "titulo": "list",
        "object_list": contacts
    }
    return render(request, "productos/productos_usuarios.html", context)

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

def producto_delete(request, id=None):
    instance = get_object_or_404(producto, id=id)
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

        cantidadproductos = len(listaproductos)

        if cantidadproductos == 0:
            request.session['factura'] = 'error'
        else:
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
    
    detallesfacturas = []

    for f in factu:
        productos_aso = detalleFactura.objects.filter(idfactura=f.id)
        detallesfacturas.append(productos_aso)


    factu = zip(factu,detallesfacturas)

    contexto = {
        'contacts': factu,
    }   
    return render(request, 'productos/misfacturas.html', contexto)

def todaslasfacturas(request):
    factu = factura.objects.all()

    detallesfacturas = []

    for f in factu:
        productos_aso = detalleFactura.objects.filter(idfactura=f.id)
        detallesfacturas.append(productos_aso)


    factu = zip(factu,detallesfacturas)

    permiso = 'admin'
    contexto = {
        'contacts': factu,
        'permiso':permiso
    }   
    return render(request, 'productos/misfacturas.html', contexto)


def adjuntar_factura(request, id):
    f = factura.objects.get(id=id)
    f.comprobacion = request.FILES['compru']
    f.save()
    return redirect('misfacturas')


def imprimirFactura(request,id,*tags, **kwargs):
    fact = get_object_or_404(factura,id=id)
    prods = detalleFactura.objects.filter(idfactura=fact.id)
    data = {
        'nombreusu' : fact,
        'productos' : prods,
    }
    pdf =  render_to_pdf("productos/imprimirFactura.html",data)
    return HttpResponse(pdf, content_type="application/pdf")

def informeDeVenta(request,id,*tags, **kwargs):

    usuarios = User.objects.all()
    usurs = 0
    for obj in usuarios:
        usurs = usurs + 1

    product = producto.objects.all()
    prods = 0
    for obj in product:
        prods = prods + 1

    publicaciones = Post.objects.all()
    Posts = 0
    for obj in publicaciones:
        Posts = Posts + 1

    empleados = user2.objects.filter(perfil=4)
    empls = 0
    for obj in empleados:
        empls = empls + 1

    #podemos crear una clase que se llame motivador, para que esta con un método nos arroje una frase aleatoria para cuando queramos

    frases = ['Cuando vas por algo, no regreses hasta que lo consigas.','Tener grandes espectativas es la clave de todo.'
    ,'Lo que separa a los emprendedores exitosos de los no exitosos es la perseverancia.',
    'Quizas aun no llego a mi meta,pero hoy estoy mas cerca de lo que estaba ayer.',
    'La inspiracion existe, pero debe encontrarte trabajando by picaso.',
    'No hay aboslutamente nunguna otra forma de trinfar en la vida si no es por el constante esfuerzo by arnold schwarzenegger.',
    'Confia en ti mismo no importa lo que los demás piensen by arnold schwarzenegger.',
    'Cuando alguien hace lo que ama se nota, cuando no amas lo que haces,se nota aún más by steve jobs.',
    'Si tu no trabajas por tus sueños, alguien te contratará para que trabajes por los suyos by steve jobs.',
    'La innovación es lo que distingue a los lideres de los seguidores by steve jobs.',
    'No creo compañias solo por crearlas, sino para que logren cosas by elonk musk.',
    'Creo que es posible que la gente normal elija ser extraordinaria by Elon musk.',
    'La vida es demasiado corta para rencores a largo plazo.'
    ]

    frase = random.choice(frases)

    #sacar el total de ventas del mes y sacar las del mes anterior para saber si aumentaron o no

    #cantidad de productos vendidos

    data = {
        'usuarios' : usurs,
        'productos' : prods,
        'publicaciones' : Posts,
        'empleados' : empls,
        'fraseMotivacional' : frase,
        'totalVentas':ventas,
    }
    pdf =  render_to_pdf("empresa/informeDeVentas.html",data)
    return HttpResponse(pdf, content_type="application/pdf")



    





