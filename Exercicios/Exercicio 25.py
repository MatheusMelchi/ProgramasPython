"""
Faça um programa que calcule as raizes da equação de segundo grau (Bhaskara)
"""
import sys
a, b, c = input("Valor de a, b, c (Bhaskara) ").split()

delta = float(b) ** 2 - (4 * float(a) * float(c))

if float(a) == 0:
    print("Não é uma equação de segundo grau")
    sys.exit()
elif float(delta) < 0:
    print("Não existe raiz")
    sys.exit()

a2 = float(a) * 2
#Raiz de delta
rd = float(delta) ** (1/2)
#Fazendo o b ficar negativo
b_negativo = float(b) * -1
#Primeira operação de x1
x1_primeira = float(b_negativo) + float(rd)
#X1
x1 = float(x1_primeira) / float(a2)
#Primeira operação de x2
x2_primeira = float(b_negativo) - float(rd)
#X2
x2 = float(x2_primeira) / float(a2)

if float(delta) == 0:
    print(f"x1: {float(x1)} Raiz unica")
elif float(delta) > 0:
    print(f"x1: {float(x1)} x2: {float(x2)}")



