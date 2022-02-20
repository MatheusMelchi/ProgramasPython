n = int(input("Numero Natural par: "))

if n < 0:
    print("Numero invalido")
elif n % 2 == 1:
    print("Numero não par")

for n in range(1, n + 1):
    if n % 2 == 0:
        print(n)
