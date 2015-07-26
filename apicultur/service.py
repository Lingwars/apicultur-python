#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from urlparse import urljoin


class UnauthorizedError(Exception):
    pass

class RateLimitError(Exception):
    pass

class UnhandledError(Exception):
    pass


class Service(object):
    method = None
    arguments = None
    func_name = None

    def __init__(self, access_token, base_url):
        self.access_token = access_token
        self.base_url = base_url

    def _join_url(self, *args):
        return '/'.join([self.base_url] + list(args))

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version)

    @classmethod
    def get_func_name(cls):
        if cls.func_name:
            return cls.func_name
        else:
            return cls.endpoint.replace("\\", '_').replace('/', '_')

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

    def test_call(self):
        call_args = {}
        for arg in self.arguments:
            call_args[arg] = 'test'
        try:
            self(**call_args)
            return True
        except UnauthorizedError:
            return u'Unauthorized! Check your ACCESS_TOKEN and application subscription to this API.'

    def get_headers(self):
        return {'content-type': 'application/json',
                'Authorization': 'Bearer ' + self.access_token}

    def handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise UnauthorizedError()
        elif response.status_code == 503:
            raise RateLimitError()
        else:
            # TODO: Handle errors
            print(u"\tERROR %s" % (response.status_code))
            print(u"\t - url: %s" % response.url)
            print(u"\t - text: %s" % response.text)
            return UnhandledError()

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


import os
import sys

def load_services(path, version=None):
    # TODO: Implement version filtering
    # Search all classes in path
    sys.path.append(path)
    candidate_services = []
    for py in [f[:-3] for f in os.listdir(path) if f.endswith('.py') and f != '__init__.py']:
        mod = __import__(py, fromlist=[py])
        classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
        for cls in classes:
            candidate_services += [cls]
            setattr(sys.modules[__name__], cls.__name__, cls)

    # Work with candidates
    endpoints = {}
    for service in candidate_services:
        if issubclass(service, Service) and service.__name__ != Service.__name__:
            func_name = service.get_func_name()
            if func_name in endpoints:
                raise ImportError("Duplicate endpoint at %r" % func_name)
            service._filepath = path
            endpoints.update({func_name: service})
    return endpoints
