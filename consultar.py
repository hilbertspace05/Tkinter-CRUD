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


class Consultar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Consultar Dados", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def consultarvalor():
            prnome = NomeE.get()
            try:
                consultar_dados = "SELECT Nome, Email, Senha FROM usuarios WHERE Nome = '{}' ".format(prnome)
                cursor = cnx.cursor()
                cursor.execute(consultar_dados)
                dados = cursor.fetchall()
                GuiaResultado['text'] = "Nome, Email e Senha: "
                Resultado['text'] = dados
            except Error:
                Resultado['text'] = "Aconteceu um erro."




        NomeL = tk.Label(self, text="Nome")
        NomeL.pack()
        NomeE = tk.Entry(self, bd=5)
        NomeE.pack()

        GuiaResultado = tk.Label(self,text="")
        GuiaResultado.pack()

        Resultado = tk.Label(self,text="")
        Resultado.pack()

        button2 = tk.Button(self, text="Consultar", command=consultarvalor)

        button2.pack()

        button1 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(paginainicial.PaginaInicial))
        button1.pack()