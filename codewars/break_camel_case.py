# Coloca espaço entre as palavras de uma camel case

def solution(s):
    return ''.join([' ' + c if c.isupper() else c for c in s])

print(solution('camelCase'))