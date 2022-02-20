n = int(input("Numero: "))

soma = 0

for num in range(1, n + 1):
    soma = soma + num
print(soma)

soma1 = 1

n2 = (2 * n - 1)

for num in range(1, n2 + 1):
    soma1 = num + soma
print(soma1)