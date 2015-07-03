# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
)
from application.services.people import People
from flask_login import login_required, current_user


people = People()


blueprint = Blueprint(
    'profile',
    __name__,
    url_prefix='/profile',
    static_folder='static',
    template_folder='templates')


@blueprint.route('/', methods=['POST'])
@login_required
def profile():
    response = people.update_profile(current_user.email, request.get_json())
    return jsonify({'msg': 'see status code'}), response.status_code

@blueprint.route('/magic')
@blueprint.route('/magic/<action>')
@login_required
def magic(action=None):
    session = {
        'email': current_user.email
    }
    if action:
        if action == 'reset':
            people.create_default_profile(current_user.email)

    return render_template('magic.html', session=session)

@blueprint.route('/whoami')
@login_required
def whoami():
    return jsonify({'email': current_user.email}), 200

@blueprint.route('/print')
@login_required
def basicprofile():
    profile = people.read_profile(current_user.email)
    services, user_services, outstanding_services = people.read_service(current_user.email)

    complete_profile = {
      'profile': profile,
      'services': user_services
    }

    return jsonify(complete_profile), 200
