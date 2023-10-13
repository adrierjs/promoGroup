# routes.py

from flask import Blueprint, jsonify, make_response
from src.app.config.connectionDataBase import conn

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

def fetch_product_data(category):
    with conn.cursor() as cursor:
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
