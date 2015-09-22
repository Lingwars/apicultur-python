#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class FreelingNER(Service):
    """
    Named entity recognition API (Spanish): This API returns all named entities
    (people, places, organizations, institutions, etc) mentioned in a given text
    written in Spanish.

    +Info: https://apicultur.io/apis/info?name=NamedEntityRecognition_Freeling_es&version=1.0.0&provider=TheLinguist
    """
    version = '1.0.0'
    endpoint = 'thelinguist/freeling/ner/es/namedentities'
    method = 'POST'
    arguments = ['texto',]
    func_name = 'ner_es'

    def check_arguments(self, **kwargs):
        kwargs = super(FreelingNER, self).check_arguments(**kwargs)
        text = kwargs['texto']
        if not text.endswith(('.', '!', '?')):
            kwargs['texto'] = text + "."
        return kwargs