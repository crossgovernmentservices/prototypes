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

@blueprint.route('/csprofile')
def csprofile():
    return render_template("csprofile.html", CivilServant=True, activeTab="you")

@blueprint.route('/csprofile_services')
def csprofile_services():
    with open('/code/application/data/services.json') as data_file:
      services = json.load(data_file)
    return render_template("csprofile_services.html", CivilServant=True, activeTab="services", services=services)
