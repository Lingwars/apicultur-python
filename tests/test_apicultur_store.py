#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from apicultur import Apicultur, UnauthorizedError
from secret import ACCESS_TOKEN_STORE


class TestApiculturStore(unittest.TestCase):
    apicultur = Apicultur(ACCESS_TOKEN_STORE, cfg_data='store.apicultur.com')

    def test_token(self):
        self.assertTrue(self.apicultur.check_token())

    def test_not_service(self):
        with self.assertRaises(RuntimeError) as e:
            self.apicultur.NotAService(word='meses')

    @unittest.skip("Cannot know if provided ACCESS_TOKEN is valid for this service")
    def test_calculador_frecuencia(self):
        r = self.apicultur.CalculaFrecuenciaPorMillon(word='meses')
        self.assertEqual(r['palabra'], 'meses')
        self.assertEqual(r['valor'], 273.01)

    @unittest.skip("Cannot know if provided ACCESS_TOKEN is valid for this service")
    def test_lemmatizador2(self):
        r = self.apicultur.lematiza2(word='meses')
        self.assertEqual(r['palabra'], 'meses')
        self.assertEqual(len(r['lemas']), 2)
        # meses -> mes
        self.assertEqual(r['lemas'][0]['lema'], 'mes')
        self.assertEqual(r['lemas'][0]['categoria'], 'NCMP000')
        # meses -> mesar
        self.assertEqual(r['lemas'][1]['lema'], 'mesar')
        self.assertEqual(r['lemas'][1]['categoria'], 'VMSP2S0')

    @unittest.skip("Cannot know if provided ACCESS_TOKEN is valid for this service")
    def test_nivel_cervantes(self):
        r = self.apicultur.damenivel(word='meses')
        print(r)
