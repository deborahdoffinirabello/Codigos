#id global com meu RU
id_global = 5153693
#criando a lista de funcionarios
lista_funcionarios = []

#função de cadastro de funcionario
def cadastrar_funcionario(id):
    print('ID do funcionário: ', id)
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    try:
        salario = float(input("Digite o salário do funcionário: "))
    except ValueError:
        print("Salário inválido. Cadastro cancelado.")
        return

    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }

    lista_funcionarios.append(funcionario.copy())
    print("Funcionário cadastrado com sucesso!\n")

#função para deletar funcionario da lista
def remover_funcionario():
    while True:
        try:
            id_remover = int(input("Digite o ID do funcionário a ser removido: "))
        except ValueError:
            print("ID inválido.")
            continue

        for i, func in enumerate(lista_funcionarios):
            if func["id"] == id_remover:
                del lista_funcionarios[i]
                print("Funcionário removido com sucesso.")
                return
        print("Id inválido. Tente novamente.") 
        
#função de consulta
def consultar_funcionarios():
    """
    Permite consultar os funcionários com base em diferentes critérios.
    """
    while True:
        print("\nCONSULTA DE FUNCIONÁRIOS")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if not lista_funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                for func in lista_funcionarios:
                    print(func)

        elif opcao == "2":
            try:
                id_busca = int(input("Digite o ID do funcionário: "))
            except ValueError:
                print("ID inválido.")
                continue

            encontrado = False
            for func in lista_funcionarios:
                if func["id"] == id_busca:
                    print(func)
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")

        elif opcao == "3":
            setor_busca = input("Digite o setor: ")
            encontrados = [func for func in lista_funcionarios if func["setor"].lower() == setor_busca.lower()]
            if encontrados:
                for func in encontrados:
                    print(func)
            else:
                print("Nenhum funcionário encontrado nesse setor.")

        elif opcao == "4":
            return 

        else:
            print("Opção inválida!")

#mensagem de bem vindo e nome seguido do código principal
print('bem vindo a empresa de Déborah Rabello')
while True:
    print("\nMENU PRINCIPAL")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")

    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == "1":
        cadastrar_funcionario(id_global)
        id_global += 1  

    elif opcao_menu == "2":
        consultar_funcionarios()

    elif opcao_menu == "3":
        remover_funcionario()

    elif opcao_menu == "4":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida!")
