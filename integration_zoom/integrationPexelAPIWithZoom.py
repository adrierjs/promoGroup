import json
from integration_pexels.integrationPexelsAPI import IntegrationWithPexelsApi
import dotenv
import os
import time

class SearchSrcImg:
    def __init__(self):
        dotenv.load_dotenv()
        self.__pexels_key = os.getenv("PEXELS_KEY")

    def integrationAPIPexel(self, query):
        integrator = IntegrationWithPexelsApi("https://api.pexels.com/v1/", PEXELS_KEY=self.__pexels_key)

        responsePexelAPI, status_code = integrator.connectionPexelsAPI(query)
        if status_code == 200:
            data = json.loads(responsePexelAPI)
            data = (data['photos'][0])
            return data['src']['large']

        return None









