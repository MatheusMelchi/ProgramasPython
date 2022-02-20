"""
Leia o salario de um trabalhador e o valor da prestação de um emprestimo.Se a prestação for maior que 20%
do salario do trabalhador imprima "Emprestimo nao concedido" se não imprima "Emprestimo concedido"
"""

s, p = input("Valor do salario, valor da prestação (respectivamente) ").split()

sp = float(s) / 100

if float(sp) * 20 <= float(p):
    print("Emprestimo não concedido ")
else:
    print("Emprestimo concedido")