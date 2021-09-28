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

class Alterar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Alterar Dados", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def alterarvalor():
            prnomea = NomeAE.get()
            prnovnome = NovnomeE.get()
            prnovemail = NovemailE.get()
            prnovsenha = NovsenhaE.get()
            try:
                alterar_dados = "UPDATE usuarios SET Nome = '{}', Email = '{}', Senha = '{}' WHERE Nome = '{}' ".format(
                    prnovnome, prnovemail, prnovsenha, prnomea)
                cursor = cnx.cursor()
                cursor.execute(alterar_dados)
                cnx.commit()
                Resultado['text'] = "Dados alterados com sucesso!"
            except Error:
                Resultado['text'] = "Aconteceu um erro."



        NomeAL = tk.Label(self, text="Nome Antigo")
        NomeAL.pack()
        NomeAE = tk.Entry(self, bd=5)
        NomeAE.pack()

        NovnomeL = tk.Label(self, text="Novo Nome")
        NovnomeL.pack()
        NovnomeE = tk.Entry(self, bd=5)
        NovnomeE.pack()

        NovemailL = tk.Label(self, text="Novo Email")
        NovemailL.pack()
        NovemailE = tk.Entry(self, bd=5)
        NovemailE.pack()

        NovsenhaL = tk.Label(self, text="Nova Senha")
        NovsenhaL.pack()
        NovsenhaE = tk.Entry(self, bd=5)
        NovsenhaE.pack()

        Resultado = tk.Label(self,text="")
        Resultado.pack()

        button2 = tk.Button(self, text="Alterar", command=alterarvalor)

        button2.pack()

        button1 = tk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(paginainicial.PaginaInicial))
        button1.pack()