from django.shortcuts import render
from .models import Consulta

def listar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/listar_consultas.html', {'consultas': consultas})

def detalhes_consulta(request, consulta_id):
    consulta = Consulta.objects.get(pk=consulta_id)
    return render(request, 'consultas/detalhes_consulta.html', {'consulta': consulta})
