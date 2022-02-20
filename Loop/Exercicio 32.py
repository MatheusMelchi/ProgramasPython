import random

d1 = range(1, 7)
d2 = range(1, 7)


n = int(input("Numero de vezes pra rolar os dados: "))


for num in range(1, n + 1):
    d1_random = random.choice(d1)
    d2_random = random.choice(d2)
    print(f"Dado 1: {d1_random} , Dado 2: {d2_random}")
    if d1_random > d2_random:
        print(f"{d1_random} > {d2_random}")
    elif d1_random < d2_random:
        print(f"{d1_random} <  {d2_random}")
    elif d1_random == d2_random:
        print(f"{d1_random} = {d2_random}")
