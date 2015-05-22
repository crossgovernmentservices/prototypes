# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    g,
)
from application.services.people import People


people = People()


blueprint = Blueprint(
    'profile',
    __name__,
    url_prefix='/profile',
    static_folder='static',
    template_folder='templates')


@blueprint.route('/', methods=['POST'])
def profile():
    response = people.update_profile(**request.form)
    return jsonify({'msg': 'see status code'}), response.status_code

@blueprint.route('/magic')
@blueprint.route('/magic/<action>')
def magic(action=None):
    session = {
        'email': g.email
    }
    if action:
        if action == 'reset':
            people.create_default_profile()

    return render_template('magic.html', session=session)

@blueprint.route('/whoami')
def whoami():
    return jsonify({'email': g.email}), 200

@blueprint.route('/print')
def basicprofile():
    profile = people.read_profile()

    return jsonify(profile), 200

