from flask import (
    Blueprint,
    request,
)
from application.services.people import People


people = People()

blueprint = Blueprint(
    'auth',
    __name__,
    url_prefix='/')


@blueprint.route('prototype_set_user', methods=['POST'])
def prototype_set_user():
    email = request.form['email']
    people.create_user(email)
    return 'OK', 200 
