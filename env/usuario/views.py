from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

from usuario.forms import registroForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from usuario.models import user2, perfiles


class registrarUsuario(CreateView):
	model = User 
	template_name = "usuario/usuarioCrear.html"
	form_class = registroForm
	success_url = reverse_lazy('ingresoUsuarios_u')

def listarUsuarios(request):
	ident = request.user.id
	paraimagen = User.objects.exclude(id=ident)

	filtro = request.GET.get('q')

	if filtro:
		paraimagen = User.objects.filter(
			Q(username__icontains=filtro)
			)

	paginator = Paginator(paraimagen, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	paraimagen = paginator.get_page(page)

	contexto = {
		'contacts': paraimagen,
	}	
	return render(request, 'usuario/usuariolistar.html', contexto)

def listarUsuarios(request):
	ident = request.user.id
	paraimagen = User.objects.exclude(id=ident)

	filtro = request.GET.get('q')

	if filtro:
		paraimagen = User.objects.filter(
			Q(username__icontains=filtro)
			)

	paginator = Paginator(paraimagen, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	paraimagen = paginator.get_page(page)

	contexto = {
		'contacts': paraimagen,
	}	
	return render(request, 'usuario/usuariolistar.html', contexto)

def user_detail(request, idusu):
	consulta= get_object_or_404(User, id=idusu)
	paraimagen = get_object_or_404(user2, user=consulta.id)
	contexto= {
		"consulta" : consulta,
		"paraimagen" : paraimagen,
	}

	return render(request, "usuario/usuarioDetalle.html", contexto)


def perfilUsuario(request,username):
	form = get_object_or_404(User, username=username)
	paraimagen = get_object_or_404(user2, user=form.id)
	cargos = perfiles.objects.all()
	contexto = {'form':form,'extend':paraimagen,'cargos':cargos,}
	return render(request,'usuario/perfilUsuario.html',contexto)

def guardarPerfilUsuario(request, idusu):

	perfil = User.objects.get(id=idusu)

	perfil.username = request.POST['username']
	perfil.first_name = request.POST['first_name']
	perfil.last_name = request.POST['last_name']
	perfil.email = request.POST['email']
	perfil.save()

	userextend = user2.objects.get(user=idusu)	
	userextend.imagen = request.FILES['imagen']
	cargo = request.POST['cargo']
	userextend.perfil = get_object_or_404(perfiles, id=cargo)  #es una instancia del objeto en la foranea
	userextend.save()
	return HttpResponseRedirect(reverse('list_p'))

def eliminarUsuarios(request, idusu):
	usuario= get_object_or_404(User, id=idusu)
	if request.method == 'POST':
		usuario.delete()
		return redirect('list_u')

	return render(request,'usuario/usuarioeliminar.html',{'usuario':usuario})

def contratarEmpleado(request):
	paraimagen = user2.objects.exclude(perfil=4)
	return render(request,'empleados/empleadoscontratar.html',{'contacts':paraimagen})

def consultarEmpleados(request):
	empledos = user2.objects.filter(perfil=4)

	filtro = request.GET.get('q')

	if filtro:
		empledos = user2.objects.filter(
			Q(username__icontains=filtro)|
			Q(email__icontains=filtro)
			)

	paginator = Paginator(empledos, 5) # Show 5 contacts per page

	page = request.GET.get('page')
	contacts = paginator.get_page(page)

	contexto = {
		'contacts': contacts,
	}	
	return render(request, 'empleados/empleadosListar.html', contexto)


def contratar(request , idusu):
	persona = get_object_or_404(user2, user=idusu)
	perfila = get_object_or_404(perfiles, id=4)
	persona.perfil = perfila
	persona.save()
	return redirect('consultarEmpleados')

def despedir(request , idusu):
	persona = get_object_or_404(user2, user=idusu)
	perfila = get_object_or_404(perfiles, id=1)
	persona.perfil = perfila
	persona.save()
	return redirect('consultarEmpleados')


