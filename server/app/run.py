#!/usr/bin/env python
# coding=utf-8



from flask import Flask
from app.database import DB
from flask_cors import CORS, cross_origin

def create_app(config):
    app = Flask(__name__)
    CORS(app)
    DB.init()
    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)



