"""
Programa para verificar se o numero é divisor de 3 ou 5 mas nao os dois ao mesmo tempo
"""

n = input("Numero ")

if float(n) % 5 == 0 and float(n) % 3 == 0:
    print("é divisivel por 3 e 5")
elif float(n) % 3 == 0:
    print("É divisivel por 3")
elif float(n) % 5 == 0:
    print("É divisivel por 5")
else:
    print("Não é divisivel por 3 nem por 5")