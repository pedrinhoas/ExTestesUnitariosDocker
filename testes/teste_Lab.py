import unittest

from src.dolar import carteira

# # Defina a função carteira
# def carteira(din_pessoal, conversao=3.45):
#     din_dolar = din_pessoal / conversao
#     return din_dolar

# Classe de teste
class TestCarteira(unittest.TestCase):
    def test_carteira(self):
        # Teste com valor padrão de conversão
        self.assertAlmostEqual(carteira(6.90), 2.0, places=2)
        # Teste com valor diferente de conversão
        self.assertAlmostEqual(carteira(6.90, 3.0), 2.30, places=2)

if __name__ == '__main__':
    unittest.main()
