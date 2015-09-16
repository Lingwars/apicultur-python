#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class FreelingSentenceSplitter(Service):
    """
    Sentence splitter API (Spanish): This API splits a given text into sentences taking into account
    Spanish rules for punctuation marks.

    +Info: https://apicultur.io/apis/info?name=SenteceSplitter_Freeling_es&version=1.0.0&provider=TheLinguist
    """
    version = '1.0.0'
    endpoint = 'thelinguist/freeling/splitter/es/sentences'
    method = 'POST'
    arguments = ['texto',]
    func_name = 'sentence_splitter_es'

    def check_arguments(self, **kwargs):
        kwargs = super(FreelingSentenceSplitter, self).check_arguments(**kwargs)
        text = kwargs['texto']
        if not text.endswith(('.', '!', '?')):
            kwargs['texto'] = text + "."
        return kwargs