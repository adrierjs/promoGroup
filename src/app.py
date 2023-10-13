import os
from flask import Flask
from src.app.routers.routes import product_routes

app = Flask(__name__)

app.register_blueprint(product_routes)

if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    app.run(host='0.0.0.0', port=5000)
