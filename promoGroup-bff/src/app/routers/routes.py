# routes.py

from flask import Blueprint, jsonify, make_response, g
from src.app.config.connectionDataBase import conn

product_routes = Blueprint('product_routes', __name__)

@product_routes.before_request
def before_request():
    g.db_conn = conn.cursor()

@product_routes.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db_conn'):
        g.db_conn.close()

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

def fetch_product_data(category):
    cursor = g.db_conn
    sql_query = """
        SELECT dados_json
        FROM data_scraping
        WHERE EXISTS (
            SELECT 1
            FROM jsonb_array_elements(dados_json) AS elem
            WHERE elem->>'category' = %s
        )
        ORDER BY created_at DESC
        LIMIT 1;
    """
    cursor.execute(sql_query, (category,))
    result = cursor.fetchall()
    if result:
        return jsonify(result[0][0])
    response = make_response('Not Found', 404)
    return response
