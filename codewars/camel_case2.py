# Transforma a string em camel case

def to_camel_case(string):
    return ''.join(word.capitalize() for word in string.split())


print(to_camel_case('test case'))