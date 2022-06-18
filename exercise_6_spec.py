import unittest

from excersice_6 import fibonacci


class Exercise6Spec(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(4), [1, 1, 2, 3])
        self.assertEqual(fibonacci(1), [1])
        self.assertEqual(fibonacci(5), [1, 1, 2, 3, 5])


if __name__ == '__main__':
    unittest.main()
