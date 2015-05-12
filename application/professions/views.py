# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
)
import json


blueprint = Blueprint(
    'professions',
    __name__,
    url_prefix='/professions',
    static_folder='static',
    template_folder='templates')


@blueprint.route('/hub')
def hub():
    with open('/code/application/data/professions_listings.json') as data_file:
        listings = json.load(data_file)
    return render_template('hub.html', listings=listings)
