"""
Programa que verifica qual triangulo é de acordo com o comprimento de seus lados
"""
import sys

A, B, C = input("Valor dos lados do tringulo ").split()
#Checagem pra ver se é um triangulo
if float(A) <= float(B) + float(C):
    pass
else:
    print("Não é um triangulo")
    sys.exit()

if float(B) <= float(A) + float(C):
    pass
else:
    print("Não é um triangulo")
    sys.exit()

if float(C) <= float(B) + float(A):
    pass
else:
    print("Não é um triangulo")
    sys.exit()
#Verificação de qual triangulo
if float(A) == float(B) == float(C):
    print("Triangulo Equilatero")
elif float(A) == float(B) != float(C):
    print("Triangulo Isóceles")
elif float(B) == float(C) != float(A):
    print("Triangulo Isóceles")
elif float(C) == float(A) != float(B):
    print("Triangulo Isóceles")
elif float(A) != float(B) != float(C):
    print("Triangulo Escaleno")

