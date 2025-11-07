i = 1
par = 0
impar = 0

while(i < 11):
    n = int(input('Digite um numero: '))
    if(n % 2 == 0):
        par += 1
    else:
        impar += 1
    i+=1

print(f'tem {par} pares e {impar} impares')