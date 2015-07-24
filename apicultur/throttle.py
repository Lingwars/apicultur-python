#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This class has beed adapted from source code at https://github.com/shazow/apiclient/blob/master/apiclient/ratelimiter.py

import time
from threading import Lock


class RateExceededError(Exception):
    pass


class Throttle(object):
    n_messages = 0
    n_seconds = 0

    def __init__(self, n_messages=0, n_seconds=None):
        self.n_messages = n_messages
        self.n_seconds = n_seconds
        self.lock = Lock()
        self._reset_window()

    def _reset_window(self):
        self.window_num = 0
        self.window_time = time.time()

    def wait(self, wait_seconds):
        print(u"... waiting %s seconds for rate limit" % wait_seconds)
        time.sleep(wait_seconds)

    def acquire(self, block=True):
        self.lock.acquire()

        now = time.time()
        if now - self.window_time > self.n_seconds:
            self._reset_window()

        if self.window_num >= self.n_messages:
            if not block:
                self.lock.release()
                raise RateExceededError()

            wait_time = self.window_time + self.n_seconds - now
            self.lock.release()
            self.wait(wait_seconds=wait_time)

            self.lock.acquire()
            self._reset_window()

        self.window_num += 1
        self.lock.release()



class NoThrottle(Throttle):
    def acquire(self, block=True):
        pass