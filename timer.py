# Copyright (C) Microsoft Corporation.  All rights reserved.

from __future__ import print_function
import timeit


def elapsed(func):
    """A decorator that times function execution."""
    if __debug__:
        def wrapper(*args, **kwargs):
            beg_ts = timeit.default_timer()
            retval = func(*args, **kwargs)
            end_ts = timeit.default_timer()
            print('%s elapsed: %f' % (func.__name__, end_ts - beg_ts))
            return retval
        return wrapper
    else:
        return func
