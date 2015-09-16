#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class FreelingParser(Service):
    """
    Chunking & full parsing API (Spanish): This API returns the constituents (phrases) of a given sentence.
    It also provides its internal structure and components.

    +Info: https://apicultur.io/apis/info?name=Parser_Freeling_es&version=1.0.0&provider=TheLinguist
    """
    version = '1.0.0'
    endpoint = 'thelinguist/freeling/parser/es/parsing'
    method = 'POST'
    arguments = ['texto',]
    func_name = 'parse_es'

    def check_arguments(self, **kwargs):
        kwargs = super(FreelingParser, self).check_arguments(**kwargs)
        text = kwargs['texto']
        if not text.endswith(('.', '!', '?')):
            kwargs['texto'] = text + "."
        return kwargs