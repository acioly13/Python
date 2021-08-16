peso = float(input('Digite o peso dos peixes: '))
extra = 0
multa = 0
if peso > 50:
    extra = peso - 50
    multa = extra * 4
print(f'Peso: {peso}')
print(f'Excesso: {extra}')
print(f'Multa: {multa}')
