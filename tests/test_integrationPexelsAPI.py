import unittest
from scr.integration_pexels.integrationPexelsAPI import IntegrationWithPexelsApi

class TestIntegrationPexelsAPI(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.query = 'Iphone 13 pro max'
        self.api = IntegrationWithPexelsApi()

    def test_connectionPexelsAPI(self):
        response, status_code = self.api.connectionPexelsAPI(query=self.query)

        self.assertEqual(status_code, 200)

    def test_responsePexelsAPI(self):
        response = self.api.connectionPexelsAPI(query=self.query)
        self.assertTrue(isinstance(response,tuple))

    def test_notResponsePexelsAPI(self):
        response, status_code = self.api.connectionPexelsAPI(query=self.query)
        if isinstance(response, str):
            self.assertEqual(status_code, 200)
        else:
            self.fail(f'return is not str, type found: {type(response)}')

if __name__ == '__main__':
    unittest.main()
