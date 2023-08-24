from django import forms
from .models import *


class AddAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'street']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control p-0', 'placeholder': 'City'}),
            'street': forms.TextInput(attrs={'class': 'form-control p-0', 'placeholder': 'Street'})
        }