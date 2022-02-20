ns = input("Numero da semana ")

if int(ns) == 1:
    print("Domingo")
elif int(ns) == 2:
    print("Segunda")
elif int(ns) == 3:
    print("Terça")
elif int(ns) == 4:
    print("Quarta")
elif int(ns) == 5:
    print("Quinta")
elif int(ns) == 6:
    print("Sexta")
elif int(ns) == 7:
    print("Sabado")
else:
    print(f"{int(ns)} dia da semana? Bom, nao existe.")