#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from .apicultur import Apicultur
from .service import RateLimitError, UnauthorizedError


class ApiculturRateLimitSafe(Apicultur):

    def __init__(self, access_token, app=None, wait_seconds=2, *args, **kwargs):
        super(ApiculturRateLimitSafe, self).__init__(access_token, app, *args, **kwargs)
        self.wait_seconds = wait_seconds

    def call_service(self, service, *args, **kwargs):
        self.throttle.acquire()
        try:
            return service(*args, **kwargs)
        except RateLimitError:
            time.sleep(self.wait_seconds)
            return self.call_service(service, *args, **kwargs)
        except UnauthorizedError:
            print(u"API call to %s unauthorized! Check your access_token." % service.__class__.__name__)
        except UnhandledError:
            pass  # TODO: Silent error?
