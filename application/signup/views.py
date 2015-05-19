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
    with open('/code/application/data/noncivilservant.json') as data_file:
      person = json.load(data_file)
    return render_template("basicprofile.html", activeTab="you", person=person)

@blueprint.route('/basicprofile/checklist')
def basicprofile_checklist():
    with open('/code/application/data/noncivilservant.json') as data_file:
      person = json.load(data_file)
    return render_template("basicprofile_checklist.html", activeTab="you", person=person)

@blueprint.route('/basicprofile_jobs')
def basicprofile_jobs():
    return render_template("basicprofile_jobs.html", activeTab="jobs", activeMenu="home")

@blueprint.route('/basicprofile_jobs/apps')
def basicprofile_jobs_apps():
    return render_template("basicprofile_jobs_apps.html", activeTab="jobs", activeMenu="apps")

@blueprint.route('/basicprofile_jobs/alerts')
def basicprofile_jobs_alerts():
    return render_template("basicprofile_jobs_alerts.html", activeTab="jobs", activeMenu="alerts")

@blueprint.route('/csprofile')
def csprofile():
    with open('/code/application/data/civilservant.json') as data_file:
      person = json.load(data_file)
    return render_template("csprofile.html", CivilServant=True, activeTab="you", person=person)

@blueprint.route('/csprofile_more')
def csprofile_more():
    with open('/code/application/data/civilservant.json') as data_file:
      person = json.load(data_file)
    return render_template("csprofile_more.html", CivilServant=True, activeTab="you", person=person)

@blueprint.route('/csprofile_learning')
def csprofile_learning():
    with open('/code/application/data/courses.json') as data_file:
      courses = json.load(data_file)
    return render_template("csprofile_learning.html", CivilServant=True, activeTab="learning", courses=courses)

# CS Profile - PERFORMANCE
@blueprint.route('/csprofile_perf')
def csprofile_perf():
    return render_template("csprofile_perf.html", CivilServant=True, activeTab="performance", activeMenu="home")

@blueprint.route('/csprofile_perf/objectives')
def csprofile_perf_obj():
    return render_template("csprofile_perf_obj.html", CivilServant=True, activeTab="performance", activeMenu="obj")

@blueprint.route('/csprofile_perf/history')
def csprofile_perf_history():
    return render_template("csprofile_perf_history.html", CivilServant=True, activeTab="performance", activeMenu="history")

@blueprint.route('/csprofile_perf/last')
def csprofile_perf_last():
    return render_template("csprofile_perf_last_review.html", CivilServant=True, activeTab="performance", activeMenu="last")

# CS Profile - JOBS
@blueprint.route('/csprofile_jobs')
def csprofile_jobs():
    return render_template("csprofile_jobs.html", CivilServant=True, activeTab="jobs", activeMenu="home")

@blueprint.route('/csprofile_jobs/alerts')
def csprofile_jobs_alerts():
    return render_template("csprofile_jobs_alerts.html", CivilServant=True, activeTab="jobs", activeMenu="alerts")

@blueprint.route('/csprofile_jobs/history')
def csprofile_jobs_history():
    return render_template("csprofile_jobs_history.html", CivilServant=True, activeTab="jobs", activeMenu="history")

@blueprint.route('/csprofile_jobs/apps')
def csprofile_jobs_apps():
    return render_template("csprofile_jobs_apps.html", CivilServant=True, activeTab="jobs", activeMenu="apps")

@blueprint.route('/csprofile_services')
def csprofile_services():
    with open('/code/application/data/services.json') as data_file:
      services = json.load(data_file)
    return render_template("csprofile_services.html", CivilServant=True, activeTab="services", services=services)
