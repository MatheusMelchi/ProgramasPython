indice = float(input("Indice de Poluição: "))

if  0.4 > indice >= 0.3:
    print("Suspender 1 Grupo")
elif 0.5 > indice >=0.4:
    print("Suspender 1 e 2 Grupo")
elif indice >= 0.5:
    print("Suspender todos os Grupos")
else:
    print("Indice Seguro")