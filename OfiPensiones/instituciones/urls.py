from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
urlpatterns = [
    path('instituciones/', views.institucion_list, name='institucionList'),
    path('institucioncreate/', csrf_exempt(views.institucion_create), name='institucionCreate'),
]