n = int(input("Horas Trabalhadas: "))

if n > 50:
    e = n - 50
    salario_base = (n - float(e)) * 10
    salario_extra = e * 20
    salario_total = float(salario_extra) + float(salario_base)
    print(f"O salario base é {salario_base}")
    print(f"O salario extra é {salario_extra}")
    print(f"O salario total é {salario_total}")
elif n <= 50:
    salario = n * 10
    print(f"O salario é {float(salario)}")
