import unittest
import litery

class test_sprawdza_tekst(unittest.TestCase):

     def test_isalpha(self):
         wynik = litery.isalpha('ala ma kota')
         self.assertEqual(wynik,'ala ma kota')

    if True:
        print ('Ala ma kota')

if __name__ == '__main__':
    unittest.main()

        
