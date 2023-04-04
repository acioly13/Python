# recebe um texto e retorna se ele é um pangrama ou não

def is_pangram(s):
    return set(s.lower()) >= set('abcdefghijklmnopqrstuvwxyz')

print(is_pangram("The quick brown fox jumps over the lazy dog."))
print(is_pangram("This is not a pangram."))