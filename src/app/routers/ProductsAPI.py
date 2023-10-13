from flask import Flask, jsonify, make_response
from src.app.config.connectionDataBase import conn
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/celular', methods=['GET'])
def getSmartphone():
    with conn.cursor() as cursor:
        sql_query = """
            SELECT dados_json
            FROM data_scraping
            WHERE EXISTS (
                SELECT 1
                FROM jsonb_array_elements(dados_json) AS elem
                WHERE elem->>'category' = 'celular'
            )
            ORDER BY created_at DESC
            LIMIT 1;
        """
        cursor.execute(sql_query)
        result = cursor.fetchall()
        if result:
            return jsonify(result[0][0])
        response = make_response('Not Found', 404)
        return response

@app.route('/notebook', methods=['GET'])
def getNotebook():
    with conn.cursor() as cursor:
        sql_query = """
                SELECT dados_json
                FROM data_scraping
                WHERE EXISTS (
                    SELECT 1
                    FROM jsonb_array_elements(dados_json) AS elem
                    WHERE elem->>'category' = 'notebook'
                )
                ORDER BY created_at DESC
                LIMIT 1;
            """
        cursor.execute(sql_query)
        result = cursor.fetchall()
        if result:
            return jsonify(result[0][0])
        response = make_response('Not Found', 404)
        return response

@app.route('/geladeira', methods=['GET'])
def getGeladeira():
    with conn.cursor() as cursor:
        sql_query = """
                    SELECT dados_json
                    FROM data_scraping
                    WHERE EXISTS (
                        SELECT 1
                        FROM jsonb_array_elements(dados_json) AS elem
                        WHERE elem->>'category' = 'geladeira'
                    )
                    ORDER BY created_at DESC
                    LIMIT 1;
                """
        cursor.execute(sql_query)
        result = cursor.fetchall()
        if result:
            return jsonify(result[0][0])
        response = make_response('Not Found', 404)
        return response



if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    app.run(host='0.0.0.0', port=5000)

