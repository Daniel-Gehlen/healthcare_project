from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/<int:pk>/', views.detalhes_usuarios, name='detalhes_usuarios'),
    path('consultas/', views.listar_consultas, name='listar_consultas'),
    path('consultas/<int:pk>/', views.detalhes_consultas, name='detalhes_consultas'),
    path('informacoes_medicas/', views.listar_informacoes_medicas, name='listar_informacoes_medicas'),
    path('informacoes_medicas/<int:pk>/', views.detalhes_informacoes_medicas, name='detalhes_informacoes_medicas'),
    path('mensagens/', views.listar_mensagens, name='listar_mensagens'),
    path('mensagens/<int:pk>/', views.detalhes_mensagens, name='detalhes_mensagens'),
    path('configuracoes/', views.listar_configuracoes, name='listar_configuracoes'),
    path('configuracoes/<int:pk>/', views.detalhes_configuracoes, name='detalhes_configuracoes'),
    path('avaliacoes/', views.listar_avaliacoes, name='listar_avaliacoes'),
    path('avaliacoes/<int:pk>/', views.detalhes_avaliacoes, name='detalhes_avaliacoes'),
    path('relatorios/', views.listar_relatorios, name='listar_relatorios'),
    path('relatorios/<int:pk>/', views.detalhes_relatorios, name='detalhes_relatorios'),
    # Adicione mais rotas conforme necessário
]