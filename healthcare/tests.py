from django.test import TestCase, Client
from .models import Usuario, Consulta, ConfiguracoesNotificacoes, Mensagem, Relatorio, InformacoesMedicas, AvaliacaoAtendimento
from .forms import CadastroUsuarioForm
from django.urls import reverse


class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(nome="Teste", email="teste@example.com", senha="senha123")

    def test_usuario_criado(self):
        usuario = Usuario.objects.get(nome="Teste")
        self.assertEqual(usuario.email, "teste@example.com")

class ConsultaTestCase(TestCase):
    def setUp(self):
        usuario = Usuario.objects.create(nome="Teste", email="teste@example.com", senha="senha123")
        Consulta.objects.create(paciente=usuario, data_consulta="2024-03-02")

    def test_consulta_criada(self):
        consulta = Consulta.objects.get(data_consulta="2024-03-02")
        self.assertEqual(consulta.paciente.email, "teste@example.com")

class ConfiguracoesNotificacoesTestCase(TestCase):
    def setUp(self):
        usuario = Usuario.objects.create(nome="Teste", email="teste@example.com", senha="senha123")
        ConfiguracoesNotificacoes.objects.create(usuario=usuario, notificacoes_email=True, notificacoes_sms=False)

    def test_configuracoes_notificacoes_criadas(self):
        configuracoes = ConfiguracoesNotificacoes.objects.get(notificacoes_email=True)
        self.assertEqual(configuracoes.usuario.email, "teste@example.com")

# Adicione os outros testes para os modelos restantes seguindo a mesma estrutura
class FormularioTestCase(TestCase):
    def test_formulario_valido(self):
        form_data = {'nome': 'Teste', 'email': 'teste@example.com', 'senha': 'senha123'}
        form = CadastroUsuarioForm(data=form_data)
        self.assertTrue(form.is_valid())
        
        
class MinhaVisualizacaoTestCase(TestCase):
    def test_visualizacao_requisicao(self):
        client = Client()
        response = client.get(reverse('minha_visualizacao'))
        self.assertEqual(response.status_code, 200)