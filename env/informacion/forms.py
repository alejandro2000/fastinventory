from django import forms

class envio(forms.Form):
	nombre= forms.CharField()
	correo= forms.EmailField()
	asunto= forms.CharField()
	mensaje= forms.CharField()