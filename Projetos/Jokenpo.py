#Este programa é um simples pedra, papel, tesoura

import random

lista_computador = [1, 2, 3]

j = input("Por favor, escolha:\n 1- Pedra\n 2- Papel\n 3- Tesoura\n Escolha: ")

lista_computador_aleatorio = random.choice(lista_computador)

#print(lista_computador_aleatorio)



if int(j) == int(lista_computador_aleatorio):
    print("Empate")
elif int(j) == 1 and int(lista_computador_aleatorio) == 2:
    print("Pedra vs Papel\nVocê Perdeu!")
elif int(j) == 1 and int(lista_computador_aleatorio) == 3:
    print("Pedra vs Tesoura\nVocê Ganhou!")
elif int(j) == 2 and int(lista_computador_aleatorio) == 3:
    print("Papel vs Tesoura\nVocê Perdeu!")
elif int(j) == 2 and int(lista_computador_aleatorio) == 1:
    print("Papel vs Pedra\n Você Ganhou")
elif int(j) == 3 and int(lista_computador_aleatorio) == 1:
    print("Tesoura vs Pedra\nVocê Perdeu!")
elif int(j) == 3 and int(lista_computador_aleatorio) == 2:
    print("Tesoura vs Papel\nVocê Ganhou!")



"""
if jogador_escolha == 1 or "pedra" or "Pedra":
    jogador_escolha = 1
elif jogador_escolha == 2 or "papel" or "Papel":
    jogador_escolha = 2
elif jogador_escolha == 3 or "tesoura" or "Tesoura":
    jogador_escolha = 3
else:
    print("Opção invalida")

if lista_computador_random == 1 or "pedra" or "Pedra":
    lista_computador_random = 1
elif lista_computador_random == 2 or "papel" or "Papel":
    lista_computador_random = 2
elif lista_computador_random == 3 or "tesoura" or "Tesoura":
    lista_computador_random = 3
    
if jogador_escolha == lista_computador_random:
    print("Empate!")
elif lista_computador_random == 1 and jogador_escolha == 2:
    print("Papel vs pedra:\nVocê Venceu!")
elif lista_computador_random == 1 and jogador_escolha == 3:
    print("Tesoura vs Pedra:\nVocê Perdeu!")
elif lista_computador_random == 2 and jogador_escolha == 3:
    print("Tesoura vs papel:\nVocê Venceu!")
elif lista_computador_random == 2 and jogador_escolha == 1:
    print("Pedra vs Papel:\nVocê Perdeu!")
elif lista_computador_random == 3 and jogador_escolha == 1:
    print("Pedra vs Tesoura:\nVocê Venceu!")
elif lista_computador_random == 3 and jogador_escolha == 2:
    print("Papel vs Tesoura:\nVocê Perdeu!")

"""