lista_medias = []

qtde_maior_igual_7 = 0

for i in range(10):
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))
    media = (nota1 + nota2 + nota3) / 3
    lista_medias.append(media)