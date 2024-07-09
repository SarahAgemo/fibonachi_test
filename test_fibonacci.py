import unittest
from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fourth_number(self):
        self.assertEqual(fibonacci(4), 3)

    def test_first_number(self):
        self.assertEqual(fibonacci(1), 1)

    def test_second_number(self):
        self.assertEqual(fibonacci(2), 1)

    def test_zero_number(self):
        self.assertEqual(fibonacci(0), 0)


if __name__ == "__main__":
    unittest.main()

# PAIR PARTNERS - MOSES OLARA and SARAH AGEMO

# https://github.com/WodPachua/TDD-Test-First-Fibonacci-exercise for JavaScript Code.
