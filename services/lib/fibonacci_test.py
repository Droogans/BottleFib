#! /usr/bin/env python

import unittest

import fibonacci

class TestFibonacci(unittest.TestCase):
    """test Fibonacci sequence generator service"""
    def test_fibonacci_series(self):
        """test just the fibonacci series generator"""
        self.assertEqual(list(fibonacci.series(3)),
                         [0, 1, 1, 2])

if __name__ == '__main__':
    unittest.main()
