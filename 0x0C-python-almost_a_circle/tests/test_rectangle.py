#!/usr/bin/python3
"""
test module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
import os


class TestBase(unittest.TestCase):
    """ test """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_types(self):
        """ test """
        b0 = Rectangle(7, 7)
        self.assertEqual(b0.id, 1)
        b1 = Rectangle(5, 6)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b1.area(), 30)
        self.assertEqual(b1.x * b1.y, 0)
        self.assertEqual(b1.to_dictionary(),
                         {'id': 2, 'width': 5, 'height': 6, 'x': 0, 'y': 0})
        b2 = Rectangle(9, 9)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b2.area(), 81)
        self.assertEqual(b2.x * b2.y, 0)
        self.assertEqual(b2.to_dictionary(),
                         {'id': 3, 'width': 9, 'height': 9, 'x': 0, 'y': 0})

        b3 = Rectangle(7, 7, 5)
        self.assertEqual(b3.area(), 49)
        self.assertEqual(b3.x * b3.y, 0)
        self.assertEqual(b3.id, 4)
        self.assertEqual(b3.to_dictionary(),
                         {'id': 4, 'width': 7, 'height': 7, 'x': 5, 'y': 0})

        b4 = Rectangle(8, 9, 6, 6)
        self.assertEqual(b4.area(), 72)
        self.assertEqual(b4.x * b4.y, 36)
        self.assertEqual(b4.id, 5)
        self.assertEqual(b4.to_dictionary(),
                         {'id': 5, 'width': 8, 'height': 9, 'x': 6, 'y': 6})

        b5 = Rectangle(10, 89, 9, 8, 66)
        self.assertEqual(b5.area(), 890)
        self.assertEqual(b5.x * b5.y, 72)
        self.assertEqual(b5.id, 66)
        self.assertEqual(b5.to_dictionary(),
                         {'id': 66, 'width': 10, 'height': 89, 'x': 9, 'y': 8})
        with self.assertRaises(TypeError):
            b6 = Rectangle(10, 89, 9, 8, 66, 8)

    def test_print_instance(self):
        """ test """
        b1 = Rectangle(1, 2)
        self.assertEqual(str(b1), "[Rectangle] (1) 0/0 - 1/2")
        b2 = Rectangle(1, 2, 3)
        self.assertEqual(str(b2), "[Rectangle] (2) 3/0 - 1/2")
        b3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(b3), "[Rectangle] (3) 3/4 - 1/2")
        b4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(b4), "[Rectangle] (5) 3/4 - 1/2")

    def test_errors(self):
        """ test """
        with self.assertRaises(TypeError):
            b6 = Rectangle(1, 2, 3, 4, 5, 6, 8)
            b5 = Rectangle()
            b6 = Rectangle(1025)
            b7 = Rectangle([1, 2])
            b8 = Rectangle(55)
        with self.assertRaises(TypeError) as exc:
            c = Rectangle("9", 5)
        self.assertEqual(str(exc.exception), "width must be an integer")
        with self.assertRaises(TypeError) as cm:
            b9 = Rectangle(10, True)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "height must be an integer")
        with self.assertRaises(TypeError) as cm:
            b9 = Rectangle(6, 9, [])
        self.assertEqual(str(cm.exception), "x must be an integer")
        with self.assertRaises(TypeError) as cm:
            b9 = Rectangle(50, 6, 5, "9")
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_update_and_to_dictionary(self):
        """ test """
        b1 = Rectangle(5, 6)
        self.assertEqual(b1.to_dictionary(),
                         {'id': 1, 'width': 5, 'height': 6, 'x': 0, 'y': 0})

        b2 = Rectangle(9, 9)
        self.assertEqual(b2.to_dictionary(),
                         {'id': 2, 'width': 9, 'height': 9, 'x': 0, 'y': 0})

        b3 = Rectangle(7, 7, 5)
        self.assertEqual(b3.to_dictionary(),
                         {'id': 3, 'width': 7, 'height': 7, 'x': 5, 'y': 0})

        b4 = Rectangle(8, 9, 6, 6)
        b4.update(1, 1, 1, 1, 88)
        self.assertEqual(b4.to_dictionary(),
                         {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 88})

        b5 = Rectangle(10, 89, 9, 8, 66)
        b5.update(5, 9, 8, 9, 5, 6, 9, 8)
        self.assertEqual(b5.to_dictionary(),
                         {'id': 5, 'width': 9, 'height': 8, 'x': 9, 'y': 5})

        # update *kwargs
        b6 = Rectangle(5, 5)
        b6.update(id=66, width=8, height=77, x=8, y=99)
        self.assertEqual(b6.to_dictionary(),
                         {'id': 66, 'width': 8, 'height': 77, 'x': 8, 'y': 99})

        with self.assertRaises(TypeError) as exc:
            arg = "height"
            b3 = Rectangle(5, 6, 7)
            b3.update(8, 9, [55])
        self.assertEqual(str(exc.exception), arg + " must be an integer")

        with self.assertRaises(TypeError) as exc:
            arg = "x"
            b4 = Rectangle(1, 2, 3, 4)
            b4.update(5, 8, 9, complex(1, 2))
        self.assertEqual(str(exc.exception), arg + " must be an integer")

        arg = ""
        with self.assertRaises(ValueError) as exc:
            arg = "width"
            b3 = Rectangle(2, 2)
            b3.update(0, 0, 9, 5, 9)
        self.assertEqual(str(exc.exception), arg + " must be > 0")

        with self.assertRaises(ValueError) as exc:
            arg = "width"
            b4 = Rectangle(2, 2)
            b4.update(0, -6)
        self.assertEqual(str(exc.exception), arg + " must be > 0")

        with self.assertRaises(ValueError) as exc:
            arg = "height"
            b5 = Rectangle(2, 2)
            b5.update(8, 5, 0, 5, 1)
        self.assertEqual(str(exc.exception), arg + " must be > 0")

        with self.assertRaises(ValueError) as exc:
            arg = "height"
            b6 = Rectangle(2, 2)
            b6.update(8, 5, -9, 0, 0)
        self.assertEqual(str(exc.exception), arg + " must be > 0")
        with self.assertRaises(ValueError) as exc:
            arg = "x"
            b1 = Rectangle(2, 2)
            b1.update(8, 5, 9, -5)
        self.assertEqual(str(exc.exception), arg + " must be >= 0")

        with self.assertRaises(ValueError) as exc:
            arg = "y"
            b2 = Rectangle(2, 2)
            b2.update(8, 5, 9, 5, -6)
        self.assertEqual(str(exc.exception), arg + " must be >= 0")

    def test_display(self):
        """ Test string displayed """
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test __str__ return value """
        r1 = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_save_to_file(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Rectangle.json")
        except OSError:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except OSError:
            pass

        b1 = Rectangle(20, 30)
        res = [b1.to_dictionary()]
        Rectangle.save_to_file([b1])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), b1.to_json_string(res))

        b1 = Rectangle(20, 30)
        b2 = Rectangle(5, 5)
        res = [b1.to_dictionary(), b2.to_dictionary()]
        Rectangle.save_to_file([b1, b2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), b1.to_json_string(res))
