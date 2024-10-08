from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.instituciones_view, name='instituciones_view'),
    path('<int:pk>', views.institucion_view, name='institucion_view'),
]