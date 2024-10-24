import os
from sqlalchemy import create_engine, Column, String, Integer 
from sqlalchemy.orm import sessionmaker, declarative_base
from dataclasses import dataclass

#Funções
def limpa_tela():
    os.system("cls || clear")
    
#Class
@dataclass
class Empresa:
    nome_produto:str
    produto:int
    preco_produto:float
    codigo_barras:int
#Lista 
lista_produto=[]
#cadastro do produto
print("""
1-Cadastro de produtos para a venda.
2-Atualização do Sistema de vendas.
3-Exibir o inventario da empresa.
4-Buscar produto.
5-Fechar sistema.
      """)
opcao_menu=int(input("Digite um numero correspondente a opção acima:"))
match(opcao_menu):
    case 1:
        print("Cadastramento do produto.")
        empresa=Empresa(
    nome_produto=input("Digite o nome do seu produto:"),
    produto=int(input("Digite a quantidade do produto no estoque:")),
    preco_produto=float(input("Digite o preço do seu produto:")),
    codigo_barras=int(input("Digite o código de barras do produto:"))  
)
        lista_produto.append(empresa)
    case 2:
        print("Atualização do sistema.")
        
