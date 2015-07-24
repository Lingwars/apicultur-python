#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class PhoneToEnglish(Service):
    # # https://apicultur.io/apis/info?name=Ponenglish_phonenglish_to_english&version=1.0&provider=MolinodeIdeas
    version = '1.0'
    endpoint = 'phonenglish/phonetoenglish'
    method = 'GET'
    arguments = ['word',]
    func_name = 'phone_to_english'

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '?word=%(word)s')
