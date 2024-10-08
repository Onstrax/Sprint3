from .logic import instituciones_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def instituciones_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            institucion_dto = vl.get_institucion(id)
            institucion = serializers.serialize('json', [institucion_dto,])
            return HttpResponse(institucion, 'application/json')
        else:
            instituciones_dto = vl.get_instituciones()
            instituciones = serializers.serialize('json', instituciones_dto)
            return HttpResponse(instituciones, 'application/json')

    if request.method == 'POST':
        institucion_dto = vl.create_institucion(json.loads(request.body))
        institucion = serializers.serialize('json', [institucion_dto,])
        return HttpResponse(institucion, 'application/json')

@csrf_exempt
def institucion_view(request, pk):
    if request.method == 'GET':
        institucion_dto = vl.get_institucion(pk)
        institucion = serializers.serialize('json', [institucion_dto,])
        return HttpResponse(institucion, 'application/json')

    if request.method == 'PUT':
        institucion_dto = vl.update_institucion(pk, json.loads(request.body))
        institucion = serializers.serialize('json', [institucion_dto,])
        return HttpResponse(institucion, 'application/json')
    
    
