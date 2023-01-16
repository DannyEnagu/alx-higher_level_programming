#!/usr/bin/python3
"""Unittests for ``Base`` class and methods."""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Define unittests for ``Rectangle`` class."""

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_agr(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(1, 2)
        self.assertEquals(r1.id, 1)

        r2 = Rectangle(3, 4)
        self.assertEquals(r2.id, 2)

    def test_five_args(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertRaises(r.id, 12)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 2, 0, 5, 12, 1)

    def test_private_attr(self):
        """Raises AttributeError when trying to access private attribute"""
        r = Rectangle(10, 5, 2, 4)
        with self.assertRaises(AttributeError):
            print(r.__width)

        with self.assertRaises(AttributeError):
            print(r.__height)

        with self.assertRaises(AttributeError):
            print(r.__x)

        with self.assertRaises(AttributeError):
            print(r.__y)

    def test_width_getter_and_setter(self):
        r = Rectangle(4, 3, 2, 9, 1)
        # Test width getter
        self.assertEqual(r.width, 4)
        # Test width setter
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_height_getter_and_setter(self):
        r = Rectangle(4, 3, 2, 9, 1)
        # Test height getter
        self.assertEqual(r.height, 3)
        # Test height setter
        r.height = 6
        self.assertEqual(r.height, 6)

    def test_x_getter_and_setter(self):
        r = Rectangle(4, 3, 2, 9, 1)
        # Test x getter
        self.assertEqual(r.x, 2)
        # Test x setter
        r.x = 15
        self.assertEqual(r.x, 15)

    def test_y_getter_and_setter(self):
        r = Rectangle(4, 3, 2, 9, 1)
        # Test y getter
        self.assertEqual(r.y, 9)
        # Test y setter
        r.y = 3
        self.assertEqual(r.y, 3)

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)


class TestRectangleClass_width(unittest.TestCase):
    """unittest for ``Rectangle`` instance attribute name ``width``"""

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)
