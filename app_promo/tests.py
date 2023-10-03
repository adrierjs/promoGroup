from django.test import TestCase
from django.urls import reverse
from selenium import webdriver

class UrlTests(TestCase):
    def test_cadastro_url(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Página de Cadastro")

    def test_login_url(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Página de Login")

    def test_index_url(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Página Inicial")

    def test_notebook_url(self):
        response = self.client.get(reverse('notebook'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Página de categoria notebooks")
        
class FrontendTestCase(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_pagina_inicial(self):
        self.driver.get('http://127.0.0.1:8000/')
        self.assertIn('Home', self.driver.title)
