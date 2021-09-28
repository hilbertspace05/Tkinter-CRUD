import tkinter as tk
import mysql.connector
import paginainicial
from mysql.connector import Error

LARGE_FONT = ("Verdana", 12)

try:
    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='crud')
except Error as erro:
    print(erro)


class Inserir(tk.Frame):
    



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Inserir Dados", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def pegarvalor():
            prnome = NomeE.get()
            premail = EmailE.get()
            prsenha = SenhaE.get()
            try:
                inserir_dados = "INSERT INTO usuarios values('{}', '{}', '{}')".format(prnome, premail, prsenha)
                cursor = cnx.cursor()
                cursor.execute(inserir_dados)
                cnx.commit()
                Resultado['text'] = "Dados inseridos com sucesso!"
            except Error:
                Resultado['text'] = "Aconteceu um erro."

        NomeL = tk.Label(self, text="Nome")
        NomeL.pack()
        NomeE = tk.Entry(self, bd=5)
        NomeE.pack()

        EmailL = tk.Label(self, text="Email")
        EmailL.pack()
        EmailE = tk.Entry(self, bd=5)
        EmailE.pack()

        SenhaL = tk.Label(self, text="Senha")
        SenhaL.pack()
        SenhaE = tk.Entry(self, bd=5)
        SenhaE.pack()

        Resultado = tk.Label(self, text="")
        Resultado.pack()

        button2 = tk.Button(self, text="Inserir", command=pegarvalor)

        button2.pack()

        button1 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(paginainicial.PaginaInicial))
        button1.pack()


