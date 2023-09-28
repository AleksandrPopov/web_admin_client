from django import forms
from .models import *


class AddAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'street', 'house']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'City'}),
            'street': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Street'}),
            'house': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'House'})
        }
