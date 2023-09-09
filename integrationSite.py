import requests

class IntegrationWithApi:
    def __init__(self, site):
        self._site = site

    def websiteConnection(self):
        try:
            # Fazer uma solicitação GET para a página
            response = requests.get(self._site)

            # Verificar se a solicitação foi bem-sucedida (status code 200)
            if response.status_code == 200:
                _dataSite = response.text
            else:
                raise Exception(f'Solicitação falhou com status code {response.status_code}')
        except Exception as erro:
            raise f'Erro {erro}'
        return _dataSite

integration = IntegrationWithApi("https://www.zoom.com.br/celular")
dataSite = integration.websiteConnection()


