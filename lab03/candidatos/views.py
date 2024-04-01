from django.shortcuts import render
from .models import Candidato

def lista_candidatos(request):
    candidatos = Candidato.objects.all()
    return render(request, 'candidatos/lista_candidatos.html', {'candidatos': candidatos})
