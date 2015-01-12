import os
import datetime

import jinja2
import pymongo

from flask import Flask
from flask import g,request

from flask.ext.mongoengine import MongoEngine
from flask.ext.admin import Admin
from flask_wtf.csrf import CsrfProtect

import googleplus

app = None
admin = Admin()
db = MongoEngine()

BASE_DIRECTORY = os.path.realpath(os.path.join(os.path.dirname(__file__),os.path.pardir))

static_url_path = " "
_static_folder = BASE_DIRECTORY + '/colossus/static/'


def create_app(package_name='colossus', config_name='Development'):
    global app
    app = Flask(package_name, instance_relative_config=True)
    
    if os.environ.get('colossus_CONFIG_NAME') == 'Production':
        config_name = 'Production'

    app.config.from_object('configurations.%s' % config_name.title())

    app.jinja_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader('colossus/templates/'),
    ])
    import googleplus
    import facebooklogin
    from . import google 
    from . import facebook
    # from google import application
    # app.register_blueprint(application)
    # from googleplus import appss 
    # app.register_blueprint(appss)
    from facebook import face
    app.register_blueprint(face)
    from facebooklogin import apps
    app.register_blueprint(apps)
    return app

# def create_celery_app(app=None):
#     pass