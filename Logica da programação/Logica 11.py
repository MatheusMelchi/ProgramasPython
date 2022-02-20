p = float(input("Peso do peixe: "))

if p > 50:
    e = p - 50
    m = float(e) * 4
    print("Valor da multa: ")
    print(m)
elif p <= 50:
    print("Sem multa")