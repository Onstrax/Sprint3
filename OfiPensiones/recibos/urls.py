from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('recibos/', views.recibo_list),
    path('recibocreate/', csrf_exempt(views.recibo_create), name='reciboCreate'),
]