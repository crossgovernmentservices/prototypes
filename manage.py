#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from flask_script import Manager, Shell, Server
from flask_migrate import MigrateCommand

from application.app import create_app
from application.settings import DevConfig, ProdConfig
from application.database import db

if os.environ.get("APPLICATION_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

manager = Manager(app)

def _make_context():
    """Return context dict for a shell session so you can access
    app, db by default.
    """
    return {'app': app, 'db': db}

@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code

manager.add_command('server', Server(
    host='0.0.0.0', port=int(os.environ.get('PORT'))))
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
