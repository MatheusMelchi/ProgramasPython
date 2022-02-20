"""
Escreva um programa que leia um numero inteiro.Se ele for negativo imprima "Numero invalido"
se for positivo de o logaritimo desse numero
"""
import math

n = input("Numero inteiro ")

if int(n) > 0:
    print(f"{math.log10(int(n))} log")
else:
    print("Numero invalido")