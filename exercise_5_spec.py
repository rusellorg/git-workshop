import unittest

from exercise_5 import load_notes


class Exercise5Spec(unittest.TestCase):
    def test_load_notes(self):
        self.assertEqual(load_notes('notes.csv'), [[1, 2, 3], [4, 5, 3]])


if __name__ == '__main__':
    unittest.main()
