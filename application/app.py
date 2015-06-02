# -*- coding: utf-8 -*-
'''The app module, containing the app factory function.'''
from flask import (
    Flask,
)

from application.settings import ProdConfig
from application.assets import assets
from application.extensions import (
    bcrypt,
    cache,
    db,
    login_manager,
    migrate,
    asset_locator,
    basic_auth,
)
from application import (
    profile,
    auth,
    route,
    being_a_civil_servant,
    prejoining,
    public,
    jobs,
    professions,
    signup,
)


def create_app(config_object=ProdConfig):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    assets.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    asset_locator.init_app(app)
    basic_auth.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(profile.views.blueprint)
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(route.views.blueprint)
    app.register_blueprint(being_a_civil_servant.views.blueprint)
    app.register_blueprint(prejoining.views.blueprint)
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(jobs.views.blueprint)
    app.register_blueprint(professions.views.blueprint)
    app.register_blueprint(signup.views.blueprint)
    return None
