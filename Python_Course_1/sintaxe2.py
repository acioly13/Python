nome = 'João Acioly'
print(len(nome))

dic = {'João': 24, 'Pedro': 20, 'Maria': 22, 'João Acioly': 24, 'Pedro Acioly': 20, 'Maria Acioly': 22, 'Nathália': 20}
for chave in dic:
    print(f'{chave} tem {dic[chave]} anos')

num0 = 0
while num0 < 11:
    print(num0)
    num0 += 1

num = 10
if num % 2 == 0:
    print('Par')


def teste_par(n):
    if n % 2 == 0:
        return True
    else:
        return False


print(teste_par(11))
