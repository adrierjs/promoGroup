import unittest
from scr.integration_zoom.dataProcess import DataConverter
from scr.integrationSite import IntegrationWithWebSite
from scr.integration_zoom.integrationPexelAPIWithZoom import SearchSrcImg

class TestIntegrationPexelsAPI(unittest.TestCase):
    def __init__(self):
        self.integration = IntegrationWithWebSite('https://www.zoom.com.br/celular')



    def test_integrationWebSiteConnection(self):
        pass

if __name__ == '__main__':
    unittest.main()
