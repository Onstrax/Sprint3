from django.db import models
from instituciones.models import Institucion

class Recibo(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, default=None)
    numero = models.IntegerField(null=False)
    fecha = models.DateField(auto_now=True, auto_now_add=False)
    valor = models.FloatField(null=False, blank=False, default=0)
    tipo = models.CharField(max_length=100, choices=[('Cobro', 'Cobro'), ('Pago', 'Pago')])
    estado = models.CharField(max_length=100, choices=[('Generado', 'Generado'), ('Pagado', 'Pagado')])
    
    def __str__(self):
        return '%s %s %s' % (self.valor, self.tipo, self.estado)
