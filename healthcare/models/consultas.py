from django.db import models

class Consulta(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_consulta = models.DateField()
    # Adicione outros campos conforme necessário
