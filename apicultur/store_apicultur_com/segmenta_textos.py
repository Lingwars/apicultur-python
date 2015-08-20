#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class SegmentaTextos(Service):
    # https://store.apicultur.com/apis/info?name=SegmentadorDeTextos&version=1.0.0&provider=MolinodeIdeas
    version = '1.0.0'
    endpoint = 'segmentatextos'
    method = 'POST'
    arguments = ['texto',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version)
