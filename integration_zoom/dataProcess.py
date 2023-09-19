from bs4 import BeautifulSoup
from integrationSite import dataSite
from integrationPexelAPIWithZoom import SearchSrcImg, IntegrationWithPexelsApi


class DataConverter:
    def __init__(self, dataSite):
        self._dataSite = dataSite
        self.__soup = BeautifulSoup(self._dataSite, 'html.parser')
        self.__elements_with_class = self.__soup.find_all(class_="ProductCard_ProductCard_Inner__tsD4M")

    def namePriceOffer(self):
        list_products = []

        for elements in self.__elements_with_class:
            href = elements.get("href")
            product_name = " ".join(elements.find('h2', {'data-testid': 'product-card::name'}).text.strip().split()[1:5])
            product_price = elements.find('p', {'data-testid': 'product-card::price'}).text.strip()

            searchSrcImg = SearchSrcImg()
            responseQueryPexelsAP = searchSrcImg.integrationAPIPexel(query=product_name)
            src_img = None
            if href and ("/celular" or '/tv') in href:

                full_link = f"www.zoom.com.br{href}"
                if responseQueryPexelsAP:
                    src_img = responseQueryPexelsAP
                product = {"name": product_name,
                           "price": product_price,
                           "product_link": full_link,
                           "src": src_img}

                list_products.append(product)
            else:
                if responseQueryPexelsAP:
                    src_img = responseQueryPexelsAP
                product = {"name": product_name,
                           "price": product_price,
                           "product_link": full_link,
                           "src": src_img
                           }
                list_products.append(product)

        return list_products


dataConverter = DataConverter(dataSite)
retorno = (dataConverter.namePriceOffer())
print(retorno)
