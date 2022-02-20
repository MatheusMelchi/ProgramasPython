#Este programa é um simples dice rolling (rolador de dados) vou tentar colocar mais que o dado simples.

import random

usuario_escolha = input("Por favor escolha qual dado deseja ser rolado: \n 1- dado comum \n 2- dado 20 lados \n")
#Lista de numeros para dado de 6 lados
dado_6 = list(range(1, 7))
#Este é o random6 ou r6 uma variavel basica que na realidade é o proprio rolamento do dado de 6 lados.
r6 = (random.choice(dado_6))
#Lista para dado de 20 lados
dado_20 = list(range(1, 21))
#Novamente o resultado randomico do dado de 20 lados
r20 = (random.choice(dado_20))

#Checagem para seleção de dado (ou D6 ou D20), alem de uma mensagem se a seleção for invalida
if int(usuario_escolha) == 1:
    print(r6)
elif int(usuario_escolha) == 2:
    print(r20)
else:
    print("Escolha Invalida")

