import requests
from dotenv import load_dotenv
import os
load_dotenv()

class IntegrationWithPexelsApi:
    def __init__(self):
        self.__pexels_key = os.getenv("PEXELS_KEY")

    def connectionPexelsAPI(self, query):
        url = f"https://api.pexels.com/v1/search?query={query}&per_page=1&locale=pt-BR"
        payload = {}
        headers = {
            'Authorization': self.__pexels_key,
        }
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            response.raise_for_status()
            return response.text, response.status_code
        except requests.exceptions.RequestException as error:
            return (f'Error connecting to pexels-api: {error}'), None

c1 = IntegrationWithPexelsApi()

print(type((c1.connectionPexelsAPI('Teste'))))


