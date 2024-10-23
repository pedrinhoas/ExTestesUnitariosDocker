import os

def carteira (din_pessoal, conversao = 3.45):
    din_dolar = din_pessoal / conversao
    return din_dolar


din_pessoal = float(os.getenv("Você tem reais?", "100"))

din_dolar = carteira(din_pessoal)
print(f"É possivel comprar {din_dolar:.2f} doletas")




