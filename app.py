# -*- coding: utf-8 -*-
from flask import Flask
from configurations import app_config, app_active

from database.db import connect_database

from routes.user_router import create_user_routes
from routes.admin_router import create_admin_routes

config = app_config[app_active]

dbConnection = connect_database()

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('configurations.py')

    create_admin_routes(app)
    create_user_routes(app)

    return app