from ..models import Recibo
from utils.utils import AESCipher

def get_recibos():
    queryset = Recibo.objects.all().order_by('-fecha')[:10]
    cipher = AESCipher("Esto es una llave arbitraria 32B")
    for recibo in queryset:
        recibo.valor = cipher.decrypt(recibo.valor)
    return queryset

def create_recibo(form):
    cipher = AESCipher("Esto es una llave arbitraria 32B")
    recibo = form.save()
    recibo.valor = cipher.encrypt(recibo.valor)
    recibo.save()
    return ()

def create_recibo_object(institucion_id, valor, tipo, estado):
    recibo = Recibo()
    recibo.institucion = institucion_id
    recibo.valor = valor
    recibo.tipo = tipo
    recibo.estado = estado
    recibo.save()
    return ()