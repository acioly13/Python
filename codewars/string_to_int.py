# Recebe uma string e transforma em inteiro

def string_to_number(s):
    if s in '0123456789':
        return int(s)
    return s


print(string_to_number('122345'))
