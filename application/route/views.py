from flask import (
    Blueprint,
    render_template,
    redirect,
)
import json
import datetime
from application.services.people import People

people = People()

blueprint = Blueprint(
    'route',
    __name__,
    url_prefix='/route',
    static_folder='static',
    template_folder='templates')

def get_service(service_id):
    with open('application/data/facts/services.json') as data_file:
      services = json.load(data_file)
    service = None
    for srv in services:
        if srv['id'] == service_id:
            service = srv
    return service

@blueprint.route('/services/<service_id>')
def services(service_id):
    return render_template('data_request.html', service=get_service(service_id))

@blueprint.route('/services/<service_id>/<action>')
def services_grant_or_deny(service_id, action):
    if action == 'grant':
        access = True
    else:
        access = False
    today = datetime.date.today()
    # TODO hide payload behind service
    payload = {
        'has_access': access,
        'data': {
            'id': service_id,
            'desc': get_service(service_id)['desc'],
            'approval_date': today.strftime('%a %d %b %Y'),
            'permissions': 'read and write'
        }
    }
    people.create_service(payload)
    if access:
        return redirect(get_service(service_id)['redirect'])
    else:
        return redirect('/signup/csprofile')
