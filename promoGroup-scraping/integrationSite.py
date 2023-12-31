import requests


class IntegrationWithWebSite:
    def __init__(self, site):
        self._site = site

    def websiteConnection(self):
        try:
            response = requests.get(self._site)
            response.raise_for_status()
            return response.text

        except requests.exceptions.RequestException as error:

            raise f'Erro {error}'


integration = IntegrationWithWebSite("https://www.zoom.com.br/celular")
dataSite = integration.websiteConnection()
