from django.db import models

class ConfiguracoesNotificacoes(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    notificacoes_email = models.BooleanField(default=False)
    notificacoes_sms = models.BooleanField(default=False)
    # Adicione outros campos conforme necessário
