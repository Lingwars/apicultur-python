#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class FreelingPOSTagger(Service):
    """
    Spanish POS tagger & Lemmatizer API: Given a text in Spanish, the API provides the lemma
    and part of speech tag for every word in the text. Morphosyntactic disambiguation is done
    through context.

    +Info: https://apicultur.io/apis/info?name=POStagger_Freeling_es&version=1.0.0&provider=TheLinguist
    """
    version = '1.0.0'
    endpoint = 'thelinguist/freeling/tagger/es/lemmas'
    method = 'POST'
    arguments = ['texto',]
    func_name = 'pos_tagger_es'

    def check_arguments(self, **kwargs):
        kwargs = super(FreelingPOSTagger, self).check_arguments(**kwargs)
        text = kwargs['texto']
        if not text.endswith(('.', '!', '?')):
            kwargs['texto'] = text + "."
        return kwargs