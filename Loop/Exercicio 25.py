soma1 = 0
soma2 = 0
soma = 0
num = 0

for n in range(1, 1001):
    if n % 3 == 0 or n % 5 == 0:
        num = n
        print(num)
        soma = soma + num
print(soma)