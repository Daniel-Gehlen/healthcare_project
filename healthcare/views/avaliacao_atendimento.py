from django.shortcuts import render
from .models import AvaliacaoAtendimento

def listar_avaliacoes(request):
    avaliacoes = AvaliacaoAtendimento.objects.all()
    return render(request, 'avaliacao_atendimento/listar_avaliacoes.html', {'avaliacoes': avaliacoes})

def detalhes_avaliacao(request, avaliacao_id):
    avaliacao = AvaliacaoAtendimento.objects.get(pk=avaliacao_id)
    return render(request, 'avaliacao_atendimento/detalhes_avaliacao.html', {'avaliacao': avaliacao})
