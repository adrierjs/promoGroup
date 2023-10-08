import json
from integration_pexels.integrationPexelsAPI import IntegrationWithPexelsApi
import dotenv
import os
import time

class SearchSrcImg:
    def __init__(self):
        self.__integrator = IntegrationWithPexelsApi()


    def integrationAPIPexel(self, query):
        responsePexelAPI, status_code = self.__integrator.connectionPexelsAPI(query)
        if status_code == 200:
            data = json.loads(responsePexelAPI)
            if data['total'] == 0:
                return None
            data = (data['hits'][0])
            return data.get('webformatURL', '')

        else:
            raise Exception(f"Erro na integração com a API Pexels. Código de status: {status_code}")
        return None


<<<<<<<< HEAD:scr/integration_zoom_buscape/integrationPexelAPIWithZoom.py
========




>>>>>>>> main:integration_zoom/integrationPexelAPIWithZoom.py
