from ..models import Institucion


def get_instituciones():
    queryset = Institucion.objects.all()
    return (queryset)


def create_institucion(form):
    recibo = form.save()
    recibo.save()
    return ()


def get_institucion_by_name(name):
    try:
        institucion = Institucion.objects.get(name=name)
        return (institucion)
    except:
        institucion = None
        return (institucion)