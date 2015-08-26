#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service
# https://store.apicultur.com/apis/info?name=DiccionariodeEspanol&version=1.0.0&provider=MolinodeIdeas
# https://store.apicultur.com/api/dicc/1.0.0/definicion/10/mel%C3%B3n
class Definicion_Uno(Service):
    prepoint = 'dicc'
    version = '1.0.0'
    endpoint = 'definicion/10'
    method = 'GET'
    arguments = ['word',]

    def get_endpoint(self):
        return self._join_url(self.prepoint, self.version, self.endpoint, '%(word)s')
