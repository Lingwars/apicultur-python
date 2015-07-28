#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from apicultur import Apicultur, UnauthorizedError
from secret import ACCESS_TOKEN_IO


class TestApiculturIO(unittest.TestCase):
    apicultur = Apicultur(ACCESS_TOKEN_IO, cfg_data='apicultur.io')

    def test_token(self):
        self.assertTrue(self.apicultur.check_token())

    def test_not_service(self):
        with self.assertRaises(RuntimeError) as e:
            self.apicultur.NotAService(word='meses')
