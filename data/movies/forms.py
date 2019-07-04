from django import forms
from .models import Data

class movieform(forms.Modelform):
	name = forms.TextField(max_length=300)
    cast = forms.TextField(max_length =300)
    review = forms.TextField(max_length=300)

    class Meta:
    	model = Data
    	fields = ('name' , 'cast' , 'review',)

