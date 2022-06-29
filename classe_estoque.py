from classe_produto import *


class Estoque:
    def __init__(self):
        self.listaProdutos = []
        self.listaProdutos.append(Produto(1, 'Notebook'))
        self.listaProdutos.append(Produto(2, 'Monitor'))

    def cadastrar_produtos(self):
        arg1 = len(self.listaProdutos)+1
        arg2 = input('Informe a descrição do produto')
        self.listaProdutos.append(Produto(arg1, arg2))

    def listar_produtos(self):
        for i in range(len(self.listaProdutos)):
            print(self.listaProdutos[i].cod, self.listaProdutos[i].descricao, self.listaProdutos[i].quantidade)
