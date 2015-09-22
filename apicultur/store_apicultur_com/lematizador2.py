#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class Lematizador2(Service):
    """
    Dada una palabra, devuelve todos los lemas posibles y su categoría gramatical y
    análisis morfológico, siguiendo la nomenclatura de las etiquetas EAGLES

    +Info: http://store.apicultur.com/apis/info?name=Lematizador2&version=1.0.0&provider=MolinodeIdeas
    """

    version = '1.0.0'
    endpoint = 'lematiza2'
    method = 'GET'
    arguments = ['word',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '%(word)s')
