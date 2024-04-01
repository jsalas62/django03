from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_candidatos, name='lista_candidatos'),
]
