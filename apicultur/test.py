#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur import Apicultur
from secret import ACCESS_TOKEN

def test1(app_name):
    apicultur = Apicultur(ACCESS_TOKEN, app=app_name)
    print("="*(len(app_name)+4))
    print("= %s =" % apicultur.app)
    print("="*(len(app_name)+4))

    if apicultur.check_token():
        # Let's work with this apicultur instance
        print(" - version: %s" % apicultur.version)
        print("")
        apicultur.list_services()
        print("")

        # Lematización
        print(u" - Lematización:")
        word = u'meses'
        print(u"   >> input: '%s'" % word)
        print(u"   + lematiza2: %s" % apicultur.lematiza2(word=word))
        print(u"   + lematiza2: %s" % apicultur.lematiza2(word=word))

    else:
        print("Invalid token :(")


if __name__ == '__main__':
    test1("My Application")