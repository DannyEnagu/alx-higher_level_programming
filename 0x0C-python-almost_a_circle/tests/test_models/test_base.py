#!/usr/bin/python3
"""Unittests for ``Base`` class and methods."""

import unittest

from models.base import Base

class BaseClass(unittest.TestCase):
    """Define unittests for ``Base`` class."""

    def test_without_arg(self):
        """Test That Base() is call without any argument"""
        bs1 = Base()
        bs2 = Base(2)
        self.assertEqual(bs2.id, 2)

    def test_with_arg(self):
        """Test that Base(12) is call with valid argument (int)

           Assumption:
            Note: it is assumed that the arguments pass will always
            be integer and we don’t need to test the type of it.
        """
        bs = Base(12)
        self.assertEqual(bs.id, 12)

    def test_id_None(self):
        """Test that ``Base(None)`` was called with None"""
        bs = Base(None)
        self.assertEqual(bs.id, 1)

    def test_two_arg(self):
        """Test for two or more arguments to ``Base``"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_public_attr_id(self):
        """Test that public attr id was directly assign value"""
        bs = Base(12)
        bs.id = 5
        self.assertEqual(5, bs.id)

    def test_id_after_arg(self):
        """Test value of id after calling ``Base(12)``"""
        bs1 = Base()
        bs2 = Base(12)
        bs3 = Base()
        self.assertEqual(bs1.id, 2)

if __name__ == '__main__':
    unittest.main()
