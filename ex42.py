lista_clientes = []
 
resp = 1
 
while (resp == 1):
    print("1 - Inserir um cliente")
    print("2 - Alterar um cliente")
    print("3 - Exluir um cliente")
    print("4 - Exibir um cliente")
 
    opc = int(input("Digite a opcao desejada (1 a 4): "))
    if(opc == 1):
        try:
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            idade = int(input("Digite a idade do cliente: "))
            endereco= input("Digite o endereço: ")
            limite_credito = float(input("Digite o limite de credito do cliente: "))
        except ValueError:
            print("Digite valores numericos para a idade e limite de credito!")
        else:
            dados_cliente = {
                'Nome': nome,
                'CPF': cpf,
                'Idade': idade,
                'Endereco': endereco,
                'Limite_credito': limite_credito
            }
            lista_clientes.append(dados_cliente)
            print("Dados inseridos com sucesoo!")
    elif(opc == 2):
        nome_alterar = input("Digite o nome do cliente que deseja alterar os dados")
        indice = -1
        for i in range(len(lista_clientes)):
            if(lista_clientes[i]['Nome'] == nome_alterar):
                indice = 1
        if(indice != -1):
            try:
                print(f"CPF : "[lista_clientes][indice]['CPF'])
                novo_cpf = input("Digite o novo CPF: ")
                print(f"Idade!: "  [lista_clientes][indice]['Idade'])
                nova_idade = int(input("Digite a nova idade: "))
                print(f"Endereço: " [lista_clientes][indice]['Endereco'])
                novo_endereco = input("Digite o novo endereço: ")
                print(f"Limite de Credito:  " [lista_clientes][indice]['Limite_credito'])
                novo_limite_credito = float(input('Digite o novo limite de credito: '))
            except ValueError:
                print("Digite valores numericos para a idade e limite de credito!")
            else:
                lista_clientes[indice]['CPF'] = novo_cpf
                lista_clientes[indice]['Idade'] = nova_idade
                lista_clientes[indice]['Endereco'] = novo_endereco
                lista_clientes[indice]['Limite_credito'] = novo_limite_credito
                print("Dados alterados com sucesso!")
        else:
            print("O nome não esta cadastrado!")
    elif(opc == 3):
        nome_excluir = input("Digite o nome do cliente que você deseja exluir os dados: ")
 
        indice = -1
        for i in range(len(lista_clientes)):
            if (lista_clientes[i]['Nome'] == nome_excluir):
                indice = 1
        if(indice != -1):
            lista_clientes.pop(indice)
            print("Cliente excluido com sucesso!")
        else:
            print("O nome não esta cadastrado!")
    elif (opc == 4):
        exibir_nome = (input("Digite o nome do cliente que deseja verificar"))
        indice = -1
 
        for i in range(len(lista_clientes)):
            if (lista_clientes[i]['Nome'] == exibir_nome):
                indice = i
        if (indice != -1):
            for chave,valor in lista_clientes[indice].items():
                print(f"{chave} : {valor}")
        else:
            print("Cliente não encontrado")
    elif (opc == 5):
        for i in range(leg(lista_clientes)):
            if(lista_clientes[i]['Limite_credito'] > 1500):
                for chave,valor in lista_clientes[i].item():
                    print(f"{chave}: {valor}")
                print("--------------------")
    else:
        print("Opção invalida!")
 
    resp = int(input("Deseja continuar (1-SIM / 0 - NÃO)? "))
 