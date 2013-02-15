#! /usr/bin/env python

def series(n):
    """Fibonacci series to `n`, as a generator"""
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, b + a
