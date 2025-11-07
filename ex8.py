i = 0
soma = 0


while(i < 5):
    print('Coloque um numero: ')
    x = int(input('O numero: '))
    soma += x
    i +=1

mediaGeral = soma / 5
 
print(f'O valor da soma desses valores foram: {soma}')
print(f'A media geral é {mediaGeral}')