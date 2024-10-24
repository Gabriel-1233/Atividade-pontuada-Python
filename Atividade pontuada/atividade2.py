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
    print("CPF inválido.")
    return 0

def listar_funcionarios():
    for func in lista_de_funcionarios:
        print(f"Nome: {func.nome_do_funcionario}, Sobrenome: {func.sobrenome_do_funcionario}, Idade: {func.idade_do_funcionario}, CPF: {func.cpf_do_funcionario}, Função: {func.funcao_do_funcionario}, Salário: {func.salario_do_funcionario}")

def atualizar_funcionario():
    pass

def demitir_funcionario():
    pass


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


