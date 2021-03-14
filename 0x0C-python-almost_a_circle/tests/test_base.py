#!/usr/bin/python3
"""
tests module
"""
import os
import unittest
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestBase(unittest.TestCase):
    """
    tests
    """

    def test_save_to_file(self):
        """
        Test
        """
        Base.save_to_file(None)
        res = "[]\n"
        with open("Base.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Base.json")
        except OSError:
            pass

        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def setUp(self):
        """
        Methods for each test
        """
        Base._Base__nb_objects = 0

    def test_types(self):
        """
        test
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_setting_id(self):
        """
        test
        """
        b3 = Base(True)
        self.assertEqual(b3.id, True)
        b4 = Base("string")
        self.assertEqual(b4.id, "string")
        b5 = Base(15)
        self.assertEqual(b5.id, 15)
        b6 = Base(None)
        self.assertEqual(b6.id, 1)
        b1 = Base(50)
        self.assertEqual(b1.id, 50)

    def test_error(self):
        """
        test
        """
        with self.assertRaises(TypeError):
            b7 = Base(1, 2)
            b8 = Base(True, 2)
            b9 = Base(True, "string")
        with self.assertRaises(AttributeError):
            b10 = Base(1025)
            var = b10.__nb_objects
