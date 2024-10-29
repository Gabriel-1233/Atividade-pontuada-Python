from dataclasses import dataclass
import random
import os

@dataclass
class Funcionario:
    nome_do_funcionario: str
    sobrenome_do_funcionario: str
    idade_do_funcionario: int
    cpf_do_funcionario: int
    funcao_do_funcionario: str
    salario_do_funcionario: float

def limpar_tela():
    os.system("Cls || clear")

def cadastrar_funcionario():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    idade = random.randint(1, 99)
    cpf = random.randint(1, 1000000)
    funcao = "Desempregado"
    salario = 0

    print("""=== Funções ===
    1 - Dono da Loja
    2 - Sócio da Loja
    3 - Gerente da Loja
    4 - Vendedor da Loja
    5 - Segurança da Loja
    """)
    
    opcao = int(input("Digite sua função: "))
    if opcao == 1:
        funcao = "Dono da Loja"
        salario = 7000
    elif opcao == 2:
        funcao = "Sócio da Loja"
        salario = 6000
    elif opcao == 3:
        funcao = "Gerente da Loja"
        salario = 5000
    elif opcao == 4:
        funcao = "Vendedor da Loja"
        salario = 1412.10
    elif opcao == 5:
        funcao = "Segurança da Loja"
        salario = 2115.00
    
    funcionario = Funcionario(nome_do_funcionario=nome, sobrenome_do_funcionario=sobrenome, idade_do_funcionario=idade, cpf_do_funcionario=cpf, funcao_do_funcionario=funcao, salario_do_funcionario=salario)
    lista_de_funcionarios.append(funcionario)
    limpar_tela()
    return lista_de_funcionarios

def buscar_funcionario():
    cpf = int(input("Digite o seu CPF: "))
    limpar_tela()
    for func in lista_de_funcionarios:
        if cpf == func.cpf_do_funcionario:
            print(f"Nome: {func.nome_do_funcionario}\nSobrenome: {func.sobrenome_do_funcionario}\nIdade: {func.idade_do_funcionario}")
            print(f"CPF: {func.cpf_do_funcionario}\nFunção: {func.funcao_do_funcionario}\nSalário: {func.salario_do_funcionario}")
            return func
        if not cpf == func.cpf_do_funcionario:
            print("CPF inválido.")
            return 0

def listar_funcionarios():
    if lista_de_funcionarios == []:
        print("Lista vazia ! ")
    for func in lista_de_funcionarios:
        print(f"Nome: {func.nome_do_funcionario}, Sobrenome: {func.sobrenome_do_funcionario}, Idade: {func.idade_do_funcionario}, CPF: {func.cpf_do_funcionario}, Função: {func.funcao_do_funcionario}, Salário: {func.salario_do_funcionario}")
def atualizar_funcionario():
    cpf = int(input("Digite o CPF do funcionário que deseja atualizar: "))
    limpar_tela()
    for func in lista_de_funcionarios:
        if cpf == func.cpf_do_funcionario:
            print(f"Nome atual: {func.nome_do_funcionario}")
            novo_nome = input("Novo nome (pressione Enter para manter o atual): ")
            if novo_nome:
                func.nome_do_funcionario = novo_nome

            print(f"Sobrenome atual: {func.sobrenome_do_funcionario}")
            novo_sobrenome = input("Novo sobrenome (pressione Enter para manter o atual): ")
            if novo_sobrenome:
                func.sobrenome_do_funcionario = novo_sobrenome

            print(f"Função atual: {func.funcao_do_funcionario}")
            nova_funcao = input("Nova função (pressione Enter para manter a atual): ")
            if nova_funcao:
                func.funcao_do_funcionario = nova_funcao

            print(f"Salário atual: {func.salario_do_funcionario}")
            novo_salario = input("Novo salário (pressione Enter para manter o atual): ")
            if novo_salario:
                func.salario_do_funcionario = float(novo_salario)
            
            limpar_tela()
            print("Funcionário atualizado com sucesso.")
            return func
    print("Funcionário não encontrado.")


def demitir_funcionario():
    cpf = int(input("Digite o CPF do funcionário que deseja demitir: "))
    limpar_tela()
    for func in lista_de_funcionarios:
        if cpf == func.cpf_do_funcionario:
            lista_de_funcionarios.remove(func)
            print(f"Funcionário com CPF {cpf} foi demitido com sucesso.")
            return func
    print("Funcionário não encontrado.")



lista_de_funcionarios = []
while True:
        print("""
        === Sistema de Funcionários ===
        1 - Cadastrar um funcionário
        2 - Listar funcionários
        3 - Atualizar um funcionário
        4 - Buscar funcionário
        5 - Demitir um funcionário
        6 - Sair do sistema
        """)
        
        escolha = int(input("Digite a opção: "))
        if escolha == 1:
            lista_de_funcionarios = cadastrar_funcionario()
        elif escolha == 2:
            listar_funcionarios()
        elif escolha == 3:
            atualizar_funcionario()
        elif escolha == 4:
            buscar_funcionario()
        elif escolha == 5:
            demitir_funcionario()
        elif escolha == 6:
            break


