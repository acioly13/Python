login = input('Digite o login: ')
senha = input('Digite a senha: ')
while senha == login:
    print('-'*5, ' Senha e login Não Podem ser IGUAIS ', '-'*5)
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')
