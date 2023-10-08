import requests
from dotenv import load_dotenv
import os
load_dotenv()

class IntegrationWithPexelsApi:
    def __init__(self):
        self.__pexels_key = os.getenv("PEXELS_KEY")

    def connectionPexelsAPI(self, query):
        url = f"https://pixabay.com/api/"
        params = {
            'key': self.__pexels_key,
            'q': query,
            'per_page': 3
        }
        try:
            response = requests.request("GET", url, params=params)
            response.raise_for_status()
            return response.text, response.status_code
        except requests.exceptions.RequestException as error:
            return (f'Error connecting to pexels-api: {error}'), None

<<<<<<< HEAD:scr/integration_pexels/integrationPexelsAPI.py
=======








>>>>>>> main:integration_pexels/integrationPexelsAPI.py
