import os
from flask import Flask
import logging
from src.app.routers.routes import product_routes

app = Flask(__name__)

app.register_blueprint(product_routes)
log_filename = 'app_logs.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s [%(levelname)s] - %(message)s')

if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    app.run(host='0.0.0.0', port=5000)