from flask import Flask, jsonify
from scr.integrationSite import IntegrationWithWebSite
from scr.integration_zoom_buscape.dataProcess import DataConverter

app = Flask(__name__)

@app.route('/api/celular', methods=['GET'])
def getCelular():
    integration = IntegrationWithWebSite("https://www.zoom.com.br/celular")
    dataSite, statusCode = integration.websiteConnection()
    dataConverter = DataConverter(dataSite)
    retorno = (dataConverter.namePriceOffer())

    return jsonify(retorno)

@app.route('/api/tv', methods=['GET'])
def getNotebook():
    integration = IntegrationWithWebSite("https://www.zoom.com.br/tv")
    dataSite, statusCode = integration.websiteConnection()
    dataConverter = DataConverter(dataSite)
    retorno = (dataConverter.namePriceOffer())

    return jsonify(retorno)

@app.route('/api/ar-condicionado', methods=['GET'])
def getArcondicionado():
    integration = IntegrationWithWebSite("https://www.zoom.com.br/ar-condicionado")
    dataSite, statusCode = integration.websiteConnection()
    dataConverter = DataConverter(dataSite)
    retorno = (dataConverter.namePriceOffer())

    return jsonify(retorno)
if __name__ == '__main__':
    # Por padrão, o Flask executará na porta 5000
    app.run(host='127.0.0.1', port=8080)

