from django.shortcuts import render
from .models import Relatorio

def listar_relatorios(request):
    relatorios = Relatorio.objects.all()
    return render(request, 'relatorios/listar_relatorios.html', {'relatorios': relatorios})

def detalhes_relatorio(request, relatorio_id):
    relatorio = Relatorio.objects.get(pk=relatorio_id)
    return render(request, 'relatorios/detalhes_relatorio.html', {'relatorio': relatorio})
