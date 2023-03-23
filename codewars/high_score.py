# Recebe uma strig que cada caractere tem um score de acordo com o alfabeto e então retorna a soma dos scores

def high_score_word(s):
    alfabeto = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                'm': 13,
                'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
                'y': 25,
                'z': 26}

    lista = s.split(' ')
    lista_score = []
    for i in lista:
        score = 0
        for j in i:
            score += alfabeto[j]
        lista_score.append(score)
        a = lista_score.index(max(lista_score))
    return lista[a]


print(high_score_word('man i need a taxi up to ubud'))
