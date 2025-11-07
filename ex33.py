list_um = []

num = int(input('Digite quantos valores voce quer guuardar na lista: '))

while (num > 20 or num < 0):
    num = int(input('Valor invalido! Digite um valor entre 1 e 20: '))

for i in range(num):
    valor = int(input('Digite um valor inteiro para adicionar na lista: '))
    list_um.append(valor)

while True:
    consulta = int(input('Digite um valor para consultar na lista (ou -1 para sair): '))
    if consulta in list_um:
        posicao = list_um.index(consulta)
        print(f'Valor {consulta} encontrado na lista na posição {posicao}.')
    elif consulta == -1:
        print('Saindo da consulta.')
        break
    else:
        print(f'Valor {consulta} não encontrado na lista.')