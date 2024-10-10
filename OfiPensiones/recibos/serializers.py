from rest_framework import serializers
from . import models


class ReciboSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('numero', 'institucion', 'fecha', 'valor', 'tipo', 'estado',)
        model = models.Recibo