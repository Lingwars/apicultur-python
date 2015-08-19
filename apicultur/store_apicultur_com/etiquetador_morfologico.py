#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class etiquetador_morfologico(Service):
    version = '1.0.0'
    endpoint = 'etiqueta'
    method = 'POST'
    arguments = ['texto',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '%(word)s')
