from django.contrib import admin
from .models import Usuario, Consulta, ConfiguracoesNotificacoes, Mensagem, Relatorio, InformacoesMedicas, AvaliacaoAtendimento

admin.site.register(Usuario)
admin.site.register(Consulta)
admin.site.register(ConfiguracoesNotificacoes)
admin.site.register(Mensagem)
admin.site.register(Relatorio)
admin.site.register(InformacoesMedicas)
admin.site.register(AvaliacaoAtendimento)
