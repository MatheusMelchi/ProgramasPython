"""
Faça um programa que receba dois numeros e mostre qual deles é o maior
"""

N1, N2 = input("Dois numeros ").split()

if int(N1) > int(N2):
    print(N1)
else:
    print(N2)
