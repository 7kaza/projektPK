import unittest
import litery

class test_sprawdza_tekst(unittest.TestCase):

     def test_isalpha(self):
        txt = litery.isalpha("ala ma kota")
        self.assertTrue(self,txt)




if __name__ == '__main__':
    unittest.main()
