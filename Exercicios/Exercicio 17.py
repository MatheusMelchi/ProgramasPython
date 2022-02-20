"""
Programa que calcula area de um trapezio
"""

BM, bm, h = input("Base Maior, Base menor, Altura (respectivamente) ") .split()

O1 = float(bm) + float(BM)

O2 = float(O1) * float(h)

R = float(O2) / 2

x = 0

if float(bm) >= float(BM):
    print("Base Invalida")
elif float(x) >= float(bm):
    print("Base invalida")
elif float(x) >= float(BM):
    print("Base invalida")
else:
    print(f"{float(R)} cm")
