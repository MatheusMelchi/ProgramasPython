maior = -99999999
menor = 9999999
soma = 0

for i in range(1, 11):
    valor = int(input("Informe um Valor: "))
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        soma = soma + valor
    else:
        int(input("Informe um Valor: "))
media = soma / 10
print(f"O Maior numero é {maior}")
print(f"O Menor numero é {menor}")
print(f"A Media dos numeros é {media}")