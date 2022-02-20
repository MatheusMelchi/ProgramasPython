num = 10

m = 0



for n in range(1, 11):
    numero = int(input(f"Informe o {n}/{num} valor: "))
    if numero < 0:
        numero = numero - numero
    m = m + numero
    media = m / 10
print(f"A media é {media}")