
""" Sample testcase"""
from django.test import SimpleTestCase

from app import calc

class ClacTest(SimpleTestCase):

    def test_add_num(self):
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)

    def test_subtract_num(self):
        """ Subtraction """
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)

        