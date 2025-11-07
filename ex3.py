nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite qual é o seu salario: '))
sexo = input('Digite qual seu sexo: (m ou f)')
estadoCivil = input('Digite seu estado civil:  ')

while(len(nome) < 3):
    print('Digite seu nome certo filho')
    nome = input('Digite seu nome: ')


while(idade < 0) or (idade > 150):
    print('Ponha a idade certo')
    idade = int(input('Digite sua idade: '))

while(salario < 0):
    print('Coloque seu salario certo!')
    salario = float(input('Digite qual é o seu salario: '))

while(sexo != "f") and (sexo != "m"):
    print('Apenas M ou F')
    sexo = input('Digite qual seu sexo: (m ou f)')

while(estadoCivil != "c") and (estadoCivil != 's') and (estadoCivil != 'v') and (estadoCivil != 'd'):
    print('Coloque o estado civil correto!')
    estadoCivil = input('Digite seu estado civil:  ')

print('Cadastro efetuado!')