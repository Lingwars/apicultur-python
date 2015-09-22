#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class Definicion_Uno(Service):
    """
    API del diccionario de español. Proporciona definiciones de la palabra pasada por parámetro

    +Info: https://store.apicultur.com/apis/info?name=DiccionariodeEspanol&version=1.0.0&provider=MolinodeIdeas
    """

    version = '1.0.0'
    endpoint = 'definicion/10'
    method = 'GET'
    arguments = ['word',]

    def get_endpoint(self):
        return self._join_url('dicc', self.version, self.endpoint, '%(word)s')
