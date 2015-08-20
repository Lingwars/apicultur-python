#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class EtiquetadorMorfologico(Service):
    # https://store.apicultur.com/apis/info?name=EtiquetadorMorfologico&version=1.0.0&provider=MolinodeIdeas
    version = '1.0.0'
    endpoint = 'etiqueta'
    method = 'POST'
    arguments = ['texto',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version)
