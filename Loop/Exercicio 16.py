n = int(input("Numero Natural impar: "))

if n < 0:
    print("Numero invalido")
elif n % 2 == 0:
    print("Numero não impar")

r = range(1, n + 1)

r = reversed(r)

for n in range(n, -1, -1):
    if n % 2 == 1:
        print(n)