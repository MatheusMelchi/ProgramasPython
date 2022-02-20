print("Operações matematicas \n 1 - adição \n 2 - subtração \n 3 - multiplicação \n 4 - divisão")

o = input()

if float(o) == 1:
    print("Adição")
    n1, n2 = input("dois numeros por favor ").split()
    print(f"{float(n1) + float(n2)}")
elif float(o) == 2:
    print("Subtração")
    n1, n2 = input("dois numeros por favor ").split()
    print(f"{float(n1) - float(n2)}")
elif float(o) == 3:
    print("Multiplicação")
    n1, n2 = input("dois numeros por favor ").split()
    print(f"{float(n1) * float(n2)}")
elif float(o) == 4:
    print("Divisão")
    n1, n2 = input("dois numeros por favor ").split()
    print(f"{float(n1) / float(n2)}")
else:
    print("Operação invalida")