"""blogPersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from posts import views
from usuario import views
from informacion import views
from productos import views

from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include("posts.urls")),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('usuario/', include("usuario.urls")),
    path('productos/', include("productos.urls")),
    path('accounts/login/', login, {'template_name':'usuario/usuarioIngresar.html'}, name='ingresoUsuarios_u'),
    path('logout/', logout, name='logout'),
    path('', include("informacion.urls")),

    #para restaurar la contraseña enviando un mensaje por correo

    url(r'^reset/password_reset',password_reset,
        {'template_name':'reloadkey/reset_form.html','email_template_name':'reloadkey/reset_email.html'},
        name="password_reset"),

    url(r'^password_reset_done',password_reset_done,
        {'template_name':'reloadkey/reset_done.html'},
        name="password_reset_done"),

    url(r'^reset/(?P<uidb64>[0-94-Za-z_\-]+)/(?P<token>.+)/$',
        password_reset_confirm,{'template_name':'reloadkey/reset_confirm.html'},
        name="password_reset_confirm"),

    url(r'^reset/done',password_reset_complete,
        {'template_name':'reloadkey/reset_complete.html'},
        name="password_reset_complete")
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
