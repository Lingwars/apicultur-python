#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class EnglishToPhone(Service):
    # https://apicultur.io/apis/info?name=Phonenglis_english_to_phonenglish&version=1.0&provider=MolinodeIdeas
    version = '1.0'
    endpoint = 'phonenglish/englishtophone'
    method = 'GET'
    arguments = ['word',]
    func_name = 'english_to_phone'

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '?word=%(word)s')
