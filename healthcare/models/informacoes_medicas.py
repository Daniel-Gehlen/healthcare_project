from django.db import models

class InformacoesMedicas(models.Model):
    paciente = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    # Adicione outros campos conforme necessário
