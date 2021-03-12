amostra = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def senha(Senha, teste=''):
    global i
    if len(teste) == 0:
        i = 0
    if len(teste) == len(Senha):
        i += 1
        if teste == Senha:
            print('Senha: "{}" descoberta apos {} tentativas'.format(
                teste, str(i)))
            return True
        return False
    else:
        for c in amostra:
            if senha(Senha, teste + c):
                return True
        return False


x = input("Digite a senha: ").upper()
senha(x)
print("Alunos: Emanuel Guilherme ; Joao Acioly")
