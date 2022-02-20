import tkinter as tk
import soma_funçoes
# Funções





# Testes

def funcao_teste():
    print("Funcionando botão")

# Algumas Variaveis Necessarias
Altura = 600
Largura = 700

# Uma Raiz para começar
root = tk.Tk()

def get_value(entry):
    value = entry.get()
    try:
        return int(value)
    except ValueError:
        return None

# Uma tela branca que configura a altura e largura
canvas = tk.Canvas(root, height=Altura, width=Largura)
canvas.pack()

entry = tk.Entry(canvas, bd=5)
entry.place(relx=0.25, rely=0.15, relheight=0.1, relwidth=0.5)

conversion = get_value(entry)
if conversion is not None:
    conversion = int(conversion)


# O local na tela onde os botões vao ficar
frame = tk.Frame(root, bg="blue")
frame.place(relx=0.25, rely=0.25, relheight=0.22, relwidth=0.5)
# Botão 1 = + (soma)
button = tk.Button(frame, text="+", bg="white", fg="black", activebackground="#B0B4B2", bd=4, height=8, width=10, command=lambda : soma_funçoes.soma(conversion))
button.grid(column=1, row=1)
# Botão 2 = - (subtração)
button2 = tk.Button(frame, text="-", bg="white", fg="black", activebackground="#B0B4B2", bd=4, height=8, width=11)
button2.grid(column=2, row=1)
# Botão 3 = / (divisão)
button3 = tk.Button(frame, text="/", bg="white", fg="black", activebackground="#B0B4B2", bd=4, height=8, width=11)
button3.grid(column=3, row=1)
# Botão 4 = * [multiplicação)
button4 = tk.Button(frame, text="*", bg="white", fg="black", activebackground="#B0B4B2", bd=4, height=8, width=11)
button4.grid(column=4, row=1)
# Onde o Resultado vai ficar
resultado = tk.Label(canvas, )

root.mainloop()
