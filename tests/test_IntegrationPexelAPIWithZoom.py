import unittest
from scr.integration_zoom_buscape.integrationPexelAPIWithZoom import SearchSrcImg

class TestIntegrationPexelsAPI(unittest.TestCase):
    def test_connectionPexelsAPI(self):
        c1 = SearchSrcImg()
        response = c1.integrationAPIPexel('iphone 13')
        self.assertTrue(isinstance(response, str))

    def test_not_connectionPexelsAPI(self):
        c1 = SearchSrcImg()
        response = c1.integrationAPIPexel('iphone 13')
        self.assertFalse(not isinstance(response, str))


if __name__ == '__main__':
    unittest.main()

