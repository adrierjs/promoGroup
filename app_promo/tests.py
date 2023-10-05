from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class ViewTestCase(TestCase):
    def test_cadastro_url(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro.html')

    def test_login_url(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_notebook_url(self):
        response = self.client.get(reverse('notebook'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notebook.html')

    def test_redefinir_email_url(self):
        response = self.client.get(reverse('redefinir_email'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redefinir_email.html')

    def test_contato_url(self):
        response = self.client.get(reverse('contato'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contato.html')

class CadastroViewTest(TestCase):
    def test_cadastro_com_sucesso(self):
        data = {
            'email': 'ronildo@gmail.com',
            'nome': 'Ronildo',
            'password': 'Ronildo'
        }

        response = self.client.post(reverse('cadastro'), data)

        self.assertRedirects(response, reverse('index'))

        self.assertTrue(User.objects.filter(username='ronildo@gmail.com').exists())

        messages = [m.message for m in get_messages(response.wsgi_request)]

    def test_cadastro_com_email_existente(self):
        User.objects.create_user(username='ronildolima@gmail.com', email='ronildolima@gmail.com', password='ronildo123')

        data = {
            'email': 'ronildolima@gmail.com',
            'nome': 'Ronildo',
            'password': 'ronildo'
        }

        response = self.client.post(reverse('cadastro'), data)

        self.assertTemplateUsed(response, 'cadastro.html')

        messages = [m.message for m in get_messages(response.wsgi_request)]


class LoginViewTest(TestCase):
    def test_login_com_sucesso(self):
        user = User.objects.create_user(username='ronildo', password='ronildo')

        data = {
            'email': 'ronildo',
            'password': 'ronildo'
        }

        response = self.client.post(reverse('login'), data)

        self.assertRedirects(response, reverse('index'))

        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_com_credenciais_invalidas(self):
        data = {
            'email': 'ronildolima123',
            'password': 'ronildo12333'
        }

        response = self.client.post(reverse('login'), data)

        self.assertTemplateUsed(response, 'login.html')

        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Usuário ou senha inválidos', messages)

class IndexViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ronildo', password='ronildo123')

    def test_acesso_sem_autenticacao(self):
        response = self.client.get(reverse('index'))

        self.assertRedirects(response, reverse('login') + '?next=' + reverse('index'))

    def test_acesso_autenticado(self):
        self.client.login(username='ronildo', password='ronildo123')

        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context['user'], self.user)

        self.assertTemplateUsed(response, 'index.html')