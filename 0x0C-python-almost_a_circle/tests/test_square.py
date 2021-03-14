#!/usr/bin/python3
"""
test module
"""
import os
import subprocess
import sys
import unittest
from models.base import Base
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestBase(unittest.TestCase):
    """
    test
    """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_print_instance(self):
        """ test """
        b1 = Square(1, 2)
        self.assertEqual(str(b1), "[Square] (1) 2/0 - 1")
        b2 = Square(1, 2, 3)
        self.assertEqual(str(b2), "[Square] (2) 2/3 - 1")
        b3 = Square(1, 2, 3, 4)
        self.assertEqual(str(b3), "[Square] (4) 2/3 - 1")
        b4 = Square(1, 2, 3, 4)
        self.assertEqual(str(b4), "[Square] (4) 2/3 - 1")
        b1.update(55, 66, 22, 33)
        self.assertEqual(str(b1), "[Square] (55) 22/33 - 66")

    def test_types(self):
        """ test """
        b0 = Square(7)
        self.assertEqual(b0.id, 1)
        b1 = Square(5, 6)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b1.area(), 25)
        self.assertEqual(b1.x * b1.y, 0)
        self.assertEqual(b1.to_dictionary(),
                         {'id': 2, 'size': 5, 'x': 6, 'y': 0})
        b2 = Square(9, 9)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b2.area(), 81)
        self.assertEqual(b2.x * b2.y, 0)
        self.assertEqual(b2.to_dictionary(),
                         {'id': 3, 'size': 9, 'x': 9, 'y': 0})

        b3 = Square(7, 7, 5)
        self.assertEqual(b3.area(), 49)
        self.assertEqual(b3.x * b3.y, 35)
        self.assertEqual(b3.id, 4)
        self.assertEqual(b3.to_dictionary(),
                         {'id': 4, 'size': 7, 'x': 7, 'y': 5})

        b4 = Square(8, 9, 6, 6)
        self.assertEqual(b4.area(), 64)
        self.assertEqual(b4.x * b4.y, 54)
        self.assertEqual(b4.id, 6)
        self.assertEqual(b4.to_dictionary(),
                         {'id': 6, 'size': 8, 'x': 9, 'y': 6})

        with self.assertRaises(TypeError):
            b5 = Square(10, 89, 9, 8, 66)

    def test_errors(self):
        """ test """
        with self.assertRaises(TypeError):
            b6 = Square(1, 2, 3, 4, 5, 6, 8)
            b5 = Square()
            b6 = Square(1025)
            b7 = Square([1, 2])
            b8 = Square(55)
        with self.assertRaises(TypeError) as exc:
            c = Square("9", 5)
        self.assertEqual(str(exc.exception), "width must be an integer")
        with self.assertRaises(TypeError) as cm:
            b9 = Square(10, True)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "x must be an integer")
        with self.assertRaises(TypeError) as cm:
            b9 = Square(6, 9, [])
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_update_and_to_dictionary(self):
        """ test """
        # update *args
        b0 = Square(10)
        self.assertEqual(b0.to_dictionary(),
                         {'id': 1, 'size': 10, 'x': 0, 'y': 0})
        b0.update(5, 5, 5, 5)
        self.assertEqual(b0.to_dictionary(),
                         {'id': 5, 'size': 5, 'x': 5, 'y': 5})

        b1 = Square(100, 55)
        self.assertEqual(b1.to_dictionary(),
                         {'id': 2, 'size': 100, 'x': 55, 'y': 0})
        b1.update(20)
        self.assertEqual(b1.to_dictionary(),
                         {'id': 20, 'size': 100, 'x': 55, 'y': 0})

        b2 = Square(88, 23, 66)
        self.assertEqual(b2.to_dictionary(),
                         {'id': 3, 'size': 88, 'x': 23, 'y': 66})
        b2.update(17, 44)
        self.assertEqual(b2.to_dictionary(),
                         {'id': 17, 'size': 44, 'x': 23, 'y': 66})

        b3 = Square(28, 33, 75, 88)
        self.assertEqual(b3.to_dictionary(),
                         {'id': 88, 'size': 28, 'x': 33, 'y': 75})
        b3.update(5, 4, 3, 2)
        self.assertEqual(b3.to_dictionary(),
                         {'id': 5, 'size': 4, 'x': 3, 'y': 2})

        # update *kwargs
        b6 = Square(5, 5)
        b6.update(id=66, size=77, x=8, y=99)
        self.assertEqual(b6.to_dictionary(),
                         {'id': 66, 'size': 77, 'x': 8, 'y': 99})

    def test_update_and_to_dictionary_Errors(self):
        """ test """
        arg = ""
        with self.assertRaises(TypeError) as exc:
            arg = "width"
            b1 = Square(2, 2)
            b1.update(4, "5")
        self.assertEqual(str(exc.exception), arg + " must be an integer")

        with self.assertRaises(TypeError) as exc:
            arg = "x"
            b3 = Square(5, 6, 7)
            b3.update(8, 9, [55])
        self.assertEqual(str(exc.exception), arg + " must be an integer")

        with self.assertRaises(TypeError) as exc:
            arg = "y"
            b4 = Square(1, 2, 3, 4)
            b4.update(5, 8, 9, complex(1, 2))
        self.assertEqual(str(exc.exception), arg + " must be an integer")

        # Value Error
        arg = ""
        with self.assertRaises(ValueError) as exc:
            arg = "width"
            b3 = Square(2, 2)
            b3.update(0, 0, 9, 5, 9)
        self.assertEqual(str(exc.exception), arg + " must be > 0")

        with self.assertRaises(ValueError) as exc:
            arg = "width"
            b4 = Square(2, 2)
            b4.update(0, -6)
        self.assertEqual(str(exc.exception), arg + " must be > 0")

        with self.assertRaises(ValueError) as exc:
            arg = "width"
            b5 = Square(2, 2)
            b5.update(8, 0, 5, 1)
        self.assertEqual(str(exc.exception), arg + " must be > 0")

        with self.assertRaises(ValueError) as exc:
            arg = "width"
            b6 = Square(2, 2)
            b6.update(8, -9, 0, 0)
        self.assertEqual(str(exc.exception), arg + " must be > 0")
        with self.assertRaises(ValueError) as exc:
            arg = "x"
            b1 = Square(2, 2)
            b1.update(8, 5, -9, 5)
        self.assertEqual(str(exc.exception), arg + " must be >= 0")

        with self.assertRaises(ValueError) as exc:
            arg = "y"
            b2 = Square(2, 2)
            b2.update(8, 5, 9, -6)
        self.assertEqual(str(exc.exception), arg + " must be >= 0")

    def test_display(self):
        """ Test string displayed """
        r1 = Square(2, 2, 2)
        res = "\n\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "\n\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test __str__ return value """
        r1 = Square(2, 5, 2, 4)
        res = "[Square] (4) 5/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_save_to_file(self):
        """ Test JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except OSError:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except OSError:
            pass

        b1 = Square(20, 30)
        res = [b1.to_dictionary()]
        Square.save_to_file([b1])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), b1.to_json_string(res))

        b1 = Square(20, 30)
        b2 = Square(5, 5)
        res = [b1.to_dictionary(), b2.to_dictionary()]
        Square.save_to_file([b1, b2])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), b1.to_json_string(res))
