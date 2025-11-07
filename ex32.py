list_um = []
list_dois = []

for i in range(20):
    num = int(input("Digite um número inteiro: "))
    list_um.append(num)

const = int(input("Digite um número inteiro para multiplicação: "))

for i in range(20):
    numdois = list_um[i] * const
    list_dois.append(numdois)
    

print("Lista original:", list_um)
print("Lista multiplicada:", list_dois)

