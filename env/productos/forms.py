from django import forms
from .models import producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = [
            "titulo",
            "contenido",
            "imagen1",
            "imagen2",
            "imagen3",
            "imagen4",
            "precio",
            "cantidad",
        ]

