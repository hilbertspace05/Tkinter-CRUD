import tkinter as tk
import paginainicial
import inserir
from consultar import Consultar
from alterar import Alterar
from excluir import Excluir


class AplicativoCrud(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)


        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (paginainicial.PaginaInicial,inserir.Inserir, Consultar, Alterar, Excluir):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(paginainicial.PaginaInicial)





    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


