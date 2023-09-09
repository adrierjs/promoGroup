import requests
class IntegrationWithPexelsApi:
    def __init__(self, site, PEXELS_KEY):
        self.__data = site
        self.__pexels_key = PEXELS_KEY

    def connectionPexelsAPI(self, query):
        url = f"https://api.pexels.com/v1/search?query={query}&per_page=1&locale=pt-BR"
        payload = {}
        headers = {
            'Authorization': self.__pexels_key,
        }
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as error:
            print(f'error connecting to pexels-api: {error}')



