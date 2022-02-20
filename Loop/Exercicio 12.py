n = int(input("Numero Natural: "))

if n < 0:
    print("Numero não natural")

r = range(0, n + 1)

reversed_r = reversed(r)

for n in reversed_r:
    print(n)

