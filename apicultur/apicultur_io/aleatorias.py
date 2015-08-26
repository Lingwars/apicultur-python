#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class AleatoriasNivel(Service):
    # http://apicultur.io/apis/info?name=WordsbyFreq_Word_Molino_es&version=1.0.0&provider=MolinodeIdeas
    version = '1.0.0'
    endpoint = 'molinodeideas/freq/es/words'
    method = 'GET'
    arguments = ['frecuencia',]
    func_name = 'aleatorias_nivel'

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '?frecuencia=%(frecuencia)s')
