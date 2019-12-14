import unittest
import litery

class test_sprawdza_tekst(unittest.TestCase):

     def test_isalpha(self):
        txt = litery.funkcja_isalpha("alamakota")
        self.assertTrue(txt)

     def test_isalnum(self):
        x = litery.funkcja_isalnum("alama2koty")
        self.assertTrue(x)
        x = litery.funkcja_isalnum("ala ma 2 koty")
        self.assertFalse(x)





if __name__ == '__main__':
    unittest.main()
