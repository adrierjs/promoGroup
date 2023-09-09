from integration_pexels.integrationPexelsAPI import IntegrationWithPexelsApi
from dataProcess import DataConverter
from integrationSite import dataSite
import dotenv
import os



dataConverter = DataConverter(dataSite)
products = dataConverter.namePriceOffer()
dotenv.load_dotenv()
PEXELS_KEY = os.getenv("PEXELS_KEY")
query = "Samsung Galaxy S20 FE"
integrator = IntegrationWithPexelsApi("https://api.pexels.com/v1/", PEXELS_KEY=PEXELS_KEY)
responsePexelAPI = integrator.connectionPexelsAPI(query)
print(products)