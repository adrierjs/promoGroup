import json
from scr.integration_pexels.integrationPexelsAPI import IntegrationWithPexelsApi

class SearchSrcImg:
    def __init__(self):
        self.__integrator = IntegrationWithPexelsApi()

    def integrationAPIPexel(self, query):
        responsePexelAPI, status_code = self.__integrator.connectionPexelsAPI(query)
        if status_code == 200:
            data = json.loads(responsePexelAPI)
            data = (data['photos'][0])
            return data['src']['large']
        return None




