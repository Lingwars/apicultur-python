#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lematizador2 import Lematizador2

# Get all services available
def load_available_services(version=None):
    # TODO: Consider version argument
    import sys
    import inspect
    from base import Base

    endpoints = {}
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and issubclass(obj, Base) and name != 'Base':
            if obj.endpoint in endpoints:
                raise ImportError("Duplicate endpoint at %r" % obj.endpoint)
            endpoints.update({obj.endpoint: obj})
    return endpoints

