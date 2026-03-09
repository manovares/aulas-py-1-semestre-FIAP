lista = []

for i in range(5):
    numero = float(input("Digite um número: "))
    lista.append(numero)

print("Soma dos números digitados:", sum(lista))
print("Média dos números digitados:", sum(lista) / len(lista))
print("Quantidade acima da media :", len([x for x in lista if x > sum(lista) / len(lista)]))
print("Quantidade abaixo da media :", len([x for x in lista if x < sum(lista) / len(lista)]))