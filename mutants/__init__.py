import os
from config import app_config
from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

app = Flask(__name__)
#Api Resources / Marshmallow serialization for SQLAlchemy
api = Api(app)
ma = Marshmallow(app)

if os.getenv('FLASK_ENV') == None:
    os.environ["FLASK_ENV"] = "dev"

#DB init
config_name = os.getenv('FLASK_ENV')
app.config.from_object(app_config[config_name])
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)

from mutants.routes import human_dna_check_routes, stats_routes
from mutants.models import *
db.create_all()



swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name':'Mutants'
    }
)
app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)


@app.route("/")
def hello_world():
    return make_response(jsonify("Mutants Test Service"),200)



