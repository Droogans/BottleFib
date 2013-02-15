#! /usr/bin/env python

import unittest

from fibonacci_service import fibonacci_document

class TestFibonacci(unittest.TestCase):
    """test Fibonacci sequence generator service"""
    def setUp(self):
        pass #start the server

    def tearDown(self):
        pass #stop the server

    def test_fibonacci_series(self):
        """test just the fibonacci series generator"""
        self.assertEqual(list(fibonacci.series(3)),
                         [0, 1, 1, 2])

    def test_fibonacci_service(self):
        """test to limit provided in given sample output"""
        expected = '<fibonacci><value index="0">0</value><value index="1">1</value><value index="2">1</value><value index="3">2</value></fibonacci>' 
        actual   = fibonacci_document(3)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

