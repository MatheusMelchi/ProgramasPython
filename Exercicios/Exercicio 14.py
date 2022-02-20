"""
Trabalho laboratorio peso:2, avaliação semestral peso:3, exame final peso:5
"""

TL, AS, EF = input("Notas aluno ").split()

TLP = float(TL) * 2

ASP = float(AS) * 3

EFP = float(EF) * 5

NFS = float(EFP) + float(ASP) + float(TLP)

NF = float(NFS) / 10

print(NF)

if float(NF) <= 2.9:
    print("Aluno reprovado")
elif 2.9 < float(NF) <= 4.9:
    print("Aluno de recuperação")
else:
    print("Aluno aprovado")