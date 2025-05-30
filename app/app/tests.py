"""
sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """test adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        """test subtracting numbers together"""
        res = calc.sub(10, 15)
        self.assertEqual(res, 5)
