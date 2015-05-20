# XGS Prototypes

[![Build Status](https://travis-ci.org/crossgovernmentservices/xgs_prototypes.svg)](https://travis-ci.org/crossgovernmentservices/xgs_prototypes)

Smoke and mirrors for XGS (Cross Government Services) prototypes.

Supersedes **cgt_prototypes**.

## Quickstart

Run [dev-env bootstrap](https://github.com/crossgovernmentservices/dev-env#3-bootstrap).

Quickly add a new blueprint with ```./scripts/blueprint```

## TODO

# Live debug

    heroku run python manage.py shell
    # -or-
    docker-compose run xgsprototypes python manage.py shell
    # then, interact with the app:
    app.test_client().get('/signup/basicprofile')


Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration:

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server

### Deployment

In your production environment, make sure the ``APPLICATION_ENV`` environment variable is set to ``"prod"``.


### Shell

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``User`` model.


### Running Tests

To run all tests, run ::

    python manage.py test


### Migrations

Whenever a database migration needs to be made. Run the following commmands:

    python manage.py db migrate

This will generate a new migration script. Then run:

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.
