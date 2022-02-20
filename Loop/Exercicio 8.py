maior = -9999
menor = 9999

num = 10

for n in range(1, 11):
    numero = int(input(f"Informe o {n}/{num} valor: "))
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
print(maior)
print(menor)