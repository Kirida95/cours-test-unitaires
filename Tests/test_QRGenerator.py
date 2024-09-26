import os
import sys
import unittest
from unittest.mock import patch,MagicMock
from pyvirtualdisplay import Display
import tkinter as tk
from tkinter import messagebox

from PIL import *



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../src')))

from QRGenerator import QRCodeGeneratorApp

class TestInit(unittest.TestCase):
    #tester démarrage app
    
    def setUp(self):
        # Démarrer un affichage virtuel (pour ci/cd)
        if sys.platform != 'win32':
            self.display = Display(visible=0, size=(800, 600))
            self.display.start()
        self.root = tk.Tk()
        self.app = QRCodeGeneratorApp(self.root)
        self.root.update_idletasks()
       
    def tearDown(self):
        self.root.destroy()
        if sys.platform != 'win32':
            self.display.stop() 
    
    
    #Tester que la taille de la fenêtre est bien 400x400 
    # def test_geometry(self):
    #     app_geometry = self.root.geometry()
    #     print(f"App geometry: {app_geometry}")
    #     self.assertTrue(app_geometry.startswith("400x400"))
        
    #tester l'input
    def test_url(self):
        self.app.entry.insert(0,"https://www.esgi.fr/")
        url = self.app.entry.get()
        self.assertEqual(url,"https://www.esgi.fr/")
    
    #Test avec url vide
    @patch('tkinter.messagebox.showwarning')  # Mock le messagebox   
    def test_empty_url(self,mock_showwarning):
        self.app.entry = MagicMock()
        self.app.entry.get.return_value = ""  # Retourne une chaîne vide

        # Appeler la méthode pour générer le QR Code
        self.app.generate_qr_code()

        # Vérifier que le message d'avertissement a été appelé
        mock_showwarning.assert_called_once_with("Avertissement", "Veuillez entrer une adresse URL pour générer un QR Code.")
        
        # url = self.app.entry.get()
        # if not url:
        #     self.assertTrue(messagebox.showwarning("Avertissement" , "Veuillez entrer une adresse URL pour générer un QR Code."))
     
     #Tester la taille du QrCode   
    def test_img_size(self):
        self.app.entry.insert(0,"https://www.esgi.fr/")
        self.app.generate_qr_code()
        
        img=self.app.qr_image
        img_size = (img.width(),img.height())
        self.assertEqual(img_size,(300,300))
        
        
        

        
    
        
            
        
        
        
        
        
        
        
if __name__ == '__main__':       
    unittest.main()