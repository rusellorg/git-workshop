import unittest
import exercise_3 as e3


class Exercise3Spec(unittest.TestCase):
    def test_calculate_years_months_days(self): 
        self.assertEqual(e3.calculate_years_months_days(575), (1, 7, 0))


if __name__ == '__main__':
    unittest.main()