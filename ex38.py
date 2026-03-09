media = []


for i in range(3):
    print("Digite a nota do aluno")
    nota = float(input("Digite a nota do aluno: "))
    nota2 = float(input("Digite a nota do aluno: "))
    nota3 = float(input("Digite a nota do aluno: "))
    print("\n")

    mediaalunos = (nota + nota2 + nota3) / 3
    alunosaprovados = 1
    if mediaalunos >= 7:
        alunosaprovados += 1
    media.append(mediaalunos)


print("Médias dos alunos:", media)
print("Quantidade de alunos aprovados:", alunosaprovados)