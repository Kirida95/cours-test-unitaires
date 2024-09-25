import os
import sys
import unittest
import pycountry
import pycountry_convert 


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../src')))


#Importer la fonction à tester depuis src/add.py
from countries import continent_name,continent_code
    #vérifier que chaque continent a bien un nom
class Test_Continent(unittest.TestCase):
    def test_continent_name(self):
        for country in pycountry.countries:
            self.assertNotEqual(continent_name,"unknown")
            
    def Test_Continent_Code(self):
        for country in pycountry.countries: 
            self.assertEqual(pycountry_convert.country_alpha2_to_continent_code(country.alpha2),continent_code)
            
     
            
if __name__ == '__main__':       
    unittest.main()