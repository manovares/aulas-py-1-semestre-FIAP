alunos = []

for i in range(2):
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")
    disciplina = input("Digite a disciplina do aluno: ")
    faltas = int(input("Digite as faltas do aluno: "))
    cp1 = float(input("Digite a nota da CP1 do aluno: "))
    cp2 = float(input("Digite a nota da CP2 do aluno: "))
    cp3 = float(input("Digite a nota da CP3 do aluno: "))

    aluno = {
        'nome': nome,
        'curso': curso,
        'disciplina': disciplina,
        'faltas': faltas,
        'cp1' : cp1,
        'cp2' : cp2,
        'cp3' : cp3
    }
    alunos.append(aluno)


print("Dados dos alunos:", alunos)

print("Aluno com faltas acima de 8:")

for aluno in alunos:
    if aluno['faltas'] > 8:
        print(aluno['nome'])