n = int(input("Numero Natural par: "))

if n < 0:
    print("Numero invalido")
elif n % 2 == 1:
    print("Numero não par")

r = range(1, n + 1)

reverser_r = reversed(r)

for n in reverser_r:
    if n % 2 == 0:
        print(n)