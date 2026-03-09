funcionarios = []

for i in range(2):
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    funcionario = {
        'nome': nome,'cargo': cargo,'salario': salario
    }
    funcionarios.append(funcionario)

print("Dados dos funcionarios:")
for funcionario in funcionarios:
    print(funcionario)
print("\n")

print("Funcionário com salário entre 5000 e 10000:")
for funcionario in funcionarios:
    if funcionario['salario'] >= 5000 and funcionario['salario'] <=10000:
        print(funcionario['nome'])