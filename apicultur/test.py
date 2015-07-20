#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur import Apicultur
from secret import ACCESS_TOKEN


def print_title(app_name, test_name):
    length = len(app_name)+len(test_name)+6
    print("="*length)
    print("= %s: %s =" % (app_name, test_name))
    print("="*length)


def test_token(app_name):
    print_title(app_name, "test_token")
    apicultur = Apicultur(ACCESS_TOKEN, app=app_name)
    if apicultur.check_token():
        print(" - token valid! :D")
    else:
        print(" - invalid token! :(")


def test_list_services(app_name):
    print_title(app_name, "test_list_services")
    apicultur = Apicultur(ACCESS_TOKEN, app=app_name)

    print(" - version: %s" % apicultur.version)
    print("")
    apicultur.list_services()
    print("")


def test_call(app_name):
    print_title(app_name, "test_call")
    apicultur = Apicultur(ACCESS_TOKEN, app=app_name)

    # Lematización
    print(u" - Lematización:")
    word = u'meses'
    print(u"   >> input: '%s'" % word)
    print(u"   + lematiza2: %s" % apicultur.lematiza2(word=word))


def test_throttle(app_name):
    print_title(app_name, "test_throttle")
    apicultur = Apicultur(ACCESS_TOKEN, app=app_name)
    messages = 2
    seconds = 10
    apicultur.set_throttle(messages, seconds)
    print(u" - Throttle set to %d messages each %d seconds:" % (messages, seconds))
    for i in xrange(5):
        print(u"    + %dth call: %s" % (i, apicultur.lematiza2(word=u'perro')))

def test_freq(app_name):
    print_title(app_name, "test_freq")
    apicultur = Apicultur(ACCESS_TOKEN, app=app_name)
    # Freq
    print(u" - Compute frequencies for work:")
    word = u'meses'
    print(u"   >> input: '%s'" % word)
    print(u"   + freq: '%s'" % apicultur.CalculaFrecuenciaPorMillon(word=word))

def test_level(app_name):
    print_title(app_name, "test_level")
    apicultur = Apicultur(ACCESS_TOKEN, app=app_name)
    # Freq
    print(u" - Cervantes level:")
    word = u'perro'
    print(u"   >> input: '%s'" % word)
    print(u"   + freq: '%s'" % apicultur.damenivel(word=word))


if __name__ == '__main__':
    test_token("My Application")
    test_list_services("My Application")
    test_call("My Application")
    #test_throttle("My Application")
    test_freq("My App")
    test_level("My App")