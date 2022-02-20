print("Escola uma opção: \n 1- Soma de dois numeros \n 2- Diferença entre dois numeros (Maior para o menor) \n 3- Produto entre dois numeros \n 4- divisão entre dois numeros (o divisor não pode ser 0)")

o = input("Opção: ")

if float(o) == 1:
    print("Soma de dois numeros")
    n1, n2 = input("dois numeros por favor ").split()
    print(f"{float(n1) + float(n2)}")
elif float(o) == 2:
    print("Diferença entre dois numeros")
    n1, n2 = input("dois numeros por favor ").split()
    print(f"{float(n1) - float(n2)}")
elif float(o) == 3:
    print("Produto entre dois numeros")
    n1, n2 = input("dois numeros por favor ").split()
    print(f"{float(n1) * float(n2)}")
elif float(o) == 4:
    print("Divisão entre dois numeros")
    n1, n2 = input("dois numeros por favor ").split()
    print(f"{float(n1) / float(n2)}")
else:
    print("Operação invalida")