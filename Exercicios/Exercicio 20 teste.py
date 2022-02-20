import sys

A, B, C = input("Valor dos lados do tringulo ").split()

#Checagem pra ver se é um triangulo
if float(A) < float(B) + float(C) or float(B) < float(A) + float(C) or float(C) < float(B) + float(A):
    pass
else:
    print("Não é um triangulo")
    sys.exit()

if float(A) == float(B) == float(C):
    print("Triangulo Equilatero")
elif float(A) == float(B) != float(C) or float(B) == float(C) != float(A) or float(C) == float(A) != float(B):
    print("Triangulo Isóceles")
elif float(A) != float(B) != float(C):
    print("Triangulo Escaleno")
