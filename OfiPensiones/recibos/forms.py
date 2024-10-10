from django import forms
from .models import Recibo

class ReciboForm(forms.ModelForm):
    class Meta:
        model = Recibo
        fields = [
            'institucion',
            #'fecha',
            'valor',
            'tipo',
            'estado',
        ]

        labels = {
            'institucion' : 'Institucion',
            #'fecha' : 'Date',
            'valor' : 'Valor',
            'tipo' : 'Tipo',
            'estado' : 'Estado',
        }
