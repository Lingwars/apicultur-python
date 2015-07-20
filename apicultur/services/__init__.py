#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
from base import Base


def load_services(path, version=None):
    # TODO: Implement version filtering
    # Search all classes in path
    candidate_services = []
    for py in [f[:-3] for f in os.listdir(path) if f.endswith('.py') and f != '__init__.py']:
        mod = __import__('.'.join([__name__, py]), fromlist=[py])
        classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
        for cls in classes:
            candidate_services += [cls]
            setattr(sys.modules[__name__], cls.__name__, cls)

    # Work with candidates
    endpoints = {}
    for service in candidate_services:
        if issubclass(service, Base) and service.__name__ != 'Base':
            if service.endpoint in endpoints:
                raise ImportError("Duplicate endpoint at %r" % service.endpoint)
            endpoints.update({service.endpoint: service})
    return endpoints

