from flask import (
    Blueprint,
    render_template,
)
import json


blueprint = Blueprint(
    'prejoining',
    __name__,
    url_prefix='/prejoining',
    static_folder='static',
    template_folder='templates')


@blueprint.route('/pass_data')
def pass_data():
    return render_template('pass_data.html')
