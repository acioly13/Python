# Ve se uma string é um isograma retorna True ou False

def is_isogram(s):
    return len(s) == len(set(s.lower()))

print(is_isogram('Dermatoglyphics'))