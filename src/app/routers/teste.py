from src.integration_site.integrationSite import IntegrationWithWebSite


integration = IntegrationWithWebSite("https://www.zoom.com.br/tv")
dataSite, statusCode = integration.websiteConnection()
dataConverter = DataConverter(dataSite)
retorno = (dataConverter.namePriceOffer())
print(retorno)

