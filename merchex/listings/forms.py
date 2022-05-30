from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from listings.models import Band

class ContactUsForm(forms.Form):
	name = forms.CharField(required = False)
	email = forms.EmailField(max_length=254)
	message = forms.CharField(max_length=1000)

class BandAddForm(forms.ModelForm):
	class Meta:
		model = Band
		fields = '__all__'
		exclude =('active','official_homepage')