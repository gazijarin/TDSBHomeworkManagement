#!/usr/bin/env python
# coding=utf-8



from flask import Flask
from app.database import DB
from flask_cors import CORS, cross_origin
from flask.json import JSONEncoder
from datetime import date

# https://stackoverflow.com/questions/43663552/keep-a-datetime-date-in-yyyy-mm-dd-format-when-using-flasks-jsonify
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

def create_app(config):
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder
    CORS(app)
    DB.init()
    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)



