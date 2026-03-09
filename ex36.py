lista = []
lista_pares = []
lista_impares = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))  
    lista.append(numero)

    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)    


print("Números digitados:", lista)
print("Números pares:", lista_pares)       
print("Números ímpares:", lista_impares)
