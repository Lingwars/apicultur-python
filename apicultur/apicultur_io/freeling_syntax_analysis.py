#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class FreelingSyntaxAnalysis(Service):
    """
    Syntax analysis API (Spanish): This API returns the syntax analysis
    (chunks, phrases and dependency relations between components) of a given sentence.

    +Info: https://apicultur.io/apis/info?name=SyntaxAnalysis_Freeling_es&version=1.0.0&provider=TheLinguist
    """
    version = '1.0.0'
    endpoint = 'thelinguist/freeling/parser/es/dependencies'
    method = 'POST'
    arguments = ['texto',]
    func_name = 'syntax_analysis_es'

    def check_arguments(self, **kwargs):
        kwargs = super(FreelingSyntaxAnalysis, self).check_arguments(**kwargs)
        text = kwargs['texto']
        if not text.endswith(('.', '!', '?')):
            kwargs['texto'] = text + "."
        return kwargs