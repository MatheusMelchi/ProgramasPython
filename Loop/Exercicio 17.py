n = int(input("Numero Natural: "))

if n < 0:
    print("Numero não natural")

soma = 0

for n in range(1, n + 1):
    soma = soma + n

soma = soma - n
print(soma)