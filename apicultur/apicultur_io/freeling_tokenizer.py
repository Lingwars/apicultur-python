#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class FreelingTokenizer(Service):
    """
    Tokenizer API: This API divides a given text in Spanish into of words.

    +Info: https://apicultur.io/apis/info?name=Tokenizer_Freeling_es&version=1.0.0&provider=TheLinguist
    """
    version = '1.0.0'
    endpoint = 'thelinguist/freeling/tokenizer/es/tokens'
    method = 'POST'
    arguments = ['texto',]
    func_name = 'tokenize_es'

    def check_arguments(self, **kwargs):
        kwargs = super(FreelingTokenizer, self).check_arguments(**kwargs)
        text = kwargs['texto']
        if not text.endswith(('.', '!', '?')):
            kwargs['texto'] = text + "."
        return kwargs