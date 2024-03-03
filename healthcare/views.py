from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'base.html')

def listar_usuarios(request):
    # Lógica para listar usuários
    return render(request, 'usuarios/listar_usuarios.html')

def detalhes_usuarios(request, pk):
    # Lógica para exibir detalhes de um usuário específico com id 'pk'
    return render(request, 'usuarios/detalhes_usuarios.html', {'pk': pk})

def listar_consultas(request):
    # Lógica para listar consultas
    return render(request, 'consultas/listar_consultas.html')

def detalhes_consultas(request, pk):
    consulta = Consulta.objects.first()  # Obtenha a primeira consulta do banco de dados
    return render(request, 'meu_template.html', {'consulta': consulta})

def listar_informacoes_medicas(request):
    # Lógica para listar informações médicas
    return render(request, 'informacoes_medicas/listar_informacoes_medicas.html')

def detalhes_informacoes_medicas(request, pk):
    # Lógica para exibir detalhes de uma informação médica específica com id 'pk'
    return render(request, 'informacoes_medicas/detalhes_informacoes_medicas.html', {'pk': pk})

def listar_mensagens(request):
    # Lógica para listar mensagens
    return render(request, 'mensagens/listar_mensagens.html')

def detalhes_mensagens(request, pk):
    # Lógica para exibir detalhes de uma mensagem específica com id 'pk'
    return render(request, 'mensagens/detalhes_mensagens.html', {'pk': pk})

def listar_configuracoes(request):
    # Lógica para listar configurações
    return render(request, 'configuracoes/listar_configuracoes.html')

def detalhes_configuracoes(request, pk):
    # Lógica para exibir detalhes de uma configuração específica com id 'pk'
    return render(request, 'configuracoes/detalhes_configuracoes.html', {'pk': pk})

def listar_avaliacoes(request):
    # Lógica para listar avaliações
    return render(request, 'avaliacoes/listar_avaliacoes.html')

def detalhes_avaliacoes(request, pk):
    # Lógica para exibir detalhes de uma avaliação específica com id 'pk'
    return render(request, 'avaliacoes/detalhes_avaliacoes.html', {'pk': pk})

def listar_relatorios(request):
    # Lógica para listar relatórios
    return render(request, 'relatorios/listar_relatorios.html')

def detalhes_relatorios(request, pk):
    # Lógica para exibir detalhes de um relatório específico com id 'pk'
    return render(request, 'relatorios/detalhes_relatorios.html', {'pk': pk})
