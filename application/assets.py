# -*- coding: utf-8 -*-
from flask_assets import Bundle, Environment

css = Bundle(
    'css/main.scss',
    filters='pyscss',
    output='public/css/main.css',
    depends="**/*.scss"
)

js = Bundle(
    'js/main.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register("js_all", js)
assets.register('css_all', css)
