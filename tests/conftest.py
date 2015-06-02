# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""
import pytest
from webtest import TestApp

from application.settings import TestConfig
from application.app import create_app


@pytest.yield_fixture(scope='function')
def app():
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()

@pytest.fixture(scope='session')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)
