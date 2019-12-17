from flask import Flask
from config import config 
from db import redis_client
# from db import db

app = Flask(__name__)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    redis_client.init_app(app)
    # with app.app_context():
    # db.create_all() #creats all table from model class 
    # attach routes and custom error pages here
    @app.route('/')
    def index():
        redis_client.set('bb','ccc')
    return app




    