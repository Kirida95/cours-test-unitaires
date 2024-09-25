import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../src')))

from first_name import greet_user

class TestGreet_user(unittest.TestCase):
    @patch('builtins.input', return_value='Jimmy')
    @patch('sys.stdout', new_callable=StringIO)
    def test_name_argument(self,mock_stdout,mock_input):
        
        greet_user()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Merci Jimmy !')
        
    @patch('builtins.input', return_value='')  # Simule un prénom vide
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_name(self, mock_stdout, mock_input):
        greet_user()  # Appel de la fonction
        # Vérification que la sortie est celle attendue
        self.assertEqual(mock_stdout.getvalue().strip(), "Vous n'avez pas saisi un prénom valide")    
  
        
if __name__=="__main__":
    unittest.main()
#tester si l'utilisateur peut entrer quelque chose
