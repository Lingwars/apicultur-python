#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class SegmentaTextos(Service):
    """
    API de segmentación de frases (sentence splitter). Dado un texto, devuelve las frases
    de las que está compuesto (la segmentación se hace teniendo en cuenta los signos de puntuación).
    El contenido de esta API esta basado en la plataforma Freeling.

    +Info: https://store.apicultur.com/apis/info?name=SegmentadorDeTextos&version=1.0.0&provider=MolinodeIdeas
    """

    version = '1.0.0'
    endpoint = 'segmentatextos'
    method = 'POST'
    arguments = ['texto',]

