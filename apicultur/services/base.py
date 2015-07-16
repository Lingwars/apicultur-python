#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from urlparse import urljoin


class Base(object):
    method = None

    def __init__(self, access_token, base_url):
        self.access_token = access_token
        self.base_url = base_url

    def _join_url(self, *args):

        return '/'.join([self.base_url] + list(args))

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version)

    def build_arguments(self, *args, **kwargs):
        # TODO: Implement argument building
        pass

    def __call__(self, *args, **kwargs):
        # TODO: Use django dispatch approach
        if self.method == 'GET':
            return self.get(*args, **kwargs)
        elif self.method == 'POST':
            return self.post(*args, **kwargs)
        else:
            raise RuntimeError("Call method not implemented")

    def get_headers(self):
        return {'content-type': 'application/json',
                'Authorization': 'Bearer ' + self.access_token}

    def handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            # TODO: Handle errors
            print(u"\tERROR %s" % (response.status_code))
            return None

    def get(self, *args, **kwargs):
        endpoint = self.get_endpoint()
        url = endpoint % (kwargs)
        headers = self.get_headers()
        r = requests.get(url, headers=headers)
        return self.handle_response(r)

    def post(self, *args, **kwargs):
        url = self.get_endpoint()
        data = kwargs
        headers = self.get_headers()
        r = requests.post(url, data=json.dumps(data), headers=headers)
        return self.handle_response(r)
