#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial
from throttle import Throttle, NoThrottle

class Apicultur(object):
    app = None
    access_token = None
    version = '1.0.0'
    base_url = 'http://store.apicultur.com/api'
    throttle = NoThrottle()

    def __init__(self, access_token, app=None):
        self.app = app
        self.access_token = access_token

        from services import load_available_services
        self._endpoints = load_available_services(self.version)

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
        service_class = self._endpoints[item]
        service = service_class(self.access_token, self.base_url)
        cur_service = partial(self.call_service, service=service)
        setattr(self, item, cur_service)
        return cur_service

    def call_service(self, service, *args, **kwargs):
        self.throttle.acquire()
        return service(*args, **kwargs)

