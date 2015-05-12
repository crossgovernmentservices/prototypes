# -*- coding: utf-8 -*-
from flask_assets import Bundle, Environment

# assets common to all blueprints
css_app = Bundle(
    'css/app.scss',
    filters='scss',
    output='gen/css/app.css',
    depends="**/*.scss"
)

js_app = Bundle(
    'js/app.js',
    filters='jsmin',
    output='gen/js/app.js'
)

# GOV.UK assets
css_govuk = Bundle(
    'css/govuk.scss',
    filters='scss',
    output='gen/css/govuk.css',
    depends="**/*.scss"
)

js_govuk = Bundle(
    'govuk_elements/public/javascripts/vendor/details.polyfill.js',
    filters='jsmin',
    output='public/js/govuk.js'
)

# 'jobs' blueprint
# Note: specifying 'css/govuk.scss' below wouldn't make govuk
# SCSS variables available to jobs.scss, hence you still need
# @import '../../../static/css/govuk';
# ...in your blueprint's SCSS.
css_jobs = Bundle(
    'jobs/css/jobs.scss',
    filters='scss',
    output='gen/css/jobs.css',
    depends="**/*.scss"
)

js_jobs = Bundle(
    'jobs/js/jobs.js',
    filters='jsmin',
    output='gen/js/jobs.js'
)

# reviews

css_jobs_review = Bundle(
    'jobs/css/review.scss',
    'jobs/css/radar-chart.scss',
    filters='scss',
    output='gen/css/jobs_review.css',
    depends="**/*.scss"
)

js_jobs_review = Bundle(
    'jobs/js/review.js',
    'jobs/js/d3.v3.min.js',
    'jobs/js/radar-chart.js',
    'jobs/js/review-summary.js',
    filters='jsmin',
    output='gen/js/jobs_review.js'
)

assets = Environment()

assets.register('css_app', css_app)
assets.register("js_app", js_app)

assets.register('css_govuk', css_govuk)
assets.register("js_govuk", js_govuk)

assets.register('css_jobs', css_jobs)
assets.register('js_jobs', js_jobs)

assets.register('css_jobs_review', css_jobs_review)
assets.register('js_jobs_review', js_jobs_review)
