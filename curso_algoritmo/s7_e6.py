num = int(input('Digite um numero: '))
while num > 10:
    print('Numero tem que ser menor que 10')
    num = int(input('Digite um numero: '))
print(f'Tabuada de {num}')
for i in range(1,11):
    print(f' {num} x {i} = {num * i}')
