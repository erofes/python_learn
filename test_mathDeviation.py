import unittest
from MathDeviation import MathDeviation


class TestMathDeviation(unittest.TestCase):
    def setUp(self):
        self.mathDeviation = MathDeviation()

    def test_two_roots_1(self):
        self.assertEqual(self.mathDeviation.solve_ABC(2, 5, 3), (-1, -1.5))

    def test_two_roots_2(self):
        self.assertEqual(self.mathDeviation.solve_ABC(2, -9, 7), (3.5, 1))

    def test_one_root(self):
        self.assertEqual(self.mathDeviation.solve_ABC(2, 4, 2), -1)

    def test_no_roots(self):
        self.assertEqual(self.mathDeviation.solve_ABC(2, 1, 3), "This equation has no roots")


