#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class CalculadorFrecuencia(Service):
    """
    Obtiene la frecuencia de uso o aparición en textos de una palabra. Calcula el número
    de veces que aparece dicha palabra por cada millón de palabras empleadas.

    +Info: https://store.apicultur.com/apis/info?name=CalculadorFrecuencia&version=1.0.0&provider=MolinodeIdeas
    """

    version = '1.0.0'
    endpoint = 'CalculaFrecuenciaPorMillon'
    method = 'GET'
    arguments = ['word',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '%(word)s')
