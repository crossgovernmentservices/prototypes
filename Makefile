.PHONY: all test coverage coveralls flake8 dist clean

all:	flake8 test coverage

test:
	py.test -v -s

coverage:
	coverage run --source application -m py.test && coverage report

coveralls:
	py.test --cov application tests/ --cov-report=term --cov-report=html

flake8:
	flake8 application tests manage.py

dist:
	python3 setup.py sdist upload

init:
	pip3 install -r requirements/dev.txt

manage_example:
	manage.py foo 

upgrade:
	pip3 install --upgrade -r requirements/dev.txt

clean:
	-find . -name "__pycache__" | sudo xargs rm -rf
	-find . -name "*.pyc" | sudo xargs rm -f
	-find . -name ".webassets-cache" | sudo xargs rm -rf

govuk_elements_get:
	-./scripts/elements.sh

govuk_elements_clean:
	-rm -rf application/static/govuk_elements

elements:	govuk_elements_clean govuk_elements_get
