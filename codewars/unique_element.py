# Recebe uma string de letras e/ou numeros e retorna de forma unica caso tenha repetido

def unique_in_order(sequence):
    result = []
    for i in sequence:
        if len(result) == 0 or i != result[-1]:
            result.append(i)
    return result


print(unique_in_order('AAAABBBCCDAABBB'))
