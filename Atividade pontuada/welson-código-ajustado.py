import os
from dataclasses import dataclass

# Funções
def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Classe e lista
@dataclass
class Empresa:
    nome_produto: str
    produto: int
    preco_produto: float
    codigo_barras: int

lista_produto = []

# Limpando poluição visual
limpa_tela()

# Cadastro do produto
print("""
1- Cadastro de produtos para a venda.
2- Exibir o inventário da empresa.
3- Atualização do sistema de vendas.
4- Buscar produto.
5- Fechar sistema.
""")

opcao_menu = int(input("Digite um número correspondente à opção acima:"))

match opcao_menu:
    case 1:
        print("Cadastramento do produto.")
        empresa = Empresa(
            nome_produto=input("Digite o nome do seu produto:"),
            produto=int(input("Digite a quantidade do produto no estoque:")),
            preco_produto=float(input("Digite o preço do seu produto:")),
            codigo_barras=int(input("Digite o código de barras do produto:"))
        )
        lista_produto.append(empresa)
        # Gravar os dados no arquivo
        nome_do_arquivo = "carteira_de_cadastro_da_empresa.txt"
        with open(nome_do_arquivo, "a") as arquivo:
            arquivo.write(f"{empresa.nome_produto},{empresa.preco_produto},{empresa.produto},{empresa.codigo_barras}\n")

    case 2:
        print("Exibindo o inventário da empresa e seus componentes.")
        if not lista_produto:
            print("Nenhum produto cadastrado.")
        else:
            for empresa in lista_produto:
                print(f"Nome do produto: {empresa.nome_produto}")
                print(f"Quantidade: {empresa.produto}")
                print(f"Valor do produto: R${empresa.preco_produto:.2f}")
                print(f"Código do produto: {empresa.codigo_barras}")

    case 3:
        print("Exibindo estoque da empresa.")
        if not lista_produto:
            print("Nenhum produto cadastrado.")
        else:
            for empresa in lista_produto:
                print(f"Nome do produto: {empresa.nome_produto}")
                print(f"Quantidade: {empresa.produto}")
                print(f"Valor do produto: R${empresa.preco_produto:.2f}")
                print(f"Código do produto: {empresa.codigo_barras}")

    case 4:
        print("Buscando produto no estoque.")
        busca_produto = input("Digite o nome ou o código de barras do produto para buscar: ")
        produto_encontrado = None

        for empresa in lista_produto:
            if empresa.nome_produto == busca_produto or str(empresa.codigo_barras) == busca_produto:
                produto_encontrado = empresa
                break

        if produto_encontrado:
            print(f"Produto encontrado:")
            print(f"O nome do produto: {produto_encontrado.nome_produto}")
            print(f"A quantidade do produto em estoque: {produto_encontrado.produto}")
            print(f"O preço do produto: R${produto_encontrado.preco_produto:.2f}")
            print(f"Código de barras do produto: {produto_encontrado.codigo_barras}")
        else:
            print("Produto não encontrado.")

    case 5:
        print("Fechando sistema.")
        exit()

    case _:
        print("Opção inválida!")
