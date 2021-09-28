import tkinter as tk
import inserir
from consultar import Consultar
from alterar import Alterar
from excluir import Excluir

LARGE_FONT = ("Verdana", 12)


class PaginaInicial(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CRUD", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Inserir",
                           command=lambda: controller.show_frame(inserir.Inserir))
        button.pack()

        button2 = tk.Button(self, text="Consultar",
                            command=lambda: controller.show_frame(Consultar))
        button2.pack()

        button3 = tk.Button(self, text="Alterar",
                            command=lambda: controller.show_frame(Alterar))
        button3.pack()

        button4 = tk.Button(self, text="Excluir",
                            command=lambda: controller.show_frame(Excluir))
        button4.pack()

