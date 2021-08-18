import random
import string
import time

letras = string.ascii_uppercase
N = 2
senha = ''
senha = senha.join(random.choice(letras) for _ in range(N))
print(f'A senha: {senha}')
teste = ''
x = 0
inicio = time.time()
while teste != senha:
    teste = ""
    teste = teste.join(random.choice(letras) for _ in range(N))
    x += 1
fim = time.time()
print(f'Tempo de execução: {fim - inicio}')
print(f'Tentativas: {x}')
