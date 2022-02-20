sexo = input("M- Masculino\nF- feminino\n")

altura = float(input("Sua Altura (em metros): "))

if sexo == "m" or sexo == "M":
    peso = (72.7 * altura) - 58
    print(peso)
elif sexo == "f" or sexo == "F":
    peso = (62.1 * altura) - 44.7
    print(peso)
else:
   print("Entrada Invalida")
