from django.http import HttpResponse
from django.shortcuts import render

from .models import Preguntas

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")

def preguntas(request):
    preguntas = Preguntas.objects.all()
    context = {'preguntas': preguntas}
    return render(request, 'preguntas.html', context)
