import os

def voto():

    ano_nasc = (int(os.getenv("Quando você nasceu? ", "2004")))
    idade = 2024 - ano_nasc
    idadevotar = 18
    if idade  >= idadevotar:
        autorizado = "Você pode votar"
    else:
        autorizado = "Você não pode votar"

    return autorizado
    
resultado = voto()
print(resultado)

