#!/usr/bin/env python
# coding=utf-8



from flask import Flask
from app.database import DB


def create_app(config):
    app = Flask(__name__)
    DB.init()
    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
