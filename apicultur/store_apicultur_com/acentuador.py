#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class Acentuador(Service):
    """
    Dadas las sílabas y la posición de la sílaba tónica devuelve la palabra correctamente acentuada
    +Info: http://store.apicultur.com/apis/info?name=Acentuador&version=1.0.0&provider=molinodeideas
    """
    version = '1.0.0'
    endpoint = 'acentua'
    method = 'GET'
    arguments = ['syllabicatedWord','stressedSyllablePosition',]

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '%(syllabicatedWord)s/%(stressedSyllablePosition)s')
        
# Ejemplo de llamada http://store.apicultur.com/api/acentua/1.0.0/ri-e/1
# Tania propone '%s/%s' % (syllabicatedWord, stressedSyllablePosition)
