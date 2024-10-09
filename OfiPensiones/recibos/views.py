from django.shortcuts import render
from .forms import ReciboForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_recibo import create_recibo, get_recibos

def recibo_list(request):
    recibos = get_recibos()
    context = {
        'measurement_list': recibos
    }
    return render(request, 'Recibo/recibos.html', context)

def recibo_create(request):
    if request.method == 'POST':
        form = ReciboForm(request.POST)
        if form.is_valid():
            create_recibo(form)
            messages.add_message(request, messages.SUCCESS, 'Recibo create successful')
            return HttpResponseRedirect(reverse('reciboCreate'))
        else:
            print(form.errors)
    else:
        form = ReciboForm()

    context = {
        'form': form,
    }

    return render(request, 'Recibo/reciboCreate.html', context)