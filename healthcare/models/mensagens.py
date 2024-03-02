from django.db import models

class Mensagem(models.Model):
    remetente = models.ForeignKey(Usuario, related_name='mensagens_enviadas', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(Usuario, related_name='mensagens_recebidas', on_delete=models.CASCADE)
    assunto = models.CharField(max_length=200)
    corpo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    # Adicione outros campos conforme necessário
