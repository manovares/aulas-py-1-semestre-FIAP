nome = input('Digite o nome de usuario: ')
senha = input('Digite sua senha: ')

while(nome == senha):
    print('O nome de usuaria não pode ser o mesmo da senha!')
    senha = input('Tente novamente outra senha: ')