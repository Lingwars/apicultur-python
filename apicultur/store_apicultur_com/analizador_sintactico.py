#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from apicultur.service import Service

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class AnalizadorSintactico(Service):
    # https://store.apicultur.com/apis/info?name=CalculadorFrecuencia&version=1.0.0&provider=MolinodeIdeas
    version = '1.0.0'
    endpoint = 'analizador/sintactico'
    method = 'POST'
    arguments = ['text',]

    def get_headers(self):
        return {'content-type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.access_token}

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version)

    def post(self, *args, **kwargs):
        url = self.get_endpoint()
        headers = self.get_headers()
        body = urlencode(kwargs)
        r = requests.post(url, data=body, headers=headers)
        return self.handle_response(r)
