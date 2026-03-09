#import para limpar conteudos irrelevantes do sistema 
import os

#lista para adicionar os dentistas que trabalham na turma do bem
dentistas = []

#função para adicionar os dentistas no sistema
def adicionaDentista(dentista):
    novoDentista = (dentista)
    dentistas.append(novoDentista)

#função para mostrar quais são os dentistas cadastrados ou se não tem cadastro
def exibeDentistas():
    if not dentistas:
        print('A lista está vazia')
        return
    for dentista in dentistas:
        print(f'{dentista}')

#função para remover dentistas cadastrados
def removerDentista(dentista):
    global dentistas
    if removerDentista:
        for dentista in dentistas:
            dentistas = [ t for t in dentistas if t != dentista ]
            print(f'O Dentista removido: {dentista}')
            break
        else:
            print(f'Dentista não encontrado: {dentista}')

#função para buscar o dentista cadastrado
def buscarDentista(dentista):
    resultado = [ t for t in dentistas if t.lower() == dentista.lower()]
    if resultado:
        for titulo in resultado:
            print(f'Dentista encontrado: {titulo}') 
    else: 
        print(f'Dentista não encontrado: {dentista}')
    
#sistema funcionando:
while True:
    os.system('cls || clear')
    print('Boas vindas ao gerenciador de Dentistas')
    print()
    print('O que você deseja fazer?')
    print('1 - Listar dentistas')
    print('2 - Adicionar dentista')
    print('3 - Remover dentista')
    print('4 - Buscar dentista')
    print('0 - Sair')
    opcao = int(input('Digite uma opção: '))

    match opcao:
        case 1:
            exibeDentistas()
        case 2:
            dentista = input('Digite o nome do dentista: ')
            adicionaDentista(dentista)
        case 3:
            dentista = input('Digite o nome do dentista: ')
            removerDentista(dentista)
        case 4:
            dentista = input('Digite o nome do dentista: ')
            buscarDentista(dentista)
        case 0:
            break
        case _:
            print('Opção inválida')
    print()
    input('Pressione ENTER para continuar...')

    