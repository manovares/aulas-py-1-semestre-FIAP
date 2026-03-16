funcionarios = []

def adicionar_funcionario(codigo, nome, idade, salario):
    funcionario = {
        'codigo': codigo,
        'nome': nome,
        'idade': idade,
        'salario': salario
    }
    funcionarios.append(funcionario)
    print("Funcionário adicionado com sucesso!")


def alterar_funcionario(codigo):
    for funcionario in funcionarios:
        if funcionario['codigo'] == codigo:
            try:
                print(f"Nome atual: {funcionario['nome']}")
                novo_nome = input("Digite o novo nome do funcionário: ")

                print(f"Idade atual: {funcionario['idade']}")
                nova_idade = int(input("Digite a nova idade: "))

                print(f"Salário atual: {funcionario['salario']}")
                novo_salario = float(input("Digite o novo salário: "))

            except ValueError:
                print("Digite valores numéricos para idade e salário!")
                return

            funcionario['nome'] = novo_nome
            funcionario['idade'] = nova_idade
            funcionario['salario'] = novo_salario

            print("Dados alterados com sucesso!")
            return

    print("Funcionário não encontrado.")


def exibir_funcionario(codigo):
    for funcionario in funcionarios:
        if funcionario['codigo'] == codigo:
            print("\nDados do funcionário:")
            print(f"Código: {funcionario['codigo']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Idade: {funcionario['idade']}")
            print(f"Salário: {funcionario['salario']}")
            return

    print("Funcionário não encontrado.")


def excluir_funcionario(codigo):
    for funcionario in funcionarios:
        if funcionario['codigo'] == codigo:
            funcionarios.remove(funcionario)
            print("Funcionário removido com sucesso!")
            return

    print("Funcionário não encontrado.")


def main():
    while True:
        print("\n1 - Adicionar funcionário")
        print("2 - Alterar funcionário")
        print("3 - Exibir funcionário")
        print("4 - Excluir funcionário")
        print("5 - Sair")

        try:
            opc = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opc == 1:
            codigo = int(input("Código: "))
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            salario = float(input("Salário: "))
            adicionar_funcionario(codigo, nome, idade, salario)

        elif opc == 2:
            codigo = int(input("Digite o código do funcionário: "))
            alterar_funcionario(codigo)

        elif opc == 3:
            codigo = int(input("Digite o código do funcionário: "))
            exibir_funcionario(codigo)

        elif opc == 4:
            codigo = int(input("Digite o código do funcionário: "))
            excluir_funcionario(codigo)

        elif opc == 5:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()