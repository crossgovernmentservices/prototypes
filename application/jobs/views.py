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
def jobs_search_by_skill():
    with open('/code/application/data/listings.json') as data_file:
        listings = json.load(data_file)
    return render_template('search_by_skill.html', listings=listings)


@blueprint.route('/your_apps')
def jobs_your_apps():
    return render_template('your_apps.html')
