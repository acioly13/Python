# João Pedro Fernandes Acioly - 201921070 - Maricá - 4 Periodo
# Entrada de dados
horas_trabalhadas = float(input('Digite as horas trabalhadas: '))
horas_extras = float(input('Digite as horas extras trabalhadas: '))

# Processamento de dados
valor_horas_trabalhadas = horas_trabalhadas * 50
valor_horas_extras = horas_extras * 65

salario_bruto = valor_horas_extras + valor_horas_trabalhadas
salario_liquido = salario_bruto - (salario_bruto*0.1)

# Saida de dados
print(f'Salario Bruto: {salario_bruto}')
print(f'Salario Liquido: {salario_liquido}')
