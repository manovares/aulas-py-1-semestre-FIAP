i = 0
maior = 0

while(i != 5):
    print('Digite um numero')
    x = int(input('Digite o numero: '))
    if(x > maior):
        maior = x
    i += 1

print(f'Maior numero é: {maior}')