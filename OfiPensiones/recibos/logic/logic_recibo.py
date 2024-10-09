from ..models import Recibo

def get_recibos():
    queryset = Recibo.objects.all().order_by('-fecha')[:10]
    return (queryset)

def create_recibo(form):
    recibo = form.save()
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