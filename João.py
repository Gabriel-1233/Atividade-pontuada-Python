# Lista onde vamos armazenar todas as vendas
vendas = []

# Função para registrar uma nova venda
def registrar_venda():
    produto = input("Produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço por unidade: "))
    # Adiciona a venda como um dicionário dentro da lista vendas
    vendas.append({"produto": produto, "quantidade": quantidade, "preco": preco})
    print("Venda registrada!\n")

# Função para consultar todas as vendas
def consultar_vendas():
    if vendas:
        print("\n--- Vendas Registradas ---")
        for i, venda in enumerate(vendas, start=1):
            print(f"{i}. Produto: {venda['produto']}, Quantidade: {venda['quantidade']}, Preço: {venda['preco']:.2f}")
        print("--------------------------\n")
    else:
        print("Nenhuma venda registrada.\n")

# Função para calcular o total de vendas
def total_vendas():
    total = sum(venda["quantidade"] * venda["preco"] for venda in vendas)
    print(f"Total arrecadado: R${total:.2f}\n")

# Função para atualizar uma venda específica
def atualizar_venda():
    consultar_vendas()
    numero = int(input("Número da venda para atualizar: ")) - 1
    if 0 <= numero < len(vendas):
        produto = input("Novo produto (ou Enter para manter): ") or vendas[numero]["produto"]
        quantidade = input("Nova quantidade (ou Enter para manter): ")
        preco = input("Novo preço (ou Enter para manter): ")

        # Atualiza apenas se o usuário digitar um novo valor
        vendas[numero]["produto"] = produto
        vendas[numero]["quantidade"] = int(quantidade) if quantidade else vendas[numero]["quantidade"]
        vendas[numero]["preco"] = float(preco) if preco else vendas[numero]["preco"]
        print("Venda atualizada!\n")
    else:
        print("Venda não encontrada.\n")

# Função para excluir uma venda específica
def excluir_venda():
    consultar_vendas()
    numero = int(input("Número da venda para excluir: ")) - 1
    if 0 <= numero < len(vendas):
        vendas.pop(numero)  # Remove a venda pelo índice
        print("Venda excluída!\n")
    else:
        print("Venda não encontrada.\n")

# Menu principal
def menu():
    while True:
        print("1. Registrar venda")
        print("2. Consultar vendas")
        print("3. Total de vendas")
        print("4. Atualizar venda")
        print("5. Excluir venda")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            registrar_venda()
        elif opcao == "2":
            consultar_vendas()
        elif opcao == "3":
            total_vendas()
        elif opcao == "4":
            atualizar_venda()
        elif opcao == "5":
            excluir_venda()
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o programa
menu()
