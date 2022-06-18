from unicodedata import name
import unittest

from exercise_2 import calculate_age_prompt

class Excersice2Spec(unittest.TestCase):
    def test_calculate_age_prompt(self):
        self.assertEqual(calculate_age_prompt(["10-05-2002", "05-10-2003", "10-01-2000"]), 20.0)


if __name__ == '__main__':
    unittest.main()