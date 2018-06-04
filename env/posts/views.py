from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404, HttpResponseRedirect
from posts.models import Post, categorias
from django.contrib.auth.models import User
from django.db.models import Q
from urllib.parse import quote_plus

from django.views.generic import ListView

from .forms import agregarPublicacion

from datetime import datetime, date, time, timedelta
# Create your views here.


def post_create(request):
	categ = categorias.objects.all()
	return render(request,'crearpost.html',{'cat':categ,})

def post_save(request):
	cat = get_object_or_404(categorias, id=request.POST['categoria'])
	usuario = get_object_or_404(User, id=request.POST['user'])
	publi = Post(
		titulo  = request.POST['titulo'],
		contenido = request.POST['contenido'],
		imagen = request.FILES['imagen'],
		categoria = cat ,
		user = usuario,
	)
	publi.save()
	return redirect('list_p')


def post_update(request, slug):
	if not request.user.is_authenticated:
		raise Http404
	nom_session = request.user.username
	instance = get_object_or_404(Post, slug=slug)
	if nom_session != str(instance.user):
		messages.warning(request, 'usted no tiene autorización para realizar esta acción.')
		#ver = "usted no tiene autorización para realizar esta acción"
		return redirect("list_p")
	else:
		publi = Post.objects.get(slug=slug)
		categ = categorias.objects.all()
		return render(request,'actualizarpost.html',{'form':publi,'cat':categ,})

def actualizarPost(request, slug):
	if not request.user.is_authenticated:
		raise Http404
	nom_session = request.user.username
	instance = get_object_or_404(Post, slug=slug)
	if nom_session != str(instance.user):
		messages.success(request, 'usted no tiene autorización para realizar esta acción.')
		#ver = "usted no tiene autorización para realizar esta acción"
		return redirect("list_p")
	else:
		publi = Post.objects.get(slug=slug)
		cat = get_object_or_404(categorias, id=request.POST['categoria'])
		usuario = get_object_or_404(User, id=request.POST['user'])
		publi.titulo  = request.POST['titulo']
		publi.contenido = request.POST['contenido']
		publi.imagen = request.FILES['imagen']
		publi.categoria = cat
		publi.user = usuario
		publi.save()
		return redirect('list_p')



def post_detail(request, slug=None):
	dias = timedelta(days=3)
	hoy = datetime.now()
	hacetresdias = hoy-dias

	publc = Post.objects.filter(timestamp__gte=hacetresdias)
	consulta= get_object_or_404(Post, slug=slug)
	share_string=quote_plus(consulta.slug)
	contexto= {
		"consulta" : consulta,
		"share_string" : share_string,
		'fresc':publc
	}

	return render(request, "Detalle.html", contexto)

def post_list(request):
	dias = timedelta(days=3)
	hoy = datetime.now()
	hacetresdias = hoy-dias

	publc = Post.objects.filter(timestamp__gte=hacetresdias)

	contact_list = Post.objects.all()

	filtro = request.GET.get('q')

	if filtro:
		contact_list = Post.objects.filter(
			Q(titulo__icontains=filtro)|
			Q(contenido__icontains=filtro)
			)

	paginator = Paginator(contact_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	contacts = paginator.get_page(page)

	contexto = {
		'contacts': contacts,
		'fresc':publc
	}
	return render(request, 'indexListar.html', contexto)

"""	def get_context_data(self, **kwargs):
          		busqueda = self.request.GET.get("q")
          		context = super().get_context_data(**kwargs)
          		if busqueda:
          			context = Post.objects.filter(titulo__icontains=busqueda)
          			#context['q'] = Post.objects.get(titulo="los computadores")
          		return context  """


def post_delete(request, slug): # consulta y elimina si el metodo es post
	if not request.user.is_authenticated:
		raise Http404
	nom_session = request.user.username
	instance = get_object_or_404(Post, slug=slug)
	if nom_session != str(instance.user):
		messages.warning(request, 'usted no tiene autorización para realizar esta acción.')
		#ver = "usted no tiene autorización para realizar esta acción"
		return redirect("list_p")
	else:
		publi = Post.objects.get(slug=slug)
		if request.method == 'POST':
			publi.delete()
			return redirect('list_p')
		return render(request,'advertenciaEliminar.html',{'publi':publi})

def list_tecnologia(request):
	dias = timedelta(days=3)
	hoy = datetime.now()
	hacetresdias = hoy-dias

	publc = Post.objects.filter(timestamp__gte=hacetresdias)

	contact_list = Post.objects.filter(categoria=1)

	filtro = request.GET.get('q')

	if filtro:
		contact_list = Post.objects.filter(
			Q(titulo__icontains=filtro)|
			Q(contenido__icontains=filtro)
			)

	paginator = Paginator(contact_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	contacts = paginator.get_page(page)

	contexto = {
		'contacts': contacts,
		'fresc':publc
	}
	return render(request, 'indexListar.html', contexto)

def list_cine(request):
	dias = timedelta(days=3)
	hoy = datetime.now()
	hacetresdias = hoy-dias

	publc = Post.objects.filter(timestamp__gte=hacetresdias)
	contact_list = Post.objects.filter(categoria=2)

	filtro = request.GET.get('q')

	if filtro:
		contact_list = Post.objects.filter(
			Q(titulo__icontains=filtro)|
			Q(contenido__icontains=filtro)
			)

	paginator = Paginator(contact_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	contacts = paginator.get_page(page)

	contexto = {
		'contacts': contacts,
		'fresc':publc
	}
	return render(request, 'indexListar.html', contexto)

def list_deportes(request):
	dias = timedelta(days=3)
	hoy = datetime.now()
	hacetresdias = hoy-dias

	publc = Post.objects.filter(timestamp__gte=hacetresdias)
	contact_list = Post.objects.filter(categoria=3)

	filtro = request.GET.get('q')

	if filtro:
		contact_list = Post.objects.filter(
			Q(titulo__icontains=filtro)|
			Q(contenido__icontains=filtro)
			)

	paginator = Paginator(contact_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	contacts = paginator.get_page(page)

	contexto = {
		'contacts': contacts,
		'fresc':publc
	}
	return render(request, 'indexListar.html', contexto)

def list_salud(request):
	dias = timedelta(days=3)
	hoy = datetime.now()
	hacetresdias = hoy-dias

	publc = Post.objects.filter(timestamp__gte=hacetresdias)
	contact_list = Post.objects.filter(categoria=4)

	filtro = request.GET.get('q')

	if filtro:
		contact_list = Post.objects.filter(
			Q(titulo__icontains=filtro)|
			Q(contenido__icontains=filtro)
			)

	paginator = Paginator(contact_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	contacts = paginator.get_page(page)

	contexto = {
		'contacts': contacts,
		'fresc':publc
	}
	return render(request, 'indexListar.html', contexto)

def list_entrevista(request):
	dias = timedelta(days=3)
	hoy = datetime.now()
	hacetresdias = hoy-dias

	publc = Post.objects.filter(timestamp__gte=hacetresdias)
	contact_list = Post.objects.filter(categoria=5)

	filtro = request.GET.get('q')

	if filtro:
		contact_list = Post.objects.filter(
			Q(titulo__icontains=filtro)|
			Q(contenido__icontains=filtro)
			)

	paginator = Paginator(contact_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	contacts = paginator.get_page(page)

	contexto = {
		'contacts': contacts,
		'fresc':publc
	}
	return render(request, 'indexListar.html', contexto)
