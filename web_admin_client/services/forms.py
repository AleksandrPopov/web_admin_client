from django import forms
from .models import *


class AddServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'time', 'cost', 'categories_pk']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Service'}),
            'time': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Time'}),
            'cost': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Cost'})
        }