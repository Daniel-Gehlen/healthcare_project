from django.shortcuts import render
from .models import Mensagem

def listar_mensagens(request):
    mensagens = Mensagem.objects.all()
    return render(request, 'mensagens/listar_mensagens.html', {'mensagens': mensagens})

def detalhes_mensagem(request, mensagem_id):
    mensagem = Mensagem.objects.get(pk=mensagem_id)
    return render(request, 'mensagens/detalhes_mensagem.html', {'mensagem': mensagem})
