#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class NivelCervantes(Service):
    """
    Dada una palabra te devuelve su catalogación según el nivel de dificultad tomando
    como referente los niveles del Marco Europeo de Referencia para las Lenguas y las
    directrices del Instituto Cervantes.

    +Info: https://store.apicultur.com/apis/info?name=NivelCervantes&version=1.0.0&provider=MolinodeIdeas
    """

    version = '1.0.0'
    endpoint = 'damenivel'
    method = 'GET'
    arguments = ['word',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '%(word)s')
