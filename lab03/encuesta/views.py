# views.py

from django.shortcuts import render, redirect
from django.http import Http404
from .models import Pregunta

def index(request):
    latest_question_list = Pregunta.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'encuesta/index.html', context)

def detalle(request, pregunta_id):
    try:
        pregunta = Pregunta.objects.get(pk=pregunta_id)
    except Pregunta.DoesNotExist:
        raise Http404("La pregunta no existe.")
    return render(request, 'encuesta/detalle.html', {'pregunta': pregunta})

def votar(request, pregunta_id):
    pregunta = Pregunta.objects.get(pk=pregunta_id)
    try:
        opcion_seleccionada = pregunta.opcion_set.get(pk=request.POST['opcion'])
    except (KeyError, Opcion.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'encuesta/detalle.html', {
            'pregunta': pregunta,
            'error_message': "No seleccionaste una opción válida.",
        })
    else:
        opcion_seleccionada.votos += 1
        opcion_seleccionada.save()
        return redirect('encuesta:detalle', pregunta_id=pregunta.id)
