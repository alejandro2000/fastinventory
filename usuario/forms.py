from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class registroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]

		labels = {
			'username' : 'Nombre de Usuario',
			'first_name' : 'Nombres',
			'last_name' : 'Apellidos',
			'email' : 'Correo',
		}


