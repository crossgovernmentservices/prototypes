# -*- coding: utf-8 -*-
'''Public section, including homepage and signup.'''
from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    url_for,
    redirect,
)
from flask.ext.login import login_user, login_required, logout_user

from application.extensions import login_manager
from application.public.forms import LoginForm
from application.utils import flash_errors
from .model import User


blueprint = Blueprint(
    'public',
    __name__,
    static_folder='../static')

@login_manager.user_loader
def load_user(id):
    return User(id)

@blueprint.route('/')
def index():
    return render_template('public/home.html')

@blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", 'success')
            # TODO validate request.args.get("next")
            redirect_url = request.args.get("next") or \
                request.referrer or \
                url_for(".login")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/login.html", form=form)

@blueprint.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('.login'))
