from aplicativocrud import AplicativoCrud
from inserir import Inserir
from consultar import Consultar
from paginainicial import PaginaInicial
from alterar import Alterar
from excluir import Excluir



PaginaInicial(None, controller= None)

Inserir(None, controller= None) #controller= lambda: paginainicial.PaginaInicial


Consultar(None, controller= None)

Alterar(None, controller= None)

Excluir(None, controller= None)




app = AplicativoCrud(None)

app.mainloop()


