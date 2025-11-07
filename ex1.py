x = int(input('Digite uma nota de 0 - 10: '))

while(0 > x or x > 10):
    print('Apenas valores positivos até 10')
    x = int(input('Digite uma nota de 0 - 10: '))