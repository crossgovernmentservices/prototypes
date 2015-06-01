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
# SCSS variables available to your SCSS file, hence you still need
# @import '../../../static/css/govuk';
# ...in your blueprint's SCSS.
css_jobs = Bundle(
    'jobs/css/jobs.scss',
    filters='scss',
    output='gen/css/jobs.css',
    depends=['**/*.scss', 'jobs/css/**/*.scss']
)

js_jobs = Bundle(
    'jobs/js/signup.js',
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
    'jobs/js/details.polyfill.js',
    'signup/js/application.js',
    filters='jsmin',
    output='gen/js/jobs_review.js'
)

# 'professions' blueprint
# Note: specifying 'css/govuk.scss' below wouldn't make govuk
# SCSS variables available to your SCSS file, hence you still need
# @import '../../../static/css/govuk';
# ...in your blueprint's SCSS.
css_professions = Bundle(
    'professions/css/professions.scss',
    filters='scss',
    output='gen/css/professions.css',
    depends="**/*.scss"
)

js_professions = Bundle(
    'professions/js/professions.js',
    'professions/js/underscore.js',
    'professions/js/mustache.min.js',
    filters='jsmin',
    output='gen/js/professions.js'
)

# 'signup' blueprint
# Note: specifying 'css/govuk.scss' below wouldn't make govuk
# SCSS variables available to your SCSS file, hence you still need
# @import '../../../static/css/govuk';
# ...in your blueprint's SCSS.
css_signup = Bundle(
    'signup/css/signup.scss',
    'signup/css/jobs.scss',
    'signup/css/basicprofile.scss',
    filters='scss',
    output='gen/css/signup.css',
    depends=['**/*.scss', 'signup/css/**/*.scss']
)

js_signup = Bundle(
    'signup/js/jquery.ical-links.js',
    'signup/js/signup.js',
    filters='jsmin',
    output='gen/js/signup.js'
)

js_basic = Bundle(
    'signup/js/basic.js',
    filters='jsmin',
    output='gen/js/basic.js'
)

js_your_apps = Bundle(
    'signup/js/your_apps.js',
    filters='jsmin',
    output='gen/js/your_apps.js'
)

js_profile_jobs = Bundle(
    'signup/js/jobs.js',
    filters='jsmin',
    output='gen/js/jobs.js'
)

js_perf_review = Bundle(
    'signup/js/d3.v3.min.js',
    'signup/js/radar-chart.js',
    'signup/js/review-summary.js',
    filters='jsmin',
    output='gen/js/perf-review.js'
)
css_perf_review = Bundle(
    'signup/css/radar-chart.scss',
    filters='scss',
    output='gen/css/radar-chart.css',
    depends="**/*.scss"
)

js_prototype_login = Bundle(
    'signup/js/prototype_login.js',
    filters='jsmin',
    output='gen/js/prototype_login.js'
)

css_login = Bundle(
    'signup/css/login.scss',
    filters='scss',
    output='gen/css/login.css',
    depends="**/*.scss"
)

css_oauth = Bundle(
    'signup/css/googlelogin.scss',
    filters='scss',
    output='gen/css/oauth.css',
    depends="**/*.scss"
)

css_profile_jobs = Bundle(
    'signup/css/jobs.scss',
    filters='scss',
    output='gen/css/jobs.css',
    depends="**/*.scss"
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

assets.register('css_professions', css_professions)
assets.register('js_professions', js_professions)

assets.register('css_signup', css_signup)
assets.register('js_signup', js_signup)

assets.register('css_oauth', css_oauth)
assets.register('css_login', css_login)
assets.register('js_profile_jobs', js_profile_jobs)
assets.register('js_basic', js_basic)
assets.register('js_your_apps', js_your_apps)
assets.register('js_prototype_login', js_prototype_login)

assets.register('css_perf_review', css_perf_review)
assets.register('js_perf_review', js_perf_review)

