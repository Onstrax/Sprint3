from django.db import models
from instituciones.models import Institucion

class Recibo(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    valor = models.CharField(max_length=512)
    tipo = models.CharField(max_length=100, choices=[('Cobro', 'Cobro'), ('Pago', 'Pago')])
    estado = models.CharField(max_length=100, choices=[('Generado', 'Generado'), ('Pagado', 'Pagado')])
    
    def __str__(self):
        return '%s %s %s' % (self.valor, self.tipo, self.estado)
