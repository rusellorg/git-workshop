import unittest

from exercise_5 import load_notes, calculate_final_notes


class Exercise5Spec(unittest.TestCase):
    def test_load_notes(self):
        self.assertEqual(load_notes('notes.csv'), [[1, 2, 3], [4, 5, 3]])

    def test_calculate_final_notes(self):
        self.assertEqual(calculate_final_notes([[4, 3, 3], [4, 5, 3]]), [3.9, 4.5])


if __name__ == '__main__':
    unittest.main()
