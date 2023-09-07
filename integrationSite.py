import undetected_chromedriver as uc
import time

class IntegrationWithApi:
    def __init__(self, site):
        self._site = site
        self._options = uc.ChromeOptions()

    def websiteConnection(self):
        try:
            self._options.headless = True
            _driver = uc.Chrome(use_subprocess=True, options=self._options)
            _driver.get(self._site)
            _driver.maximize_window()
            # time.sleep(50)
            _driver.save_screenshot("validation.png")
            _dataSite = _driver.page_source
        except Exception as erro:
            raise f'Erro {erro}'
        finally:
            _driver.close()
        return _dataSite

integration = IntegrationWithApi("https://www.zoom.com.br/celular")
dataSite = integration.websiteConnection()
