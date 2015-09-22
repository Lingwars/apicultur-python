#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class SilabeadorOrtografico(Service):
    """
    Separa en sílabas la palabra introducida

    +Info: http://store.apicultur.com/apis/info?name=SilabeadorOrtografico&version=1.0.0&provider=MolinodeIdeas
    """
    version = '1.0.0'
    endpoint = 'silabeame'
    method = 'GET'
    arguments = ['word',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '%(word)s')
