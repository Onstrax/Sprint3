from ..models import Institucion
def get_instituciones():
    instituciones = Institucion.objects.all()
    return instituciones

def get_institucion(var_pk):
    institucion = Institucion.objects.get(pk=var_pk)
    return institucion

def update_institucion(var_pk, new_var):
    institucion = get_institucion(var_pk)
    institucion.name = new_var["name"]
    institucion.save()
    return institucion

def create_institucion(var):
    institucion = institucion(name=var["name"])
    institucion.save()
    return institucion