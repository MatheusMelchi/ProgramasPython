"""
Faça um programa que leia um numero e caso ele seja positivo:

calcule e mostre o numero: Digitado ao quadrado e a raiz quadrada do numero digitado
"""

N = input("Numero ")

if float(N) > 0:
    print(f"{float(N) ** 2} numero ao quadrado {float(N) ** (1/2)} Raiz quadrada")
else:
    print("Numero invalido")
