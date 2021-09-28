import tkinter as tk

janela = tk.Tk()
janela.title("CRUD")

janela.rowconfigure(1, minsize=300, weight=1)
janela.columnconfigure(1, minsize=300, weight=1)


var = tk.StringVar()
label = tk.Label(janela, textvariable=var)
botinserir = tk.Button(janela, text="Inserir")
botconsultar = tk.Button(janela, text="Consultar")
botalterar = tk.Button(janela, text="Alterar")
botexcluir = tk.Button(janela, text="Excluir")

var.set("Selecione uma opção para banco de dados: ")
label.pack()
botinserir.pack(expand=True)
botconsultar.pack(expand=True)
botalterar.pack(expand=True)
botexcluir.pack(expand=True)


janela.mainloop()