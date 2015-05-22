import requests
import json
import os
from flask import g


class People(object):
    """Proxy to People Service

    """

    URL = os.environ.get('PEOPLE_PORT_3004_TCP', 'http://people-service/').replace('tcp','http')
    TOKEN = os.environ.get('PEOPLE_API_TOKEN', 'hunter2')  # http://bash.org/?244321
    PROFILE_API = '%s/profile' % URL
    SERVICE_API = '%s/service' % URL
    NOTIFICATION_API = '%s/notification' % URL

    def create_notification(self, message, transport='sms'):
        payload = {
            'message': message,
            'transport': transport
        }
        return self._create(People.NOTIFICATION_API, payload)

    def read_notification(self, ):
        return self._read(People.NOTIFICATION_API)

    def change_name(self, name):
        return self.update_profile(name=name)

    def create_profile(self, profile):
        return self._create(People.PROFILE_API, {'data': profile})

    def create_default_profile(self):
        profile = {
            'name': 'Colm Britton',
            'email.personal': g.email,
            'profile_pic': 'http://placehold.it/100x100',
            'tel': '01234567890',
            'integrations': {
                'linkedin': False
            },
            'cv': False,
            'is_civil_servant': False,
            'skills': [
                'Python',
                'Business analysis',
                'Stakeholder management',
                'Content design',
                'Graphics design'
            ],
            'role': 'TODO role_id',
            'team': 'Cross Government Tools',
            'area': 'GDS',
            'location': 'Aviation House, Kingsway, London',
            'profession': 'Digital',
            'function': 'Technology',
            'organisation': 'Cabinet Office'
        }
        return self.create_profile(profile)

    def update_profile(self, payload):
        # get existing proffile
        profile = self.read_profile()

        if profile:
            profile_data = profile['data']
            profile_data.update(payload)
            profile['data'] = profile_data

            return self._update(People.PROFILE_API, profile['id'], profile)
        else:
            # create a default profile
            return self._create(People.PROFILE_API, {'data': payload})
        
    def read_profile(self, ):
        """Assumes one profile entry"""
        response = self._read(People.PROFILE_API)
        if response.status_code // 100 == 2:
            resources = response.json()['resources']
            if len(resources) == 0:
                return None
            else:
                return resources[-1]
        else:
            return None

    def create_service(self, payload):
        return self._create(People.SERVICE_API, payload)

    def read_service(self, ):
        """Returns a 3-tuple of the form:
        (a, b, c)

        Where:
        a: all services available
        b: services user has granted/denied access to
        c: all services user hasn't granted/denied access to yet
        """
        with open('application/data/facts/services.json') as data_file:
            services = json.load(data_file)

        # the services the user hasn't granted/denied yet
        outstanding_services = []

        # the services the user has interacted with
        user_services = []

        response = self._read(People.SERVICE_API)
        if response.status_code // 100 == 2:
            user_services = response.json()['resources']
            for existing_service in services:
                has_service = False
                for user_service in user_services:
                    if user_service['data']['id'] == existing_service['id']:
                        has_service = True
                if not has_service:
                    outstanding_services.append(existing_service)
        return services, user_services, outstanding_services

    def _create(self, api, payload):
        data = json.dumps(payload)
        return requests.post(
            api,
            data=data,
            auth=(g.email, People.TOKEN),
            headers={'Content-type': 'application/json', 'Accept': 'application/json'})

    def _read(self, api, ):
        return requests.get(
            api,
            auth=(g.email, People.TOKEN),
            headers={'Accept': 'application/json'})

    def _update(self, api, id, payload):
        data = json.dumps(payload)
        return requests.put(
            '%s/%i' % (api, id),
            data=data,
            auth=(g.email, People.TOKEN),
            headers={'Content-type': 'application/json', 'Accept': 'application/json'})


    def create_user(self, email):
        data = json.dumps({'email': email})
        requests.post(
            '%s/session' % People.URL,
            data=data,
            headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
