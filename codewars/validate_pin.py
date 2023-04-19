# Valida um pin com 4 ou 6 dígitos exatos

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


print(validate_pin("1234"))
print(validate_pin("12345"))
print(validate_pin("a234"))
print(validate_pin("123456"))
