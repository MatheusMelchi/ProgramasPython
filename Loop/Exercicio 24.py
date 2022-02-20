num = int(input("Numero Natural: "))


if num <= 0:
    print("Numero Invalido")

soma = 0
num1 = 0

for n in range(1, num + 1):
    if n == num:
        n = 0
    elif num % n == 0:
        num1 = n
        soma = soma + num1
print(soma)
