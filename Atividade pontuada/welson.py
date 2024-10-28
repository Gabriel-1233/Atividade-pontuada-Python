import os
from sqlalchemy import create_engine, Column, String, Integer 
from sqlalchemy.orm import sessionmaker, declarative_base
from dataclasses import dataclass

#Funções
def limpa_tela():
    os.system("cls || clear")
    
#Class e lista
@dataclass
class Empresa:
    nome_produto:str
    produto:int
    preco_produto:float
    codigo_barras:int
lista_produto=[]

#Limpando poluição visual
limpa_tela()
#cadastro do produto
print("""
1-Cadastro de produtos para a venda.
2-Exibir o inventario da empresa.
3-Atualização do sistema de vendas.
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
    
    # Gravar os dados no arquivo
        nome_do_arquivo = "carteira_de_cadasto_da_empresa.txt"
        with open(nome_do_arquivo, "a") as arquivo:
            arquivo.write(f"{empresa.nome_produto},{empresa.preco_produto},{empresa.produto},{empresa.codigo_barras}\n")
            
    
    case 2:
        print("\\exinbindo o inventario da empresa e seus componentes.")
        
        if not lista_produto:
            print("Nenhum habitante cadastrado.")
        else:
            valor_do_produto=(empresa.valor_produto for empresa in lista_produto)
            nome_do_produto=(empresa.nome_produto for empresa in lista_produto)
            estoque_de_produtos=(empresa.estoque_produto for empresa in lista_produto)
            codigo_do_produto=(empresa.estoque_produto for empresa in lista_produto)
            
            print(f"O Nome do produto: {nome_do_produto}")
            print(f"Quantidade: {estoque_de_produtos}")
            print(f"O Valor do produto:R${valor_do_produto:.2f}")
            print(f"O código do produto: {codigo_do_produto}")
    
    case 3:
        print("Exibindo estoque da empresa.")
        
        
        
