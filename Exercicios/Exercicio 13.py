"""
Faça um algoritimo que calcule a media ponderada de 3 notas.A primeira de peso 1 e a segunda peso 1 e a terceira peso 3.
Ao final mostrar a media do aluno e indicar se o aluno foi aprovado ou reprovado.

a media deve ser no minimo 60 para ser aprovado
"""

n1, n2, n3 = input("Notas prova ").split()

n3r = float(n3) * 2

na1 = float(n3r) + float(n2) + float(n1)

nar = float(na1) / 4

print(nar)

if float(nar) < 60.0:
    print("Aluno reprovado")
else:
    print("Aluno aprovado")