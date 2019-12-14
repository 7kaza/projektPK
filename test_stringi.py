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

     def test_capitalize(self):
        a = litery.funkcja_capitalize("ala ma kota")
        self.assertEqual(a,"Ala ma kota")

     def test_casefold(self):
        b = litery.funkcja_casefold("Ala Ma Kota")
        self.assertEqual(b,"ala ma kota")
     def test_lower(self):
        c = litery.funkcja.lower("Ala ma KOTA")
        self.assertEqual(c,"Ala ma kota")



if __name__ == '__main__':
    unittest.main()
