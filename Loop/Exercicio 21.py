n1 = int(input("Primeiro Numero: "))

n2 = int(input("Segundo Numero: "))

soma = 0
num1 = 0
num2 = 0
mult = 1

for n in range(n1, n2 + 1):
    if n % 2 == 0:
        num1 = n
        soma = soma + num1
for num in range(n1, n2 + 1):
    if num % 2 == 1:
        num2 = num
        mult = (mult * num2)

print(soma)
print(mult)



