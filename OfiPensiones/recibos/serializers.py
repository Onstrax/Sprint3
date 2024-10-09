from rest_framework import serializers
from . import models


class ReciboSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'institucion', 'fecha', 'valor', 'tipo', 'estado',)
        model = models.Recibo