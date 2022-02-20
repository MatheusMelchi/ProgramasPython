i, t = input("Idade e Tempo de trabalho respectivamente ").split()

if int(i) >= 65 or int(t) >= 30 or int(i) >= 60 and int(t) >= 25:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar ainda")

#O or funcionou aqui por algum motivo