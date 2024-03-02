from django.db import models

class AvaliacaoAtendimento(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()
    # Adicione outros campos conforme necessário
