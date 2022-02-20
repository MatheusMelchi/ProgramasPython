n = int(input("Numero: "))

#h(n) = 1 + 1/n...

nh = 1

for num in range(1, n + 1):
    nh = nh + 1/num
    print(nh)
