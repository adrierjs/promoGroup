from flask import Blueprint, jsonify, make_response, g
from src.app.config.connectionDataBase import conn
import json

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/celular', methods=['GET'])
def getSmartphone():
    return fetch_product_data('celular')

@product_routes.route('/notebook', methods=['GET'])
def getNotebook():
    return fetch_product_data('notebook')

@product_routes.route('/geladeira', methods=['GET'])
def getGeladeira():
    return fetch_product_data('geladeira')

@product_routes.route('/tv', methods=['GET'])
def getTv():
    return fetch_product_data('tv')

@product_routes.route('/ar-condicionado', methods=['GET'])
def getArcondicionado():
    return fetch_product_data('ar')

@product_routes.route('/livros', methods=['GET'])
def getLivros():
    return fetch_product_data('livros')

@product_routes.before_request
def before_request():
    g.db_conn = conn.cursor()

@product_routes.after_request
def after_request(response):
    g.db_conn.close()
    return response

def fetch_product_data(category):
    sql_query = """
        SELECT jsonb_build_object(
            'name', elem->>'name',
            'price', elem->>'price',
            'domain', elem->>'domain',
            'srcImg', elem->>'srcImg',
            'category', elem->>'category',
            'productLink', elem->>'productLink'
        ) as result
        FROM data_scraping,
             LATERAL jsonb_array_elements(dados_json) AS elem
        WHERE dados_json @> %s
        ORDER BY created_at DESC
    """
    category_json = json.dumps([{"category": category}])
    g.db_conn.execute(sql_query, [category_json])
    result = g.db_conn.fetchall()
    if result:
        return jsonify(result[0][0])
    response = make_response('Not Found', 404)
    return response
