#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class segmenta_textos(Service):
    version = '1.0.0'
    endpoint = 'segmentatextos'
    method = 'POST'
    arguments = ['texto',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '%(word)s')
