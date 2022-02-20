qtd = int(input("Quantidade de numeros: "))

maior = -999999999999
menor = 9999999999999

for n in range(1, qtd + 1):
    num = int(input(f"Informe o {n}/{qtd} valor: "))
    if num > maior:
        maior = num
        qtd_maior = 0
    elif num == maior:
        qtd_maior += 1
    elif num < menor:
        menor = num

print(maior)
print(menor)
print(qtd_maior + 1)
