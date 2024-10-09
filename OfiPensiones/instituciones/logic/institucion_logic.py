from ..models import Institucion

def get_instituciones():
    queryset = Institucion.objects.all()
    return (queryset)

def get_institucion(var_pk):
    institucion = Institucion.objects.get(pk=var_pk)
    return institucion

def update_institucion(var_pk, new_var):
    institucion = get_institucion(var_pk)
    institucion.name = new_var["name"]
    institucion.save()
    return institucion

def create_institucion(form):
    institucion = form.save()
    institucion.save()
    return ()

def get_institucion_by_name(name):
    try:
        institucion = Institucion.objects.get(name=name)
        return (institucion)
    except:
        institucion = None
        return (institucion)