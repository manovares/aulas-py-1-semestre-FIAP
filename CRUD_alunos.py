import json

def main():
    lista_alunos = []

    opcao = 1

    while (opcao != 5):
        print("1 - Inserir um aluno")
        print("2 - Alterar um aluno")
        print("3 - Excluir um aluno")
        print("4 - Exibir um aluno")
        print("5 - Exportar os dados dos alunos para json")
        print("6 - Importar os dados dos alunos de um arquivo json para lista")
        print("7 - Sair")
        opcao = int(input("Digite a opcao desejada (1 a 7): "))

        if (opcao >= 1 and opcao <= 7):
            # Insercao de um aluno
            if (opcao == 1):
                # Chamada da funcao inserir_aluno
                inserir_aluno(lista_alunos)

            elif (opcao == 2):
                rm_alterar = int(input("Digite o RM do aluno que deseja alterar: "))
                indice = buscar_rm(lista_alunos,rm_alterar)

                if (indice != -1):
                    alterar_aluno(lista_alunos,indice)
                else:
                    print("RM nao encontrado")

            elif (opcao == 3):
                # Remocao de um aluno
                rm_excluir = int(input("Digite o RM do aluno que deseja excluir: "))
                indice = buscar_rm(lista_alunos, rm_excluir)

                if (indice != -1):
                    excluir_aluno(lista_alunos,indice)
                else:
                    print("RM nao encontrado")
            elif (opcao == 4):
                # Exibicao de todos os alunos
                rm = int(input("Digite o RM do aluno que deseja exibir: "))
                indice = buscar_rm(lista_alunos,rm)
                if (indice != -1):
                    exibir_aluno(lista_alunos,indice)
                else:
                    print("RM nao encontrado")
            elif (opcao == 5):
                exportar_json(lista_alunos) 
            elif (opcao == 6):
                importar_json(lista_alunos)

        else:
            print("Opcao invalida!")

# Funcoes do CRUD

def exportar_json(lista_alunos):
    nome_arquivo = input("Digite o nome do arquivo para exportar os dados (ex: alunos.json): ")
    if (len(lista_alunos) > 0):
        with open(nome_arquivo, 'w', encoding='utf-8') as arqAlunos:
            json.dump(lista_alunos,arqAlunos, ensure_ascii=False, indent="\n")
        print("Dados exportados com sucesso!")
    else:
        print("A lista de alunos esta vazia. Nao ha dados para exportar!")

def importar_json(lista_alunos):
    nome_arquivo = input("Digite o nome do arquivo para importar os dados (ex: alunos.json): ")
    lista_alunos.clear() # limpa a lista de alunos para receber os dados do arquivo json
    with open(nome_aquivo, 'r', encoding='utf-8') as arqAlunos:
        dados_arq = arqAlunos.read()
        lista_dados_json = json .loads(dados_arq)
        for aluno in lista_dados_json:
            lista_alunos.append(aluno)
    print("Dados importados com sucesso!")


def inserir_aluno (lista_alunos):
    try:
        rm = int(input("RM: "))
        indice = buscar_rm(lista_alunos, rm)
        while (indice != -1): # o rm que deseja inserir esta na lista
            rm = int(input("Esse RM ja esta cadastrado. Digite outro RM: "))
            indice = buscar_rm(lista_alunos, rm)
        nome = input("Nome: ")
        curso = input("Curso: ")
        mensalidade = float(input("Mensalidade: "))
    except ValueError:
        print("Digite valores numericos para o rm e a mensalidade!")
    else:
        dados_aluno = {
            'RM': rm,
            'Nome': nome,
            'Curso': curso,
            'Mensalidade': mensalidade
        }

        lista_alunos.append(dados_aluno)
        print("Dados inseridos com sucesso! ")

def buscar_rm (lista_alunos, rm_procurar):
    indice = -1
    for i in range(len(lista_alunos)):
        if (lista_alunos[i]['RM'] == rm_procurar):
            indice = i

    return(indice)

def alterar_aluno (lista_alunos, indice):
    try:
        print(f"Nome: {lista_alunos[indice]['Nome']}")
        nome = input("Digite o novo nome: ")
        print(f"Curso: {lista_alunos[indice]['Curso']}")
        curso = input("Digite o novo curso: ")
        print(f"Mensalidade: {lista_alunos[indice]['Mensalidade']}")
        mensalidade = float(input("Digite a nova mensalidade: "))
    except ValueError:
            print("Digite um valor numerico para a mensalidade!")
    else:
        lista_alunos[indice]['Nome'] = nome
        lista_alunos[indice]['Curso'] = curso
        lista_alunos[indice]['Mensalidade'] = mensalidade
        print("Dados alterados com sucesso! ")

def excluir_aluno (lista_alunos,indice):
    lista_alunos.pop(indice)
    print("Aluno exluido com sucesso!")

def exibir_aluno (lista_alunos,indice):
    for chave, valor in lista_alunos[indice].items():
        print(f"{chave}: {valor}")

# Chamada da funcao main
if (__name__ == "__main__"):
    main()