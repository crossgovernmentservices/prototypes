To update **govuk_template**:

    cd elsewhere
    git clone https://github.com/alphagov/govuk_template
    cd govuk_template
    bundle install
    bundle exec rake build:jinja
    mv pkg/jinja_<TAB> xgs_prototypes/application/static/govuk_template
