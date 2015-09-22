#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class FreelingNumerical(Service):
    """
    Quantities, dates and currency extractor API (Spanish): This API returns all numerical values
    (quantities, dates, currency, time, etc) mentioned in a given text in Spanish. Both expressions
    written in number (7) and in words (siete) are recognized.

    +Info: https://apicultur.io/apis/info?name=NumericalExpressionRecognition_Freeling_es&version=1.0.0&provider=TheLinguist
    """
    version = '1.0.0'
    endpoint = 'thelinguist/freeling/quantityextractor/es/quantities'
    method = 'POST'
    arguments = ['texto',]
    func_name = 'quantities_es'

    def check_arguments(self, **kwargs):
        kwargs = super(FreelingNumerical, self).check_arguments(**kwargs)
        text = kwargs['texto']
        if not text.endswith(('.', '!', '?')):
            kwargs['texto'] = text + "."
        return kwargs