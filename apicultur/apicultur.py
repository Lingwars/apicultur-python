#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from functools import partial

from .throttle import Throttle, NoThrottle
from .service import load_services


APICULTUR = {'store.apicultur.com': {'base_url': 'http://store.apicultur.com/api',
                                     'version': '1.0.0',
                                     'services': os.path.join(os.path.dirname(__file__), 'store.apicultur.com')},
             'apicultur.io': {'base_url': 'http://apicultur.io/api',
                              'version': '1.0'}
}


class Apicultur(object):
    throttle = NoThrottle()
    _endpoints = {}

    def __init__(self, access_token, app=None, cfg_data=APICULTUR['store.apicultur.com']):
        self.app = app
        self.access_token = access_token
        if cfg_data:
            self.base_url = cfg_data['base_url']
            self.version = cfg_data['version']
            if 'services' in cfg_data:
                self.add_services(dirname=cfg_data['services'])

    def add_services(self, dirname, clear=False):
        if clear:
            self._endpoints.clear()
            self._endpoints = {}

        endpoints = load_services(dirname, self.version)
        self._endpoints.update(endpoints)  # TODO: What to do with duplicates?

    def check_token(self):
        # TODO: Is there a way to check this?
        return True

    def list_services(self):
        # List all services available in 'services' package and compatible with this version.
        for endpoint, obj in self._endpoints.iteritems():
            print(u"%s:\t .%s(%s)" % (obj.__name__, endpoint, ', '.join(obj.arguments)))

    def set_throttle(self, max_messages=0, every_seconds=None):
        assert(max_messages >= 0)
        assert(max_messages==0 or every_seconds > 0)
        if max_messages == 0:
            self.throttle = NoThrottle()
        else:
            self.throttle = Throttle(n_messages=max_messages, n_seconds=every_seconds)

    def __getattr__(self, item):
        # We are calling a service: build and return as callable
        service_class = self._endpoints.get(item, None)
        if not service_class:
            raise RuntimeError("API endpoint not available.")
        service = service_class(self.access_token, self.base_url)
        cur_service = partial(self.call_service, service=service)
        setattr(self, item, cur_service)
        return cur_service

    def call_service(self, service, *args, **kwargs):
        self.throttle.acquire()
        return service(*args, **kwargs)

