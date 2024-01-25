import tkinter as tk

def acender_luz():
    canvas.itemconfig(luz, fill='blue')

def apagar_luz():
    canvas.itemconfig(luz, fill='gray')

janela = tk.Tk()
janela.title("Botão de Luz")

canvas = tk.Canvas(janela, width=200, height=200)
canvas.pack()

# Crie uma "luz" representada por um círculo cinza
luz = canvas.create_oval(50, 50, 150, 150, fill='gray')

# Crie um botão para acender a luz
botao_acender = tk.Button(janela, text="Acender Luz", command=acender_luz)
botao_acender.pack()

# Crie um botão para apagar a luz
botao_apagar = tk.Button(janela, text="Apagar Luz", command=apagar_luz)
botao_apagar.pack()

janela.mainloop()
