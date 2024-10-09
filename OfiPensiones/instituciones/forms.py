from django import forms
from .models import Institucion

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = [
            'name',
        ]
        labels = {
            'name': 'Name',
        }