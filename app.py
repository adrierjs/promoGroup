import os
from flask import Flask
import logging
from flask_cors import CORS
from src.app.routers.routes import product_routes

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(product_routes)
log_filename = 'app_logs.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s [%(levelname)s] - %(message)s')

def log_requests_to_console():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    log.addHandler(handler)


if __name__ == '__main__':
    log_requests_to_console()
    app.run(host='0.0.0.0', port=5000)
