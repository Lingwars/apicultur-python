#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from urlparse import urljoin


class Base(object):
    method = None
    arguments = None

    def __init__(self, access_token, base_url):
        self.access_token = access_token
        self.base_url = base_url

    def _join_url(self, *args):
        return '/'.join([self.base_url] + list(args))

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version)

    def check_arguments(self, **kwargs):
        if self.arguments:
            for arg in self.arguments:
                if not arg in kwargs:
                    raise AttributeError("Missing %r named argument" % arg)
        return kwargs

    def __call__(self, **kwargs):
        arguments = self.check_arguments(**kwargs)
        # TODO: Use django dispatch approach
        if self.method == 'GET':
            return self.get(**arguments)
        elif self.method == 'POST':
            return self.post(**arguments)
        else:
            raise RuntimeError("Call method not implemented")

    def get_headers(self):
        return {'content-type': 'application/json',
                'Authorization': 'Bearer ' + self.access_token}

    def handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print(u"ERROR 401: Unauthorized!")
            return None
        else:
            # TODO: Handle errors
            print(u"\tERROR %s" % (response.status_code))
            print(u"\t - url: %s" % response.url)
            print(u"\t - text: %s" % response.text)
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
