from ..logic.institucion_logic import get_institucion_by_name, create_institucion

# this function return variable id. If the variable does not exist, then it is created


def get_institucion(name):
    institucion = get_institucion_by_name(name)
    if institucion != None:
        return (institucion)
    else:
        institucion = create_institucion(name)
        return (institucion)
