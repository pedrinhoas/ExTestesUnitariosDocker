import os

def carteira (din_pessoal):
    din_dolar = din_pessoal / 3.45
    return din_dolar


din_pessoal = float(os.getenv("Você tem reais?", "100"))

din_dolar = carteira(din_pessoal)
print(f"É possivel comprar {din_dolar:.2f} doletas")




