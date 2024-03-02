from django.shortcuts import render
from .models import ConfiguracoesNotificacoes

def listar_configuracoes(request):
    configuracoes = ConfiguracoesNotificacoes.objects.all()
    return render(request, 'configuracoes_notificacoes/listar_configuracoes.html', {'configuracoes': configuracoes})

def detalhes_configuracao(request, configuracao_id):
    configuracao = ConfiguracoesNotificacoes.objects.get(pk=configuracao_id)
    return render(request, 'configuracoes_notificacoes/detalhes_configuracao.html', {'configuracao': configuracao})
