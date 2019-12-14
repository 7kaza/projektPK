import unittest
import litery

class test_sprawdza_tekst(unittest.TestCase):

     def test_isalpha(self):
        x = litery.isalpha()
        self.assertEqual(x,True)


if __name__ == '__main__':
    unittest.main()
