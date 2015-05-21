from flask import (
    Blueprint,
    jsonify,
    request
)
from application.services.people import People


people = People()

blueprint = Blueprint(
    'profile',
    __name__,
    url_prefix='/profile')


@blueprint.route('/name', methods=['POST'])
def name():
    name = request.get_json()['name']
    people.change_name(name)
    return jsonify({'msg': 'OK'}), 200
