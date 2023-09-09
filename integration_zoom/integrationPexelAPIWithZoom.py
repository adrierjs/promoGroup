import json
from integration_pexels.integrationPexelsAPI import IntegrationWithPexelsApi
import dotenv
import os

class SearchSrcImg:
    def __init__(self, dataSite):
        dotenv.load_dotenv()
        self.__dataSite = dataSite
        self.__pexels_key = os.getenv("PEXELS_KEY")

    def integrationAPIPexel(self, query):
        integrator = IntegrationWithPexelsApi("https://api.pexels.com/v1/", PEXELS_KEY=self.__pexels_key)
        responsePexelAPI = integrator.connectionPexelsAPI(query)
        retorno = responsePexelAPI

        data = json.loads(retorno)
        data = (data['photos'][0])
        return data['src']['large']












