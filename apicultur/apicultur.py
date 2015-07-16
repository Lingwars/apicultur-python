#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Apicultur(object):
    app = None
    access_token = None
    version = '1.0.0'
    base_url = 'http://store.apicultur.com/api'

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
            print(u"%s: .%s(%s)" % (obj.__name__, endpoint, ', '.join(obj.arguments)))

    def __getattr__(self, item):
        # We are calling to a service: build and return as callable
        service_class = self._endpoints[item]
        service = service_class(self.access_token, self.base_url)
        setattr(self, item, service)
        return service

