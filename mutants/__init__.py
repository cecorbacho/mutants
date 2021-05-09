import os
from config import app_config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api


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

@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()



