from django.db import models

    
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário
    
    
class Consulta(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_consulta = models.DateField()
    # Adicione outros campos conforme necessário
    
    
class ConfiguracoesNotificacoes(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    notificacoes_email = models.BooleanField(default=False)
    notificacoes_sms = models.BooleanField(default=False)
    # Adicione outros campos conforme necessário
    
   
class Mensagem(models.Model):
    remetente = models.ForeignKey(Usuario, related_name='mensagens_enviadas', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(Usuario, related_name='mensagens_recebidas', on_delete=models.CASCADE)
    assunto = models.CharField(max_length=200)
    corpo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    # Adicione outros campos conforme necessário
   
    
class Relatorio(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    # Adicione outros campos conforme necessário
    
    
class InformacoesMedicas(models.Model):
    paciente = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    # Adicione outros campos conforme necessário
    
    
class AvaliacaoAtendimento(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()
    # Adicione outros campos conforme necessário



