# Pegar 2 listas e ver se o quadrado de uma se encontra na outra

def comp(lista1, lista2):
    try:
        return sorted([i ** 2 for i in lista1]) == sorted(lista2)
    except:
        return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(a1, a2))
