FROM python:3.4
RUN apt-get update -qq

RUN mkdir -p /code/requirements
WORKDIR /code

ADD requirements /code/requirements
RUN pip install -r requirements/dev.txt

ADD . /code

EXPOSE 3003
