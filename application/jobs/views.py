# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
)
import json


blueprint = Blueprint(
    'jobs',
    __name__,
    url_prefix='/jobs',
    static_folder='static',
    template_folder='templates')


@blueprint.route('/search_by_skill')
def search_by_skill():
    with open('/code/application/data/listings.json') as data_file:
        listings = json.load(data_file)
    return render_template('search_by_skill.html', listings=listings)


@blueprint.route('/your_apps')
def your_apps():
    return render_template('your_apps.html')


@blueprint.route('/description_developer')
def description_developer():
    with open('/code/application/data/dev_jd.json') as data_file:
        job_description = json.load(data_file)
    return render_template('description.html', jd=job_description)


@blueprint.route('/description_policy')
def description_policy():
    with open('/code/application/data/policy_jd.json') as data_file:
        job_description = json.load(data_file)
    return render_template('description.html', jd=job_description)


@blueprint.route('/description_general')
def description_general():
    with open('/code/application/data/general_jd.json') as data_file:
        job_description = json.load(data_file)
    return render_template('description.html', jd=job_description)


@blueprint.route('/review')
def review():
    with open('/code/application/data/review_skills.json') as data_file:
        skills = json.load(data_file)
    return render_template('review.html', skills=skills)


@blueprint.route('/review_summary')
def review_summary():
    return render_template('review_summary.html')


@blueprint.route('/to_review')
def to_review():
    with open('/code/application/data/review_team.json') as data_file:
        team = json.load(data_file)
    with open('/code/application/data/review_others.json') as data_file:
        others = json.load(data_file)
    return render_template('to_review.html', team=team, others=others)


@blueprint.route('/email_referred')
def email_referred():
    email = {
        'to': 'DavidDavids@gmail.com',
        'from': 'iamtherecruiter@gmail.com',
        'subject': 'Front-end dev role',
        'content': """
            <p>Hi David,</p>

            <p>Hope you are keeping well. I saw this great front-end developer role at GDS that I thought you might be interested in. You can found out more about it <a href="/jobs/description_frontend_developer">here</a></p>

            <p>Let me know how you get on,</p>

            <p>Mr Recruiter</p>
        """
    }
    return render_template('email_referred.html', email=email)


@blueprint.route('/contract')
def contract():
    return render_template('contract.html')
