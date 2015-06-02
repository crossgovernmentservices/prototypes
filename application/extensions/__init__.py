# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = "public.login"

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_migrate import Migrate
migrate = Migrate()

from flask_cache import Cache
cache = Cache()

from .asset_locator import AssetLocator
asset_locator = AssetLocator()

from flask_basicauth import BasicAuth
basic_auth = BasicAuth()
