"""
Faça um programa que receba dois numeros e mostre o maior.Assim como a diferença entre eles
"""
N1, N2 = input("Dois Numeros ").split()

if float(N1) > float(N2):
    print(f"{float(N1)} a diferença entre eles é {float(N1) - float(N2)}")
elif float(N2) > float(N1):
    print(f"{float(N2)} a diferença entre eles é {float(N2) - float(N1)}")
