from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

from django.test import LiveServerTestCase
from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys

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

# TESTES E2E
class MyE2ETest(LiveServerTestCase):
    def setUp(self):
        self.driver = Edge(executable_path='/promogroup-front/app_promo/msedgedriver')

    def tearDown(self):
        self.driver.quit()

    def test_abrir_site(self):
        self.driver.get(self.live_server_url)

        self.assertIn("PromoGroup", self.driver.title)

    def test_pesquisa(self):
        self.driver.get(self.live_server_url)

        search_input = self.driver.find_element_by_id("product-input")
        search_input.send_keys("Smartphones")
        search_input.submit()

        self.assertIn("Smartphones", self.driver.page_source)

    def test_prencher_formulario(self):
        self.driver.get(self.live_server_url)

        self.driver.find_element_by_id("name").send_keys("Ronildo")
        self.driver.find_element_by_id("email").send_keys("ronildo@gmail.com")
        self.driver.find_element_by_id("password").send_keys("ronildo123")
        self.driver.find_element_by_id("pass2").send_keys("ronildo123")

        self.driver.find_element_by_id("btn-submit").click()

        success_message = self.driver.find_element_by_class_name("uk-alert-success")
        self.assertTrue(success_message.is_displayed())
