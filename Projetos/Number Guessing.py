#Esse programa é um simples Number Guesser (um jogo de advinhação de numeros), é bem simples

import random
#Simples apresentação com input
numero_jogador = input("Bem-vindo ao jogo Number Guesser, por favor tente advinhar um numero de 1 a 10 \nNumero: ")
#Lista de numeros possiveis e em baixo a sua "randomificação"
lista_numeros = range(11)

n = (random.choice(lista_numeros))
#Checagem basica pra ver se o numero é igual ao numero aleatorio
if int(numero_jogador) == int(n):
    print("Parabens você acertou")
elif int(numero_jogador) != int(n):
    print("Tente novamente :(")

print(n)


#Seria bem simples aumentar ou diminuir a quantidade de numeros (so alterar a lista)