# Retorna uma lista de nomes se tiver 4 caracteres

def friend(x):
    return [name for name in x if len(name) == 4]


print(friend(["Ryan", "Kieran", "Mark"]))