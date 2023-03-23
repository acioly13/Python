# Função que pega um numero entre 1 e 3999 e retorna o numero em romano

def num_roman(num):
    if num < 1 or num > 3999:
        return 'Numero invalido'
    romanos = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    result = ''
    for i in sorted(romanos.keys(), reverse=True):
        while num >= i:
            result += romanos[i]
            num -= i
    return result

print(num_roman(1))
