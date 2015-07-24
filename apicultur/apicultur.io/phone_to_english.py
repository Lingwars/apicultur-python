#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class PhoneToEnglish(Service):
    # https://store.apicultur.com/apis/info?name=CalculadorFrecuencia&version=1.0.0&provider=MolinodeIdeas
    version = '1.0'
    endpoint = 'phonenglish/englishtophone'
    method = 'GET'
    arguments = ['word',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '%(word)s')
