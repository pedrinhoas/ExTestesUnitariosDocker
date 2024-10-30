import unittest
import os
import sys
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Importar a função do módulo
from src.votar import voto

class TestVoto(unittest.TestCase):
    
    @patch.dict(os.environ, {"ANO_NASC": "2004"})
    def test_voto_2004(self):
        self.assertEqual(voto(), "Você pode votar")
    
    # @patch.dict(os.environ, {"ANO_NASC": "2010"})
    # def test_voto_2010(self):
    #     self.assertEqual(voto(), "Você não pode votar")
    
    # @patch.dict(os.environ, {"ANO_NASC": "1990"})
    # def test_voto_1990(self):
    #     self.assertEqual(voto(), "Você pode votar")

if __name__ == '__main__':
    unittest.main()
