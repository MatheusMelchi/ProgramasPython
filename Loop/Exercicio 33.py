i, j = input("Dois Numeros Naturais: ").split()

n = int(input("Numero: "))

i = int(i)
j = int(j)

for num in range(1, n + 1):
    if j % num == 0:
        print(num)
    elif i % num == 0:
        print(num)
    elif num % j == 0:
        print(num)
    elif num % i == 0:
        print(num)

