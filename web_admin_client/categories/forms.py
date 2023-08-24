from django import forms
from .models import *


class AddCategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Category'}),
        }
