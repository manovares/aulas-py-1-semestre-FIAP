produtos = []

for i in range(3):
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor = float(input("Digite o valor do produto: "))

    produto = {
        'nome': nome,
        'descricao': descricao,
        'quantidade': quantidade,
        'valor': valor
    }
    produtos.append(produto)

print("Produtos cadastrados:")
for produto in produtos:
    print(produto)
print("\n")
print("Produtos com quantidade acima de 50 e valor abaixo de 500:")
for produto in produtos:
    if produto['quantidade'] > 50 and produto['valor'] < 500:
        print(produto['nome'])