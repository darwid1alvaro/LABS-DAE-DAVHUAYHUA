from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Desde la visa de encuestas!</h1>")

def detalle(request, pregunta_id):
    return HttpResponse("Estas viendo la pregunta %s." % pregunta_id)

def resultados(request, pregunta_id):
    response = "Estas viendo los resultado de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def votar(request, pregunta_id):
    return HttpResponse("Estas votando por la pregunta %s." % pregunta_id)

def app(request, num1, num2, operacion):
    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
    elif operacion == 'division':
        resultado = num1 / num2
    else:
        resultado = 'Operación no válida'
    
    response = "El resultado de la %s es %s."
    return HttpResponse(response % (operacion, resultado))
# Create your views here.
