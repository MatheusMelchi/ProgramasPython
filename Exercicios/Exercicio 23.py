A = input("Verificador de ano bissexto\n Ano: ")

if int(A) % 400 == 0 or int(A) % 4 == 0 and int(A) % 100 != 0:
    print("Ano bissexto")
else:
    print("Não é ano bissexto")