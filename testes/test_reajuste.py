import unittest
import sys
import os
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar a função do módulo correto
from src.salarioreajuste import func

class TestFunc(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["Bruno", "5000", "2"])
    def test_func_3_anos(self, mock_input):
        nome, recalculo = func()
        self.assertEqual(nome, "Bruno")
        self.assertAlmostEqual(recalculo, 5000 * 1.03, places=2)
    
    @patch('builtins.input', side_effect=["Bruno", "5000", "5"])
    def test_func_5_anos(self, mock_input):
        nome, recalculo = func()
        self.assertEqual(nome, "Bruno")
        self.assertAlmostEqual(recalculo, 5000 * 1.125, places=2)
    
    @patch('builtins.input', side_effect=["Bruno", "5000", "15"])
    def test_func_15_anos(self, mock_input):
        nome, recalculo = func()
        self.assertEqual(nome, "Bruno")
        self.assertAlmostEqual(recalculo, 5000 * 1.20, places=2)

if __name__ == '__main__':
    unittest.main()
