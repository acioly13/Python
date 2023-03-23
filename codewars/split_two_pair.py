# Recebe uma string e retorna uma lista de pares de caracteres se o ultimo caracter estiver sozinho, adicione um '_'.

def solution(s):
    if len(s) % 2 != 0:
        s += '_'
    return [s[i:i + 2] for i in range(0, len(s), 2)]


print(solution('abcde'))
