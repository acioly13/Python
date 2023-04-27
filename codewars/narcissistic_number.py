# Recebe um inteiro e retorna True se ele for um número narcisista, ou False caso contrário


def narcissistic(value):
    tamanho = len(str(value))
    soma = sum(int(cifra)**tamanho for cifra in str(value))
    if value == soma:
        return True
    return False


print(narcissistic(122))
