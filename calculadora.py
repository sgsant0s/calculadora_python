import tkinter as tk
from tkinter import messagebox

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        messagebox.showerror("Erro", "Entrada inválida")

def button_divide():
    button_click('/')

def button_multiply():
    button_click('*')

def button_subtract():
    button_click('-')

def button_add():
    button_click('+')

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Campo de exibição
display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões numéricos
buttons = [
    (1, 3, 0), (2, 3, 1), (3, 3, 2),
    (4, 2, 0), (5, 2, 1), (6, 2, 2),
    (7, 1, 0), (8, 1, 1), (9, 1, 2),
    (0, 4, 0)
]

for (num, row, col) in buttons:
    button = tk.Button(root, text=str(num), padx=20, pady=20, command=lambda n=num: button_click(n))
    button.grid(row=row, column=col)

# Botões de operação
button_add = tk.Button(root, text="+", padx=19, pady=20, command=button_add)
button_subtract = tk.Button(root, text="-", padx=21, pady=20, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=21, pady=20, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=21, pady=20, command=button_divide)
button_equal = tk.Button(root, text="=", padx=47, pady=20, command=button_equal)
button_clear = tk.Button(root, text="C", padx=47, pady=20, command=button_clear)

# Posicionando os botões de operação
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=1)

# Iniciando o loop principal da interface
root.mainloop()
