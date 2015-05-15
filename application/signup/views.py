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

@blueprint.route('/googlelogin')
def googlelogin():
    return render_template("googlelogin.html")

@blueprint.route('/basicprofile')
def basicprofile():
    return render_template("basicprofile.html", activeTab="you")

@blueprint.route('/basicprofile_jobs')
def basicprofile_jobs():
    return render_template("basicprofile_jobs.html", activeTab="jobs")
