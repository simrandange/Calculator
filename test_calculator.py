"""
test_calculator.py

Unit tests for calculator.py. Run with: python -m unittest test_calculator.py
"""

import unittest
from calculator import add, subtract, multiply, divide, calculate


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-2, -3), -5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333, places=9)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_calculate(self):
        self.assertEqual(calculate(2, "+", 3), 5)
        self.assertEqual(calculate(2, "-", 3), -1)
        self.assertEqual(calculate(2, "*", 3), 6)
        self.assertEqual(calculate(6, "/", 3), 2)

    def test_calculate_unknown_operator(self):
        with self.assertRaises(ValueError):
            calculate(2, "%", 3)


if __name__ == "__main__":
    unittest.main()
