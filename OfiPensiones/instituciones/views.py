from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import InstitucionForm
from .logic.institucion_logic import get_instituciones, create_institucion

def institucion_list(request):
    instituciones = get_instituciones()
    context = {
        'institucion_list': instituciones
    }
    return render(request, 'Institucion/instituciones.html', context)

def institucion_create(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            create_institucion(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created institucion')
            return HttpResponseRedirect(reverse('institucionCreate'))
        else:
            print(form.errors)
    else:
        form = InstitucionForm()

    context = {
        'form': form,
    }
    return render(request, 'Institucion/institucionCreate.html', context)





# from .logic import instituciones_logic as vl
# from django.http import HttpResponse
# from django.core import serializers
# import json
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def instituciones_view(request):
#     if request.method == 'GET':
#         id = request.GET.get("id", None)
#         if id:
#             institucion_dto = vl.get_institucion(id)
#             institucion = serializers.serialize('json', [institucion_dto,])
#             return HttpResponse(institucion, 'application/json')
#         else:
#             instituciones_dto = vl.get_instituciones()
#             instituciones = serializers.serialize('json', instituciones_dto)
#             return HttpResponse(instituciones, 'application/json')

#     if request.method == 'POST':
#         institucion_dto = vl.create_institucion(json.loads(request.body))
#         institucion = serializers.serialize('json', [institucion_dto,])
#         return HttpResponse(institucion, 'application/json')

# @csrf_exempt
# def institucion_view(request, pk):
#     if request.method == 'GET':
#         institucion_dto = vl.get_institucion(pk)
#         institucion = serializers.serialize('json', [institucion_dto,])
#         return HttpResponse(institucion, 'application/json')

#     if request.method == 'PUT':
#         institucion_dto = vl.update_institucion(pk, json.loads(request.body))
#         institucion = serializers.serialize('json', [institucion_dto,])
#         return HttpResponse(institucion, 'application/json')
    
    
