num = 10

soma = 0

for n in range(1, 11):
    numero = int(input(f"Informe o {n}/{num} valor: "))
    soma = numero + soma
print(soma)