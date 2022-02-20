num = 10

m = 0



for n in range(1, 11):
    numero = int(input(f"Informe o {n}/{num} valor: "))
    m = m + numero
    media = m / 10
print(f"A media é {media}")