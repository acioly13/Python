# Converte nomes em iniciais

def abbrev_name(name):
    return ".".join([n[0].upper() for n in name.split()])


print(abbrev_name("Rafael Daniel"))
print(abbrev_name("Rafael"))
print(abbrev_name("Daniel"))