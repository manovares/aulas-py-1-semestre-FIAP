def main():
    lista_funcionarios = []
    resp = 1

    while(resp == 1):
        print("1 - Inserir Funcionario")
        print("2 - Alterar Funcionario")
        print("3 - Excluir Funcionario")
        print("4 - Exibir Funcionario")
        opc = int(input("Digite a opção desejada: "))

        if opc == 1:
            inserir_funcionarios(lista_funcionarios)
        elif opc == 2:
            codigo_alterar = int(input("Digite o código do funcionário a ser alterado: "))
            indice = buscar_funcionario(lista_funcionarios, codigo_alterar)
            if (indice != -1):
                alterar_funcionario(lista_funcionarios,indice)
            else:
                print("Funcionário não encontrado.")
        elif opc == 3:
            codigo_excluir = int(input("Digite o código do funcionário a ser excluído: "))
            indice = buscar_funcionario(lista_funcionarios, codigo_excluir)
            if (indice != -1):
                excluir_funcionario(lista_funcionarios, indice)
            else:
                print("Funcionário não encontrado.")
        elif opc == 4:
            codigo_exibir = int(input("Digite o código do funcionário a ser exibido: "))
            indice = buscar_funcionario(lista_funcionarios, codigo_exibir)
            if (indice != -1):
                exibir_funcionarios(lista_funcionarios, indice)
            else:
                print("Funcionário não encontrado.")
        else:
            print("Opção inválida. Digite uma opção entre 1 e 4.")
        
        resp = int(input("Deseja continuar? (1 - Sim / 0 - Não): "))

def buscar_funcionario(lista_funcionarios,codigo):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if lista_funcionarios[i]['Codigo'] == codigo:
            indice = i
    return indice

def inserir_funcionarios(lista_funcionarios):
    try:
        codigo = int(input("Digite o código do funcionário: "))
        indice = buscar_funcionario(lista_funcionarios, codigo)
        while indice != -1:
            print("Código já existe. Digite outro código.")
            codigo = int(input("Digite o código do funcionário: "))
            indice = buscar_funcionario(lista_funcionarios, codigo)
        nome = input("Digite o nome do funcionário: ")
        idade = int(input("Digite a idade do funcionário: "))
        salario = float(input("Digite o salário do funcionário: "))
    except ValueError:
        print("Digite valores numericos para codigo, idade e salario.")
    else:
        dados_funcionario = {'Codigo': codigo, 'Nome': nome, 'Idade': idade, 'Salario': salario}
        lista_funcionarios.append(dados_funcionario)   

def alterar_funcionario(lista_funcionarios,indice):
    try:
        print(f"Nome: {lista_funcionarios[indice]['Nome']}")
        novo_nome = input("Digite o novo nome do funcionário: ")
        print(f"Idade: {lista_funcionarios[indice]['Idade']}")
        nova_idade = int(input("Digite a nova idade do funcionário: "))
        print(f"Salário: {lista_funcionarios[indice]['Salario']}")
        novo_salario = float(input("Digite o novo salário do funcionário: "))
    except ValueError:
        print("Digite valores numericos para idade e salario.")
    else:
        lista_funcionarios[indice]['Nome'] = novo_nome
        lista_funcionarios[indice]['Idade'] = nova_idade
        lista_funcionarios[indice]['Salario'] = novo_salario
        print("Funcionário alterado com sucesso.")

def excluir_funcionario(lista_funcionarios,indice):
    lista_funcionarios.pop(indice)
    print("Funcionário excluído com sucesso.")

def exibir_funcionarios(lista_funcionarios,indice):
    for chave,valor in lista_funcionarios[indice].items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    main()