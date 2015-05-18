from flask import (
    Blueprint,
    render_template,
)
import json


blueprint = Blueprint(
    'being_a_civil_servant',
    __name__,
    url_prefix='/being_a_civil_servant',
    static_folder='static',
    template_folder='templates')


@blueprint.route('/addreceipt')
def hello():
    return render_template('addreceipt.html')

@blueprint.route('/expenses_data_request')
def expense_data():
    return render_template('expenses_data_request.html')
