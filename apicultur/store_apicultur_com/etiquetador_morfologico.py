#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class EtiquetadorMorfologico(Service):
    """
    Dado un texto, devuelve los lemas y la categoría gramatical de cada palabra del texto.
    El contenido de esta API esta basado en la plataforma Freeling.

    +Info: https://store.apicultur.com/apis/info?name=EtiquetadorMorfologico&version=1.0.0&provider=MolinodeIdeas
    """

    version = '1.0.0'
    endpoint = 'etiqueta'
    method = 'POST'
    arguments = ['texto',]
