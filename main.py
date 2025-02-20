import tkinter as tk
def calcular(operacao):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                result_label.config(text="Erro: Divisão por zero")
                return
        result_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        result_label.config(text="Erro: Insira números válidos")


janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x200")


tk.Label(janela, text="Primeiro número:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(janela)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(janela, text="Segundo número:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(janela)
entry2.grid(row=1, column=1, padx=5, pady=5)


operacoes = {'+': (2, 0), '-': (2, 1), '*': (3, 0), '/': (3, 1)}
for op, (linha, col) in operacoes.items():
    tk.Button(janela, text=op, command=lambda o=op: calcular(o), width=5).grid(row=linha, column=col, padx=5, pady=5)


result_label = tk.Label(janela, text="Resultado: ")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


janela.mainloop()