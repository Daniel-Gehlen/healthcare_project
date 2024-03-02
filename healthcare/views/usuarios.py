from django.shortcuts import render
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

def detalhes_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    return render(request, 'usuarios/detalhes_usuario.html', {'usuario': usuario})
