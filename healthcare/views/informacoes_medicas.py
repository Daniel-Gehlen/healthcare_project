from django.shortcuts import render
from .models import InformacoesMedicas

def listar_informacoes_medicas(request):
    informacoes = InformacoesMedicas.objects.all()
    return render(request, 'informacoes_medicas/listar_informacoes_medicas.html', {'informacoes': informacoes})

def detalhes_informacao_medica(request, informacao_id):
    informacao = InformacoesMedicas.objects.get(pk=informacao_id)
    return render(request, 'informacoes_medicas/detalhes_informacao_medica.html', {'informacao': informacao})
