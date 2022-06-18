import unittest

from excersice_4 import numer_primo

class Excersice4Spec(unittest.TestCase):
    def test_numeroPrimo(self):
        self.assertEqual(numer_primo(inicio=1, fin=10), [2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()