"""
Leia um numero real, se o numero for positvo imprima a raiz quadrada se ele for negativo
imprima-o ao quadrado
"""

NR = input("Numero real ")

if int(NR) > 0:
    print(int(NR) ** (1/2))
else:
    print(int(NR) ** 2)
