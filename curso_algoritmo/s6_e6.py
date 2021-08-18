extra = 0
c = input('Digite o codigo do funcionario: ')
horas = float(input('Digite as horas trabalhadas: '))
if horas > 50:
    extra = horas - 50
    salario = (horas - extra) * 10
    extra = extra * 20
    salario_t = salario + extra
    print(f'Salario Total: R${salario_t} reais')
    print(f'Extra: R${extra} reais')
else:
    salario = horas * 10
    print(f'Salario: R${salario} reais')

