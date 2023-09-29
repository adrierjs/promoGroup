import unittest
from scr.integrationSite import IntegrationWithWebSite

class TestIntegrationWithWebSite(unittest.TestCase):
    def setUp(self):
        self.site = IntegrationWithWebSite("https://www.zoom.com.br/celular")

    def test_website_connection_successful(self):
        response, status_code = self.site.websiteConnection()
        self.assertEqual(status_code, 200)

    def test_website_connection_failure(self):
        self.site = IntegrationWithWebSite("https://www.zoom.com.br/teste-falha")

        with self.assertRaises(Exception):
            self.site.websiteConnection()

    def test_ReponseWebSite(self):
        response, status_code = self.site.websiteConnection()
        if isinstance(response, str):
            self.assertEqual(status_code, 200)
        else:
            self.fail(f'return is not str, type found: {type(response)}')

if __name__ == '__main__':
    unittest.main()
