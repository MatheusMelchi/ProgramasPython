"""
Leia um numero fornecido pelo usuario. Se esse numero for positivo, calcule a raiz, quadrada do numero
se for negativo, imprima uma mensagem dizendo "Numero Invalido"
"""

N = input("Numero ")

if int(N) >= 0:
    print(f"{int(N)**(1/2)}")
else:
    print("Numero invalido")
