import random

print(random.randrange(4))  # puxa um numero pseudoaleatorio entre 0 e 3
print(random.randint(1, 4))  # puxa um numero pseudoaleatorio entre 1 e 4
lista = [1, 2, 3, 4]
print(random.choice(lista))  # puxa um numero pseudoaleatorio da lista
print(random.sample(lista, 2))  # puxa dois numeros pseudoaleatorios da lista
