import unittest

from exercise_1 import calculate_hypotenuse, calculate_area_and_perimeter


class Exercise1Spec(unittest.TestCase):
    def test_calculate_hypotenuse(self):
        self.assertEqual(calculate_hypotenuse(1, 1), 1.4)

    def test_calculate_area_and_perimeter(self):
        self.assertEqual(calculate_area_and_perimeter(1, 1), (0.5, 3.4))


if __name__ == '__main__':
    unittest.main()
