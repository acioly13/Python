peso = float(input('Digite o peso dos peixes: '))
if peso > 50:
    extra = peso - 50
    multa = extra * 4
else:
    extra = 0
    multa = 0
print(f'Peso: {peso}Kg')
print(f'Excesso: {extra}Kg')
print(f'Multa: R${multa}')
