FROM python:3.4
RUN apt-get update -qq && apt-get -y install rubygems unzip ruby-dev
RUN gem install sass bundler rake

# separate requirements space to prevent things like 'src'
# from popping up when pip finds stuff on Github, for instance.
RUN mkdir -p /reqs/requirements
ADD requirements /reqs/requirements
WORKDIR /reqs
RUN pip install -r requirements/dev.txt

RUN mkdir /code
WORKDIR /code
ADD . /code

EXPOSE 3003
