from bs4 import BeautifulSoup
from scr.integrationSite import IntegrationWithWebSite
from scr.integration_zoom_buscape.integrationPexelAPIWithZoom import SearchSrcImg

class DataConverter:
    def __init__(self, link, domain):
        integration = IntegrationWithWebSite(link)
        self.__dataSite, statusCode = integration.websiteConnection()
        self.__soup = BeautifulSoup(self.__dataSite, 'html.parser')
        self.__elements_with_class = self.__soup.find_all(class_="ProductCard_ProductCard_Inner__tsD4M")
        self.__searchSrcImg = SearchSrcImg()
        self.__domain = domain

    def namePriceOffer(self):
        listProducts = []

        for elements in self.__elements_with_class:
            href = elements.get("href")
            productName = " ".join(elements.find('h2', {'data-testid': 'product-card::name'}).text.strip().split()[1:5])
            productPrice = elements.find('p', {'data-testid': 'product-card::price'}).text.strip()

            responseQueryPexelsAP = self.__searchSrcImg.integrationAPIPexel(query=productName)

            # if href and ('/celular' in href or '/tv' in href):

            scrImg = None
            fullLink = f"www.{self.__domain}.com.br{href}"
            # if responseQueryPexelsAP:
            #     scrImg = responseQueryPexelsAP
            # else:
            #     scrImg = None
            product = {"name": productName,
                       "price": productPrice,
                       "productLink": fullLink,
                       "src": scrImg,
                       "domain": self.__domain
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
