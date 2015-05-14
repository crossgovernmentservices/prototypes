# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
)
import json


blueprint = Blueprint(
    'signup',
    __name__,
    url_prefix='/signup',
    static_folder='static',
    template_folder='templates')


@blueprint.route('/create')
def create():
    return render_template("create.html")

@blueprint.route('/basic')
def basic():
    return render_template("basic.html")
