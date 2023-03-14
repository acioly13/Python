# Convert to Camel Case

def to_camel_case(texto):
    if len(texto) == 0:
        return ''
    else:
        texto = texto.replace('-', ' ').replace('_', ' ').split()
        return texto[0] + ''.join([palavra.capitalize() for palavra in texto[1:]])


# Teste
print(to_camel_case('the-stealth-warrior'))
print(to_camel_case('The_Stealth_Warrior'))
print(to_camel_case(''))
