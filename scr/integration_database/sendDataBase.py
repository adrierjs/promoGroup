from collections import OrderedDict

from scr.integration_zoom_buscape.dataProcess import DataConverter
from scr.integration_database.connectionDataBase import cursor, conn
import re
import json
links = ["https://www.zoom.com.br/celular"]


for link in links:
    match = re.search(r'www\.(.*?)\.com', link)
    if match:
        domain = match.group(1)
        dataConverter = DataConverter(link, domain)
        retorno = dataConverter.namePriceOffer()
        print(retorno)
        ordered_data = [OrderedDict(sorted(item.items())) for item in retorno]
        dataJson = json.dumps(ordered_data, ensure_ascii=False)
        #
        # # Execute a inserção na tabela data_scraping
        cursor.execute("INSERT INTO data_scraping (dados_json) VALUES (%s);", (dataJson,))
        #
        # cursor.close()
        # conn.commit()

