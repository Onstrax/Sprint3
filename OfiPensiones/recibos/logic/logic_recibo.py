from ..models import Recibo

def get_recibos():
    queryset = Recibo.objects.all().order_by('-fecha')[:10]
    return (queryset)

def create_recibo(form):
    recibo = form.save()
    recibo.save()
    return ()