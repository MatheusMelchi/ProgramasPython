num = int(input("Numero Natural: "))

if num <= 0:
    print("Numero Invalido")

for n in range(1, num + 1):
    if num % n == 0:
        print(n)