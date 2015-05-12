# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
)
import json


blueprint = Blueprint(
    'jobs',
    __name__,
    url_prefix='/jobs',
    static_folder='static',
    template_folder='templates')


@blueprint.route('/search_by_skill')
def search_by_skill():
    with open('/code/application/data/listings.json') as data_file:
        listings = json.load(data_file)
    return render_template('search_by_skill.html', listings=listings)


@blueprint.route('/your_apps')
def your_apps():
    return render_template('your_apps.html')


@blueprint.route('/description_developer')
def description_developer():
    with open('/code/application/data/dev_jd.json') as data_file:
        job_description = json.load(data_file)
    return render_template('description.html', jd=job_description)


@blueprint.route('/description_policy')
def description_policy():
    with open('/code/application/data/policy_jd.json') as data_file:
        job_description = json.load(data_file)
    return render_template('description.html', jd=job_description)
