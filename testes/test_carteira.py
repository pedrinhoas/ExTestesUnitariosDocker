import unittest
import sys
import os

# Adiciona o diretório 'src' ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar a função do módulo correto
from src.dolar import carteira

# Classe de teste
class TestCarteira(unittest.TestCase):
    def test_carteira(self):
        # Teste com valor padrão de conversão
        self.assertAlmostEqual(carteira(100), 28.99, places=2)
        # Teste com valor diferente de conversão
        # self.assertAlmostEqual(carteira(6.90, 3.0), 2.30, places=2)

if __name__ == '__main__':
    unittest.main()

