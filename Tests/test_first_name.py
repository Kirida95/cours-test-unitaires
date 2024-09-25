import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../src')))

from first_name import greet_user

class TestGreet_user(unittest.TestCase):
    @patch('builtins.input', return_value='Jimmy')
    @patch('sys.stdout', new_callable=lambda:StringIO)
    def test_name_argument(self,mock_stdout,mock_input):
        
        result=greet_user()
        self.assertEqual(result, 'Merci Jimmy !')
        
  
        
if __name__=="__main__":
    unittest.main()
#tester si l'utilisateur peut entrer quelque chose
