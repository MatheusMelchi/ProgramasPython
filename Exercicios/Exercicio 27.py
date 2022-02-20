import sys

idade = input("Idade do nadador ")

if int(idade) < 0:
    print("Idade Invalida")
    sys.exit()

if int(idade) < 7:
    print("Infantil A")
elif 8 <= int(idade) <= 10:
    print("Infantil B")
elif 11 <= int(idade) <= 13:
    print("Juvenil A")
elif 14 <= int(idade) <= 17:
    print("Juvenil B")
elif int(idade) >= 18:
    print("Senior")
