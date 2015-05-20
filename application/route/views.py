from flask import (
    Blueprint,
    render_template,
    redirect,
)
import json
from application.services.people import People

people = People()

blueprint = Blueprint(
    'route',
    __name__,
    url_prefix='/route',
    static_folder='static',
    template_folder='templates')

def get_service(name):
    with open('application/data/facts/services.json') as data_file:
      services = json.load(data_file)
    service = None
    for srv in services:
        if srv['id'] == name:
            service = srv
    return service

@blueprint.route('/services/<name>')
def services(name):
    return render_template('data_request.html', service=get_service(name))

@blueprint.route('/services/<name>/<action>')
def services_grant_or_deny(name, action):
    email = 'juan.uys@digital.cabinet-office.gov.uk'
    if action == 'grant':
        access = True
    else:
        access = False
    payload = {
        'has_access': access,
        'data': {
            'name': name
        }
    }
    people.create_service(email, payload)
    if access:
        return redirect(get_service(name)['redirect'])
    else:
        return redirect('/signup/csprofile')
