#3n +1

n = int(input("Numero: "))

while n != 1:
    if n % 2 == 1:
        n = 3 * n + 1
    elif n % 2 == 0:
        n = n / 2
print(n)