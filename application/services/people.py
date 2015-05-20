import requests
import json
import os


class People(object):
    """Proxy to People Service

    """

    URL = os.environ.get('PEOPLE_PORT_3004_TCP').replace('tcp','http')
    PROFILE_API = '%s/profile' % URL
    SERVICE_API = '%s/service' % URL

    def create_profile(self, email, payload):
        return self._create(People.PROFILE_API, email, payload)

    def read_profile(self, email):
        return self._read(People.PROFILE_API, email)

    def create_service(self, email, payload):
        return self._create(People.SERVICE_API, email, payload)

    def read_service(self, email):
        return self._read(People.SERVICE_API, email)

    def _create(self, api, email, payload):
        data = json.dumps(payload)
        r = requests.post(
            api,
            data=data,
            auth=(email, 'hunter2'),
            headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
        self._maybe_create_user(r, email)
        return r

    def _read(self, api, email):
        r = requests.get(
            api,
            auth=(email, 'hunter2'),
            headers={'Accept': 'text/plain'})
        self._maybe_create_user(r, email)
        return r


    # just some show&tell hackery to automatically
    # create users if they don't exist
    def _maybe_create_user(self, response, email):
        if response.status_code // 100 != 2:
            data = json.dumps({'email': email})
            requests.post(
                '%s/session' % People.URL,
                data=data,
                headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
