import tkinter as tk
import mysql.connector
from mysql.connector import Error
import paginainicial

LARGE_FONT = ("Verdana", 12)

try:
    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='crud')
except Error as erro:
    print(erro)

class Excluir(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Excluir Dados", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def excluirvalor():
            prnome = NomeE.get()
            try:
                deletar_dados = "DELETE FROM usuarios WHERE Nome = '{}' ".format(prnome)
                cursor = cnx.cursor()
                cursor.execute(deletar_dados)
                cnx.commit()
                Resultado['text'] = "Dados excluídos com sucesso!"
            except Error:
                Resultado['text'] = "Aconteceu um erro."

        NomeL = tk.Label(self, text="Nome")
        NomeL.pack()
        NomeE = tk.Entry(self, bd=5)
        NomeE.pack()

        Resultado = tk.Label(self,text="")
        Resultado.pack()

        button2 = tk.Button(self, text="Excluir", command=excluirvalor)

        button2.pack()

        button1 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(paginainicial.PaginaInicial))
        button1.pack()