def func ():
    nome = input("Qual o seu nome: ")
    salario = float(input("Quanto você ganha: "))
    anos_trabalho = int(input("Quantos anos você está na empresa: "))

    if anos_trabalho <= 3:
        recalculo = salario * (1 + 3/100)
    elif anos_trabalho > 3 and anos_trabalho <= 10:
        recalculo = salario * (1 + 12.5/100)
    else:
        recalculo = salario * (1 + 20/100)

    return nome, recalculo

nome, recalculo = func()
print(f"Parabéns {nome}, seu salário recalculado é de R$ {recalculo:,.2f}")