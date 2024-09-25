import os
import sys
import unittest



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../src')))


#Importer la fonction à tester depuis src/add.py
from add import addition

class TestAdd(unittest.TestCase):
    def test_positif(self):
        self.assertEqual(addition(2,3), 5)  #assertEqual dit que la methode addition avec 2 et 3 doit être égal à 5
        
    def test_negatif(self): 
        self.assertEqual(addition(-1,1),0)
        
if __name__ == '__main__':       
    unittest.main()