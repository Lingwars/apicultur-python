#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from apicultur import Apicultur, UnauthorizedError
from secret import ACCESS_TOKEN


apicultur = Apicultur(ACCESS_TOKEN, app="Test")
#apicultur.add_services(os.path.join(os.path.dirname(__file__), 'services'))

def print_title(app_name, test_name):
    length = len(app_name)+len(test_name)+6
    print("="*length)
    print("= %s: %s =" % (app_name, test_name))
    print("="*length)


def test_token(app_name):
    print_title(app_name, "test_token")
    if apicultur.check_token():
        print(" - token valid! :D")
    else:
        print(" - invalid token! :(")


def test_list_services(app_name):
    print_title(app_name, "test_list_services")
    print(" - version: %s" % apicultur.version)
    print("")
    apicultur.list_services(test=True)
    print("")


def test_call(app_name):
    print_title(app_name, "test_call")
    # Lematización
    print(u" - Lematización:")
    word = u'meses'
    print(u"   >> input: '%s'" % word)
    print(u"   + lematiza2: %s" % apicultur.lematiza2(word=word))


def test_throttle(app_name):
    print_title(app_name, "test_throttle")
    messages = 2
    seconds = 10
    apicultur.set_throttle(messages, seconds)
    print(u" - Throttle set to %d messages each %d seconds:" % (messages, seconds))
    for i in xrange(5):
        print(u"    + %dth call: %s" % (i, apicultur.lematiza2(word=u'perro')))

def test_freq(app_name):
    print_title(app_name, "test_freq")
    # Freq
    print(u" - Compute frequencies for work:")
    word = u'meses'
    print(u"   >> input: '%s'" % word)
    print(u"   + freq: '%s'" % apicultur.CalculaFrecuenciaPorMillon(word=word))

def test_level(app_name):
    print_title(app_name, "test_level")
    # Freq
    print(u" - Cervantes level:")
    word = u'perro'
    print(u"   >> input: '%s'" % word)
    print(u"   + freq: '%s'" % apicultur.damenivel(word=word))


if __name__ == '__main__':
    #tests = [test_token, test_list_services, test_call, test_throttle, test_freq, test_level]
    tests = [test_token, test_list_services, test_call, test_freq, test_level]

    for test in tests:
        try:
            test("My App")
        except UnauthorizedError:
            print(u"[ERROR]: Unauthorized!")
