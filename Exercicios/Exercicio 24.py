import sys

valor = input("Valor do produto: ")

estado = input(" 1- São Paulo\n 2- Minas Gerais\n 3- Mato Grosso\n 4- Rio de janeiro\n Estado: ")

if float(valor) < 0:
    print("Valor invalido")
    sys.exit()

sp = float(valor) / 100 * 12

mg = float(valor) / 100 * 7

rj = float(valor) / 100 * 15

ms = float(valor) / 100 * 8

if int(estado) == int(1):
    print(float(sp) + float(valor))
elif int(estado) == int(2):
    print(float(mg) + float(valor))
elif int(estado) == int(3):
    print(float(rj) + float(valor))
elif int(estado) == int(4):
    print(float(ms) + float(valor))
else:
    print("Estado invalido")
    sys.exit()
