numero = int(input("Tabuada do: "))

while numero > 10:
    print("A Tabuada so pode ir ate o 10")
    numero = int(input("Tabuada do: "))
for i in range(1, 11):
    valor = numero * i
    print(f"{numero} * {i} = {valor}")