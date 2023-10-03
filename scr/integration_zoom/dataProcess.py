from bs4 import BeautifulSoup
from scr.integrationSite import IntegrationWithWebSite
from integrationPexelAPIWithZoom import SearchSrcImg

class DataConverter:
    def __init__(self, dataSite):
        self._dataSite = dataSite
        self.__soup = BeautifulSoup(self._dataSite, 'html.parser')
        self.__elements_with_class = self.__soup.find_all(class_="ProductCard_ProductCard_Inner__tsD4M")

    def namePriceOffer(self):
        listProducts = []

        for elements in self.__elements_with_class:
            href = elements.get("href")
            productName = " ".join(elements.find('h2', {'data-testid': 'product-card::name'}).text.strip().split()[1:5])
            productPrice = elements.find('p', {'data-testid': 'product-card::price'}).text.strip()

            searchSrcImg = SearchSrcImg()
            responseQueryPexelsAP = searchSrcImg.integrationAPIPexel(query=productName)
            scrImg = None

            # if href and ('/celular' in href or '/tv' in href):

            fullLink = f"www.zoom.com.br{href}"
            if responseQueryPexelsAP:
                scrImg = responseQueryPexelsAP
            product = {"name": productName,
                       "price": productPrice,
                       "productLink": fullLink,
                       "src": scrImg
                       }

            listProducts.append(product)
            # else:
            #     print('oi')
            #     if responseQueryPexelsAP:
            #         scrImg = responseQueryPexelsAP
            #     product = {"name": productName,
            #                "price": productPrice,
            #                "productLink": fullLink,
            #                "src": scrImg
            #                }
            #     listProducts.append(product)

        return listProducts

links = ["https://www.zoom.com.br/celular","https://www.zoom.com.br/tv"]

for link in links:

    integration = IntegrationWithWebSite(link)
    dataSite, statusCode = integration.websiteConnection()
    dataConverter = DataConverter(dataSite)
    retorno = (dataConverter.namePriceOffer())
    print(retorno)

