import tkinter as tk
from mysql.connector import Error
import mysql.connector

LARGE_FONT = ("Verdana", 12)

try:
    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='crud')
except Error as erro:
    print(erro)

class AplicativoCrud(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)


        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (PaginaInicial,Inserir, Consultar, Alterar, Excluir):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PaginaInicial)

        
        mainloop()




    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class PaginaInicial(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CRUD", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Inserir",
                           command=lambda: controller.show_frame(Inserir))
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
                            command=lambda: controller.show_frame(PaginaInicial))
        button1.pack()

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
                            command=lambda: controller.show_frame(PaginaInicial))
        button1.pack()

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
                            command=lambda: controller.show_frame(PaginaInicial))
        button1.pack()

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
                            command=lambda: controller.show_frame(PaginaInicial))
        button1.pack()

