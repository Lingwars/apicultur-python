#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import Base

class NivelCervantes(Base):
    # https://store.apicultur.com/apis/info?name=NivelCervantes&version=1.0.0&provider=MolinodeIdeas
    version = '1.0.0'
    endpoint = 'damenivel'
    method = 'GET'
    arguments = ['word',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '%(word)s')
