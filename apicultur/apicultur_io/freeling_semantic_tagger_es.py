#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class FreelingSemanticTagger(Service):
    """
    Semantic tagger & POS tagger & Lemmatizer API (Spanish): Given a text in Spanish,
    the API provides the lemma, part of speech tag and semantic code from Wordnet for every word in the text.

    +Info: https://apicultur.io/apis/info?name=SemanticTagger_Freeling_es&version=1.0.0&provider=TheLinguist
    """
    version = '1.0.0'
    endpoint = 'thelinguist/freeling/semantictagger/es/lemmas'
    method = 'POST'
    arguments = ['texto',]
    func_name = 'semantic_tagger_es'

    def check_arguments(self, **kwargs):
        kwargs = super(FreelingSemanticTagger, self).check_arguments(**kwargs)
        text = kwargs['texto']
        if not text.endswith(('.', '!', '?')):
            kwargs['texto'] = text + "."
        return kwargs