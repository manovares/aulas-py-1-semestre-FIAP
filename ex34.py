lista_numeros = []
lista_pares = []
lista_impares = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print("Lista original:", lista_numeros)
print("Números pares:", lista_pares)
print("Números ímpares:", lista_impares)