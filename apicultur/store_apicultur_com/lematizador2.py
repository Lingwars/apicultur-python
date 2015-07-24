#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class Lematizador2(Service):
    version = '1.0.0'
    endpoint = 'lematiza2'
    method = 'GET'
    arguments = ['word',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '%(word)s')
