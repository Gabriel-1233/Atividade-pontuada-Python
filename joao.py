import os
from dataclasses import dataclasses

os.system("cls || clear")

@dataclasses
class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    def __init__venda__(self, id, venda, produto):
        self.id = id
        self.venda = venda
        self.produto = produto

class Gestao:
    def __init__(self):
        self.produtos = []
        self.vendas = []

    def adicionar_produto(self, nome, preco):
        produto = produto(nome, preco)
        self.produtos.append(produto)
        