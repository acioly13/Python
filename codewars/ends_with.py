# Verifica se termina com a string passada como parâmetro

def solution(string, ending):
    return string.endswith(ending)


print(solution('abcde', 'cde'))  # True
print(solution('abcde', 'abc'))  # False