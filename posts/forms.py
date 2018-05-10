from django import forms
from posts.models import Post


class agregarPublicacion(forms.ModelForm):

	class Meta:

		model = Post

		fields = [
			'titulo',
			'contenido',
			'imagen',
			'user',
		]

		labels = {
			'titulo' : 'Titulo',
			'contenido' : 'Contenido',
		}


