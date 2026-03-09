produtos = []

resp = 1
 
while (resp == 1):
    print("1 - inserir um produto")
    print("2 - alterar um produto")
    print("3 - exibir um produto")
    print("4 - excluir um produto")

    opc = int(input("Digite a opcao desejada (1 a 4): "))
    if(opc == 1):
        try:
            descricao = input("Digite a descrição do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            marca = input("Digite a marca do produto: ")
            valor = float(input("Digite o valor do produto: "))
        except ValueError:
            print("Digite valores numericos para a quantidade e valor do produto!")
        else:
            dados_produto = {
                'Descricao': descricao,
                'Quantidade': quantidade,
                'Marca': marca,
                'Valor': valor
            }
            produtos.append(dados_produto)
            print("Dados inseridos com sucesso!")
    elif(opc == 2):
        descricao_alterar = input("Digite a descrição do produto que deseja alterar os dados: ")
        for produto in produtos:
            if(produto['Descricao'] == descricao_alterar):
                try:
                    print(f"Quantidade: " [produto]['Quantidade'])
                    nova_quantidade = int(input("Digite a nova quantidade: "))
                    print(f"Marca: " [produto]['Marca'])
                    nova_marca = input("Digite a nova marca: ")
                    print(f"Valor: " [produto]['Valor'])
                    novo_valor = float(input("Digite o novo valor do produto: "))
                except ValueError:
                    print("Digite valores numericos para a quantidade e valor do produto!")
                else:
                    produto['Quantidade'] = nova_quantidade
                    produto['Marca'] = nova_marca
                    produto['Valor'] = novo_valor
                    print("Dados alterados com sucesso!")
            else:
                print("A descrição do produto não esta cadastrada!")
    elif(opc == 3):
        descricao_exibir = input("Digite a descrição do produto que deseja exibir os dados:")
        for produto in produtos:
            if(produto['Descricao'] == descricao_exibir):
                print(produto)
            else:   
                print("A descrição do produto não esta cadastrada!")
    elif(opc == 4):
        descricao_excluir = input("Digite a descrição do produto que deseja excluir os dados: ")
        for produto in produtos:
            if(produto['Descricao'] == descricao_excluir):
                produtos.remove(produto)
                print("Produto excluido com sucesso!")
            else:
                print("A descrição do produto não esta cadastrada!")