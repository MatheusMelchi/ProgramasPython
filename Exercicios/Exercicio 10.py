"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, ultilizando as
seguintes formulas (onde h corresponde a altura)

Homens: (72.7 * h) - 58
Mulheres: (62.1 * h) - 44.7
"""

h, s = input("Altura (em m) e sexo (respectivamente) ").split()

ph = (72.7 * float(h)) - 58

pm = (62.1 * float(h)) - 44.7

if s in ["f", "feminino"]:
    print(float(pm))
else:
    print(float(ph))


