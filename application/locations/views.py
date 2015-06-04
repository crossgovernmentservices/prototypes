from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
)
import json
import os
from application.services.people import People
from flask_login import login_required, current_user


people = People()

blueprint = Blueprint(
    'locations',
    __name__,
    url_prefix='/locations',
    static_folder='static',
    template_folder='templates')


@blueprint.route('/find')
def find():
    return render_template('find.html')

@blueprint.route('/my/office/<address>')
@login_required
def my_office(address):
    loc = {
        'locations': {
            'office': {
                'address': address,
                'url': 'http://%s/location/%s' % (os.environ.get('LOCATIONS_FRONTEND'), address)
            }
        }
    }
    response = people.update_profile(current_user.email, loc)
    return redirect(url_for('signup.basicprofile'))
