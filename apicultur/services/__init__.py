#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pkgutil
import os
from base import Base


# Get all services available.
def load_services(dirname='services', version=None):
    # All packages in dirname
    modules = ['%s.%s' % (dirname, package_name) for importer, package_name, _ in pkgutil.iter_modules([dirname])]

    # All classes in each module
    candidate_services = []
    for mod in modules:
        module = __import__(mod)
        components = mod.split('.')
        for comp in components[1:]:
            module = getattr(module, comp)
            md = module.__dict__
            candidate_services += [md[c] for c in md if (isinstance(md[c], type) and md[c].__module__ == module.__name__)]

    # Work with candidates
    endpoints = {}
    for service in candidate_services:
        if issubclass(service, Base) and service.__name__ != 'Base':
            if service.endpoint in endpoints:
                raise ImportError("Duplicate endpoint at %r" % service.endpoint)
            endpoints.update({service.endpoint: service})
    return endpoints
