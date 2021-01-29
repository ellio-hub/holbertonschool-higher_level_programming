#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_value(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
        self.assertEqual(max_integer([1, 2, 5, 3, -4]), 5)
        self.assertEqual(max_integer([-1, -2, -5, -3, -4]), -1)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer(), None)