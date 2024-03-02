from django.db import models

class Relatorio(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    # Adicione outros campos conforme necessário
