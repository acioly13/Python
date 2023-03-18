# Função que recebe um inteiro(segundos) e retorna uma string no formato HH:MM:SS

def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f'{hours:02}:{minutes:02}:{seconds:02}'


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))