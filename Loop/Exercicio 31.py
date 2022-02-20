soma1 = 1
soma2 = 1

n = int(input("Numero: "))

for n in range(1, n + 1):
    soma1 = n * 2 - 1
    soma2 = n
    s = soma1 / soma2
    print(f"{soma1} / {soma2}")

