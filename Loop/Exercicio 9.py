n = int(input("Numero Natural: "))

if n < 0:
    print("Numero não natural")

n = n * 2

for n in range(1, n + 1):
    if n % 2 == 1:
        print(n)
