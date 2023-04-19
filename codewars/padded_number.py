# Recebe um inteiro e retorna uma string com o número Ex: 00005

def solution(value):
    return 'Value is' + ' ' + str(value).zfill(5)


print(solution(5))
